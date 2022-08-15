from abc import abstractmethod, ABC
from typing import List
from app.config.config_parser import IConfigParser


__all__ = ['IConfigFactory']


class IConfigFactory(ABC):
    @classmethod
    @abstractmethod
    def config_types(cls) -> List[str]:
        pass

    @abstractmethod
    def get_parser(self) -> IConfigParser:
        pass
