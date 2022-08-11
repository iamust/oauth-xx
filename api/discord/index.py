from os import environ
from flask import Flask
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def discord(path):
  session = OAuth2Session(environ.get('DISCORD_CLIENT_ID'),
                          environ.get('DISCORD_CLIENT_SECRET'),
                          redirect_uri=environ.get('DISCORD_REDIRECT_URI'),
                          scope=environ.get('DISCORD_SCOPE'))
  authorization_url, state = session.create_authorization_url('https://discord.com/api/oauth2/authorize')
  return {'authorization_url': authorization_url}