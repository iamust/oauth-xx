from os import environ
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def discord(path):
  session = OAuth2Session(environ.get('DISCORD_CLIENT_ID'),
                          environ.get('DISCORD_CLIENT_SECRET'),
                          redirect_uri=environ.get('DISCORD_REDIRECT_URI'),
                          scope=environ.get('DISCORD_SCOPE'))

  try:
    authorization_response = request.form.get('authorization_response')
    return session.fetch_token('https://discord.com/api/oauth2/token',
                               grant_type='authorization_code',
                               authorization_response=authorization_response)
  except Exception as exception:
    return {'message': str(exception)}