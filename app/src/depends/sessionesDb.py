from app.config.DBConfig import SessionLocal

# Dependencia que nos proporciona la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()