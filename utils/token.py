from typing import Dict
from datetime import datetime, timedelta, UTC
from jose import jwt, JWTError

from .env import SECRET, ALGORITHM

class Token:
    @staticmethod
    def encode_jwt(user_details: Dict, duration: timedelta = timedelta(minutes=30)) -> str:
        user_copy = user_details.copy()
        now = datetime.now(UTC)
        exp = now + duration
        user_copy.update({
            "iat": now,
            "exp": exp
        })
        return jwt.encode(user_copy, SECRET, algorithm=ALGORITHM)

    @staticmethod
    def decode_jwt(token: str) -> Dict:
        try:
            return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        except JWTError as e:
            raise e
