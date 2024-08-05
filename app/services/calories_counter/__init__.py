from typing import List

from app.exceptions import TooLongDescriptionException, IllegibilityException
from config import GPT_SYSTEM_MESSAGE
from messages_config import MAX_LONG_DESC
from utils.gpt import GPT


class CaloriesCounterService:
    @classmethod
    def count_cpfc(cls, text: str) -> List[int]:
        if len(text) > MAX_LONG_DESC:
            raise TooLongDescriptionException
        
        response, _ = GPT.send(message=text, history=[{"role": "system", "content": GPT_SYSTEM_MESSAGE}])

        if response == "exc":
            raise IllegibilityException
        
        return [int(float(i)) for i in response.split(', ')]
