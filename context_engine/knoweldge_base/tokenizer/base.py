from abc import ABC, abstractmethod
from typing import List

from context_engine.models.data_models import Messages


class Tokenizer(ABC):

    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        pass

    @abstractmethod
    def detokenize(self, tokens: List[str]) -> str:
        pass

    def token_count(self, text: str, as_message: bool = False) -> int:
        return len(self.tokenize(text))

    @abstractmethod
    def messages_token_count(self, messages: Messages) -> int:
        pass
