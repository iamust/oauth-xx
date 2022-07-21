from jinja2 import Environment, FileSystemLoader
from glob import glob
import json
import re

environment = Environment(loader=FileSystemLoader('src'))
replacer = lambda path: re.sub(r'^src\/', '', path)
paths = list(map(replacer, glob('src/*.py')))

with open('./providers.json', 'r') as config:
  providers = json.load(config)

  for name in providers.keys():
    for path in paths:
      template = environment.get_template(path)

      with open(f'./api/{name}/{path}', 'w') as output:
        output.write(template.render(NAME=name.upper(), fname=name, **providers[name]))
