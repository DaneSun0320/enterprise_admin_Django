
import datetime
import jwt

SECRET_KEY = "covidadmin"

headers = {
    'alg': "HS256",  # 声明所使用的算法
}

EXP_TIME = 60 * 60 * 12 # 设置12小时过期


def create_token(id):
    payload = {
        'iat':datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=0, minutes=0, seconds=EXP_TIME),
        'id': id
    }
    return jwt.encode(payload=payload, key=SECRET_KEY, algorithm='HS256')

def verify(token):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, verify=True, algorithms='HS256')
        return 1,payload.get("id")
    except Exception as e:
        return 0,None

if __name__ == "__main__":
    print(verify("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDM3ODA4NjUsImV4cCI6MTY0Mzc4MDg2NiwidXNlcm5hbWUiOiJhYWEifQ.OYivr_H3IEc5AnghyzLX7qRxx3a8gGTvslkptyerXEs"))