from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Usuario
from app.schemas import LoginRequest, LoginResponse
from app.security import crear_token

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(
        Usuario.username == data.username,
        Usuario.password == data.password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = crear_token({
        "sub": user.username,
        "rol": user.rol
    })

    return LoginResponse( access_token=token, role=user.rol )

