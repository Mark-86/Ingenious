from databases import DatabaseURL
from rsa import PublicKey
from starlette.config import Config
from starlette.datastructures import Secret
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

private_key ="""
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA40ws50iENO3Lw9NYaUpVje+/TgKgx/zEFreWdvgBlYxLu8aH
I5jN4Xh51Vo/bt+JK7CC66jEMsgjCKZDMhCPBAsPdTVYl+1zKkZwdMwjlTZyfTEx
JhCqkYPjYUOIcd1cinJph9mJ4hzuv78obstqRnkv55mAieyxjHB2aqVk7qAjA2S6
GMpdwoa6yeeJoC0Rz+v7AV5Sx+fYGuugjey3Vbe+in4j6yyPN/P9f4PvXYbWFxiJ
5w2i3cOOSlJQfyFzDlnHtWyuShr7Qvie8QLZLZa5HM3QL5kUlOBQYqdfW2lIDSui
i9kHKKOszgUF+wKMbJL7jAtJvICjDsPeO0+XHQIDAQABAoIBAQCMLdSbpwtyIR3D
3bnu5Zsx+CQBlnlWHTtJz1uKb5V6h5XFbsC1YW3Hmid5PzlTxaSxPyDe+axWrTt+
ABv86l1pXvDfllDXEegusFZ2kdd4FKYzM31ePnUTXUWEHMQvhRengrw2viDdRH6x
3tCu0+DtKZwzt2Wgqkstk8ZUK0C+MPccxLZTqsG9JUTpG394WpTpEsHGpc2Tl7sZ
lDcfXvBbPZLePmG+RrP+YihTcYlrVnlbn4WjU1WXet7qz3zkAXRF8eqTaiVsSJqp
37ulrC+AH4cAB4kuutLem3S13K1gZRv7PCLJV3avLgt3Xqf2D3nmcHXkkheTjm7n
On2oJ5P5AoGBAPImlnlb3cb5Uoh9gr4SZ3UA2k0V0qv+fWzS9k2rdZ/ll3xI/lhJ
StGFwKzCv0lStBudi4Gw1Oc7v6/ZAFG414WKL9SzuM45zcarTd9K0i6PRZpVMy/3
PO9wP838Gtnm5Fn5Du9P5gwVJ3vrdOfzfWemTLV9u74YmPS0bk5vZnRDAoGBAPBM
HgBVWMl1AivzFZstVT4iG4EK4A3xbKgnRHqzm3ZHg5j+Asdb9CU1gxdxudzs8N95
8CK1BLOB/QneibjTwJVqsCWRP2DkA/FMi6PVuFeKzV6tkZLQ7cMPr3LmVMNknknG
/aoQ7aXErNsag9v50TnD6oHdqsoYB2+WQYQTK8EfAoGACCHlodPFAf6zl+PnNSz3
DoXlzvrxpVcZrUL0hK1CeQlD6ielax+jBKBiVSsBM5w0ckz7N3LR46YtDOHT0erM
Si7W5mTWyw5D6+0q41nm7yteog1Ed9Ls1/nEGs3htPm9J4xmxQDA8Bzxw4an2XZi
+s0p/FppqLu4v1cj8Txqi3MCgYByyUmDi0Fwao5xBBuMFumjVpOg3tsMjgkDgk55
9pYKuDqquJwHM2u64ocOierpF94wQoVtbt8iCLQhJMbRHYXfWiluqKWH2SPw/kmu
J4d5efqEgZEKevc4uKNs1Y4kEEp0n7PIq3F6QCr6Nv5J9Fn3qBi7lHHjO/tBWJtP
RgEerQKBgGqoGOBWglKNZOsPDPqVZ7Tvy4/66cyNawrm852AX0r4C9PMeVyLSmaS
8k0oicYEjbPBAFshQSZ34T/s9BGliHESad+QQCStxar+1f6OfD7hfAh/NBPmS10D
6JgVyliYWTMjGdhot3oRjyNPOjhGTPHs4qxBuuUOnqaSqzznjOlY
-----END RSA PRIVATE KEY-----
"""

public_key= """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA40ws50iENO3Lw9NYaUpV
je+/TgKgx/zEFreWdvgBlYxLu8aHI5jN4Xh51Vo/bt+JK7CC66jEMsgjCKZDMhCP
BAsPdTVYl+1zKkZwdMwjlTZyfTExJhCqkYPjYUOIcd1cinJph9mJ4hzuv78obstq
Rnkv55mAieyxjHB2aqVk7qAjA2S6GMpdwoa6yeeJoC0Rz+v7AV5Sx+fYGuugjey3
Vbe+in4j6yyPN/P9f4PvXYbWFxiJ5w2i3cOOSlJQfyFzDlnHtWyuShr7Qvie8QLZ
LZa5HM3QL5kUlOBQYqdfW2lIDSuii9kHKKOszgUF+wKMbJL7jAtJvICjDsPeO0+X
HQIDAQAB
-----END PUBLIC KEY-----
"""


class Settings:

    PROJECT_NAME = os.getenv("PROJECT_NAME")
    PROJECT_DESCRIPTION = os.getenv("PROJECT_DESCRIPTION")
    API_ROOT_PATH: str = os.getenv("API_ROOT_PATH")
    VERSION = "0.0.1"
    SECRET_KEY = os.getenv("SECRET_KEY")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    DATABASE_URL = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True


class AuthJWTSettings(BaseSettings):
    authjwt_algorithm: str = "RS512"
    authjwt_public_key: str = public_key
    authjwt_private_key: str = private_key


settings = Settings()
auth_jwt_settings = AuthJWTSettings()
