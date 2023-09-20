"""
Update Anki model templates
"""
from pathlib import Path
import requests

here = Path(__file__).parent
build_dir = here / '_build'

def invoke(action, **params):
  data = {'action': action, 'version': 6}
  if params:
    data['params'] = params
  # print(data)
  r = requests.post('http://127.0.0.1:8765', json=data)
  return r.json()

def update_model_template(model_dir: Path):
  name = model_dir.name
  front_file = model_dir / 'front.html'
  back_file = model_dir / 'back.html'

  template_name = 'Cloze' if 'Cloze' in name else 'Card 1'

  model = {
    'name': name,
    'templates': {
      template_name: {
        'Front': front_file.read_text(),
        'Back': back_file.read_text(),
      }
    }
  }
  invoke('updateModelTemplates', model=model)
  print(f'Updated template for {name}')

for model_dir in build_dir.iterdir():
  update_model_template(model_dir)
