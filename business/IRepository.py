from abc import ABC, abstractmethod
from business.UserStory import UserStory


class IRepository(ABC):
    @abstractmethod
    def get(self, id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, user_story: UserStory):
        pass

    @abstractmethod
    def update(self, user_story_id: str, user_story: UserStory):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass