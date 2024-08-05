from app.models.user import User
from app.services.register.schemas import RegisterUserSchema


class RegisterService:
    @classmethod
    def register_user(cls, data: RegisterUserSchema):
        User.new(**data.model_dump())

    @classmethod
    def registered(cls, user_id: int):
        return bool(User.filter(id=user_id).one_or_none())
