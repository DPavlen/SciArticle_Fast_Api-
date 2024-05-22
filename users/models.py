from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    """Модель юзера. Описание в соответсвии с Алхимии vers.2."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    def __str__(self):
        return f"Пользователь {self.email}"
