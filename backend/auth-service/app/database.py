import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:admin123@postgres:5432/hospital"

engine = None

# Espera a que Postgres esté listo
for _ in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except Exception:
        time.sleep(2)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
