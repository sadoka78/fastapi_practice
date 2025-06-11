from jose import JWTError,jwt
from datetime import datetime,timedelta
from config import SECRET_KEY ,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES )
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM )
    return encoded_jwt
