from flask import Flask, request, session
from google.oauth2 import id_token
from google.auth.transport import requests

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 실제 애플리케이션에서는 안전한 키를 사용해야 합니다.

GOOGLE_CLIENT_ID = "your-google-client-id"  # Google API Console에서 받은 클라이언트 ID를 입력해주세요.

@app.route("/login_with_token", methods=["POST"])
def login_with_token():
    try:
        token = request.form.get("id_token")

        # Google의 공개 키로 ID 토큰을 검증합니다.
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return "잘못된 발행자", 401

        if idinfo['aud'] != GOOGLE_CLIENT_ID:
            return "잘못된 클라이언트 ID", 401

        # ID 토큰이 제대로 검증되면, 유저의 Google ID를 세션에 저장합니다.
        session["user"] = idinfo['sub']
        return "로그인에 성공했습니다."

    except ValueError:
        # 토큰이 유효하지 않거나 만료되었을 경우 ValueError를 발생시킵니다.
        return "토큰 검증에 실패했습니다.", 401
