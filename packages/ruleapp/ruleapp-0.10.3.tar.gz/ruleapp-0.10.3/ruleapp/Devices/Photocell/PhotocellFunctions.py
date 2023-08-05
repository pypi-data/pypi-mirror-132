from PhotocellDTO import Photocell
from ..DeviceEvaluationDTO import DeviceEvaluation
from PhotocellAntecedentFunctions import PhotocellAntecedentFunction


class PhotocellFunction(object):
    def __init__(self, redis):
        self.r = redis
        self.photocell_antecedent_functions = PhotocellAntecedentFunction(redis)

    def register(self, user_id, device_id):
        try:
            result = "false"
            key_pattern = "device:" + device_id
            if self.r.exists(key_pattern + ":name") == 0:
                self.r.rpush("user:" + user_id + ":sensors", device_id)
                device = Photocell()
                device.id = device_id
                device_id_keys = self.r.lrange("user:" + user_id + ":sensors")
                device.name = "PHOTOCELL " + str(len(device_id_keys))
                self.r.set(key_pattern + ":name", device.name)
                self.r.set(key_pattern + ":user_id", user_id)
                self.r.set(key_pattern + ":measure", device.measure)
                self.r.set(key_pattern + ":max_measure", device.max_measure)
                self.r.set(key_pattern + ":max_measure_time", device.max_measure_time)
                self.r.set(key_pattern + ":max_measure_date", device.max_measure_date)
                self.r.set(key_pattern + ":min_measure", device.min_measure)
                self.r.set(key_pattern + ":min_measure_time", device.min_measure_time)
                self.r.set(key_pattern + ":min_measure_date", device.min_measure_date)
                self.r.set(key_pattern + ":expiration", device.expiration)
                result = device
            return result
        except Exception as error:
            print(repr(error))
            return "error"

    def get_device(self, user_id, device_id):
        try:
            key_pattern = "device:" + device_id
            dto = Photocell()
            dto.id = device_id
            dto.name = self.r.get(key_pattern + ":name")
            dto.max_measure = self.r.get(key_pattern + ":max_measure")
            dto.max_measure_time = self.r.get(key_pattern + ":max_measure_time")
            dto.max_measure_date = self.r.get(key_pattern + ":max_measure_date")
            dto.min_measure = self.r.get(key_pattern + ":min_measure")
            dto.min_measure_time = self.r.get(key_pattern + ":min_measure_time")
            dto.min_measure_date = self.r.get(key_pattern + ":min_measure_date")
            dto.expiration = self.r.get(key_pattern + ":expiration")
            if self.r.exists(key_pattern + ":rules") == 1:
                rules_id = self.r.lrange(key_pattern + ":rules")
                for rule_id in rules_id:
                    rule_name = self.r.get("user:" + user_id + ":rule:" + rule_id + ":name")
                    dto.rules.append({"id": rule_id, "name": rule_name})
            if self.r.exists(key_pattern + ":measure") == 1:
                measure = self.r.get(key_pattern + ":measure")
                if measure == "-":
                    dto.measure = measure
                    dto.absolute_measure = measure
                    dto.color = "yellow"
                    dto.status = "initialization"
            return dto
        except Exception as error:
            print(repr(error))
            return "error"

    def update_device(self, new_device):
        try:
            dto = Photocell()
            dto.device_mapping(new_device)
            key_pattern = "device:" + dto.id
            self.r.set(key_pattern + ":name", dto.name)
            self.r.set(key_pattern + ":expiration", dto.expiration)
            return dto
        except Exception as error:
            print(repr(error))
            return "error"

    def delete_device(self, user_id, device_id):
        try:
            self.r.lrem("user:" + user_id + ":sensors", device_id)
            key_pattern = "device:" + device_id
            self.r.delete(key_pattern + ":name")
            self.r.delete(key_pattern + ":user_id")
            self.r.delete(key_pattern + ":measure")
            self.r.delete(key_pattern + ":max_measure")
            self.r.delete(key_pattern + ":max_measure_time")
            self.r.delete(key_pattern + ":max_measure_date")
            self.r.delete(key_pattern + ":min_measure")
            self.r.delete(key_pattern + ":min_measure_time")
            self.r.delete(key_pattern + ":min_measure_date")
            if self.r.exists(key_pattern + ":rules") == 1:
                rules = self.r.lrange(key_pattern + ":rules")
                for rule_id in rules:
                    self.photocell_antecedent_functions.delete_antecedent(user_id, rule_id, device_id)
        except Exception as error:
            print(repr(error))
            return "error"

    def measure_evaluation(self, device_id, measure):
        key_pattern = "device:" + device_id
        expiration = int(self.r.get(key_pattern + ":expiration")) + 2
        self.r.setex(key_pattern + ":measure", expiration, measure)
        return measure

    def device_evaluation(self, device_id, measure):
        output = DeviceEvaluation()
        key_pattern = "device:" + device_id
        if self.r.exists(key_pattern + ":user_id") == 1:
            output.user_id = self.r.get("device:" + device_id + ":user_id")
            output.measure = self.measure_evaluation(device_id, measure)
            output.device_id = device_id
            output.type = "antecedent"
            if self.r.exists(key_pattern + ":rules"):
                output.rules = self.r.lrange(key_pattern + ":rules")
        return output
