from typing import List, Dict

class ConversationMemory:
    def __init__(self, max_messages: int = 20):
        self.messages: List[Dict[str, str]] = []
        self.max_messages = max_messages

    def add_user_message(self, content: str):
        self.messages.append({"role": "user", "content": content})
        self._truncate()

    def add_assistant_message(self, content: str):
        self.messages.append({"role": "assistant", "content": content})
        self._truncate()

    def get_messages(self) -> List[Dict[str, str]]:
        return self.messages

    def clear(self):
        self.messages = []

    def _truncate(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
