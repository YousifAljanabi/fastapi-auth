from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy, CookieTransport
import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET")

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


JWT_Bearer_backend = AuthenticationBackend(
    name="jwt_bearer",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


JWT_Cookie_backend = AuthenticationBackend(
    name="jwt_cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


auth_backends = [JWT_Bearer_backend, JWT_Cookie_backend]
