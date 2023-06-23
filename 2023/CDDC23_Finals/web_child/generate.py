import jwt
from datetime import datetime, timedelta

key = "7His_iS_Jwt_SEcrE7_KEy"
key = "JWT_Secret_Key"

payload = {
    'id': "admin",
    'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
}
token = jwt.encode(payload, key, 'HS256')
print(token)

print(jwt.decode(token, key, "HS256"))