import json

import allure
from allure_commons.types import AttachmentType


class Helper:
    def attach_response(self, response: str) -> None:
        response = json.dumps(obj=response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)
