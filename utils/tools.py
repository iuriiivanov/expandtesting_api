import json
from typing import Any

import allure
from allure_commons.types import AttachmentType


class Helper:
    def attach_response(self, response: str) -> None:
        response = json.dumps(obj=response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    def attach_value(self, value: str | int | float | list[Any] | dict[Any, Any]) -> None:
        allure.attach(body=value, name="Value from the test", attachment_type=AttachmentType.TEXT)
