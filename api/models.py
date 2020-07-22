
class Model:
    def to_dict(self):
        return NotImplementedError


class User(Model):
    def to_dict(self):
        return {}


class UserID(Model):
    def to_dict(self):
        return {}


class UserAuth(Model):
    def to_dict(self):
        return {}
