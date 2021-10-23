from os import environ
from flask import Flask
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def weibo(path):
  session = OAuth2Session(environ.get('WEIBO_CLIENT_ID'),
                          environ.get('WEIBO_CLIENT_SECRET'),
                          redirect_uri=environ.get('WEIBO_REDIRECT_URI'),
                          scope=environ.get('WEIBO_SCOPE'))
  authorization_url, state = session.create_authorization_url('https://api.weibo.com/oauth2/authorize')
  return {'authorization_url': authorization_url}
