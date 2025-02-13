import json

from .models import Webhook


def handle_webhook_event(json_data: str) -> Webhook:
    data_dict = json.loads(json_data)

    return Webhook(**data_dict)
