from os import environ
from flask import Flask
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def kakao(path):
  session = OAuth2Session(environ.get('KAKAO_CLIENT_ID'),
                          environ.get('KAKAO_CLIENT_SECRET'),
                          redirect_uri=environ.get('KAKAO_REDIRECT_URI'),
                          scope=environ.get('KAKAO_SCOPE'))
  authorization_url, state = session.create_authorization_url('https://kauth.kakao.com/oauth/authorize')
  return {'authorization_url': authorization_url}