from typing import Tuple
import requests

from config import GPT_API_KEY, GPT_API_URL


class GPT:
    api_key = GPT_API_KEY
    base_url = GPT_API_URL

    @classmethod
    def send(cls, message, history) -> Tuple[str, int]:
        request_json = {
            "message": message,
            "api_key": cls.api_key,
            "history": history
        }

        response = requests.post(url=cls.base_url, json=request_json)

        if response.status_code != 200:
            raise Exception(response.status_code)
        
        resp_json = response.json()
        
        if resp_json['is_success']:
            return resp_json['response'], resp_json['used_words_count']
        else:
            raise Exception(resp_json["error_message"])