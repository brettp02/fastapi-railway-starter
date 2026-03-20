from typing import Annotated

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from sqlmodel import select

from app.db.database import SessionDep
from app.models.user import User

api_key_header = APIKeyHeader(name="X-API-Key")


def get_current_user(
    session: SessionDep,
    api_key: str = Security(api_key_header),
) -> User:
    user = session.exec(select(User).where(User.api_key == api_key)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is inactive",
        )
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]