from apis.users.payloads import Payloads
from utils.helper import Helper


class Users(Helper):
    def __init__(self):
        super().__init__()
        self.payload = Payloads()
