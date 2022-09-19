import os
from databases import Database
import uvicorn
from fastapi import FastAPI
from os import environ
from dotenv import load_dotenv

from routers import vowels

# loads env variables from .env file
# don't commit .env file to git
curr_file_path = os.path.realpath(__file__)
curr_directory = os.path.split(curr_file_path)[0]
env_path = os.path.join(curr_directory, "../.env")
load_dotenv(env_path)

ENV = environ

database = Database(ENV['DATABASE_URL'])
app = FastAPI()

# router docs in https://fastapi.tiangolo.com/tutorial/bigger-applications/
app.include_router(vowels.router)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def startup():
    await database.disconnect()


@app.get("/")
async def hello_world():
    """Shows env var VAR1"""
    return ENV.get('VAR1')


if __name__ == '__main__':
    # add port to .env file (any port, 8000, for example)
    uvicorn.run('app.main:app',
                host='0.0.0.0',
                port=int(ENV['PORT']),
                reload=True,
                log_level='info')
