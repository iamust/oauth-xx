from os import environ
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def {{fname}}(path):
  session = OAuth2Session(environ.get('{{NAME}}_CLIENT_ID'),
                          environ.get('{{NAME}}_CLIENT_SECRET'),
                          redirect_uri=environ.get('{{NAME}}_REDIRECT_URI'),
                          scope=environ.get('{{NAME}}_SCOPE'))

  try:
    authorization_response = request.form.get('authorization_response')
    return session.fetch_token('{{token_endpoint}}',
                               grant_type='authorization_code',
                               authorization_response=authorization_response)
  except Exception as exception:
    return {'message': str(exception)}
