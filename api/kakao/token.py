from os import environ
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def kakao(path):
  session = OAuth2Session(environ.get('KAKAO_CLIENT_ID'),
                          environ.get('KAKAO_CLIENT_SECRET'),
                          redirect_uri=environ.get('KAKAO_REDIRECT_URI'),
                          scope=environ.get('KAKAO_SCOPE'))

  try:
    authorization_response = request.form.get('authorization_response')
    return session.fetch_token('https://kauth.kakao.com/oauth/token',
                               grant_type='authorization_code',
                               authorization_response=authorization_response)
  except Exception as exception:
    return {'message': str(exception)}