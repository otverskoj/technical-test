from abc import ABC, abstractmethod

from app.config.models.app import ApplicationConfig


class IConfigParser(ABC):
    @abstractmethod
    def get_config(self, config_path: str) -> ApplicationConfig:
        pass
