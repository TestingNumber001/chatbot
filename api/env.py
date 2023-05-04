from dotenv import load_dotenv as _load
_load()

from os import environ as _env

class _Env():
    def __getattribute__(self, __name: str) -> str | None:
        return _env.get(__name)
    
env = _Env()