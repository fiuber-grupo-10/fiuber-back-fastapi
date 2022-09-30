import uvicorn
from fastapi import FastAPI
from app.config import settings
from app.database.db import create_session_from_url

app = FastAPI()


def get_db():
    db_session = create_session_from_url(settings.database_url)()
    try:
        yield db_session
    finally:
        db_session.close()


@app.get('/')
def home():
    return "Hello World"


if __name__ == '__main__':
    # add port to .env file (any port, 8000, for example)
    uvicorn.run('app.main:app',
                host='0.0.0.0',
                port=int(settings.port),
                reload=True,
                log_level='info')
