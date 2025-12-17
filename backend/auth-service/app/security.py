from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 60

def crear_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
