from os import environ
from flask import Flask
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def google(path):
  session = OAuth2Session(environ.get('GOOGLE_CLIENT_ID'),
                          environ.get('GOOGLE_CLIENT_SECRET'),
                          redirect_uri=environ.get('GOOGLE_REDIRECT_URI'),
                          scope=environ.get('GOOGLE_SCOPE'))
  authorization_url, state = session.create_authorization_url('https://accounts.google.com/o/oauth2/auth')
  return {'authorization_url': authorization_url}