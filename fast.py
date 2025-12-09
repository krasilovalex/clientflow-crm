from app.core.security import get_password_hash, verify_password

h = get_password_hash("a" * 200)
print(h)

print(verify_password("a" * 200, h))
print(verify_password("wrong", h))
