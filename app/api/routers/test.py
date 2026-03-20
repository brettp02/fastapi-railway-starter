from fastapi import APIRouter, HTTPException, status

from app.core.security import CurrentUser
from app.db.database import SessionDep

TOKEN_COST = 5

router = APIRouter(
    prefix="/test",
    tags=["test"],
)


@router.get("", status_code=status.HTTP_200_OK)
def test_endpoint(current_user: CurrentUser, session: SessionDep) -> dict:
    if current_user.tokens < TOKEN_COST:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=f"Insufficient tokens. Required: {TOKEN_COST}, available: {current_user.tokens}",
        )
    current_user.tokens -= TOKEN_COST
    session.add(current_user)
    session.commit()
    return {"message": "success", "tokens_remaining": current_user.tokens}
