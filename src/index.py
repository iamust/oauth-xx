from os import environ
from flask import Flask
from authlib.integrations.requests_client import OAuth2Session

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def {{fname}}(path):
  session = OAuth2Session(environ.get('{{NAME}}_CLIENT_ID'),
                          environ.get('{{NAME}}_CLIENT_SECRET'),
                          redirect_uri=environ.get('{{NAME}}_REDIRECT_URI'),
                          scope=environ.get('{{NAME}}_SCOPE'))
  authorization_url, state = session.create_authorization_url('{{authorization_endpoint}}')
  return {'authorization_url': authorization_url}
