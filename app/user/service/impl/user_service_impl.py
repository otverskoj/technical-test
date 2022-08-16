from uuid import UUID

from app.user.models.user import User
from app.user.models.user_in_db import UserInDB
from app.user.service.core.user_service import IUserService
from app.user.repositories.core.user_repository import IUserRepository


class UserServiceImpl(IUserService):
    __slots__ = ('__user_repo',)

    def __init__(self, user_repo: IUserRepository) -> None:
        self.__user_repo = user_repo

    def create_user(self, user: User) -> UserInDB:
        return self.__user_repo.create(user)
        
    def get_user_by_id(self, user_id: UUID) -> UserInDB:
        return self.__user_repo.get_by_id(user_id)

    def update_user(self, user_id: UUID, user: User) -> UserInDB:
        return self.__user_repo.update(user_id, user)

    def delete_user(self, user_id: UUID) -> None:
        self.__user_repo.delete(user_id)
