import base64
import zlib

class Hasher:
    def __init__(self, hash_mode: int = 2):
        self.hash_mode = hash_mode
        # 1 = Nur Base64 encoding 
        # 2 = Zusätzliches Compressing
        self.author = "harimtim"
        self.date = "07.07.2025"
        self.github = "https://github.com/harimtim/PassManager"

        if self.hash_mode not in (1, 2):
            raise ValueError("HashMode muss entweder 1 oder 2 sein!")

    def hash_password(self, password: str) -> str:
        if self.hash_mode == 1:
            return base64.b64encode(password.encode())
        if self.hash_mode == 2:
            return zlib.compress(base64.b64encode(password.encode()))
        
    def unhash(self, hash_to_unhash: bytes) -> str:
        if self.hash_mode == 1:
            return base64.b64decode(hash_to_unhash).decode()
        if self.hash_mode == 2:
            return base64.b64decode(zlib.decompress(hash_to_unhash)).decode()
