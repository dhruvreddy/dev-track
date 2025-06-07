from passlib.context import CryptContext

class Hashing():
    _context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def get_hash(password: str) -> str:
        return Hashing._context.hash(password)

    @staticmethod
    def verify_hash(hashed: str, plain: str) -> bool:
        return Hashing._context.verify(plain, hashed)