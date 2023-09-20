from pathlib import Path
import shutil
import re

here = Path(__file__).parent
src_dir = here / 'src'
build_dir = here / '_build'

if build_dir.exists():
  shutil.rmtree(build_dir)
build_dir.mkdir()

def apply_template(src_file: Path, output_model_dir: Path):
  output = src_file.read_text()

  def repl(match):
    filename = match.group(1)
    source = (src_dir / filename).read_text().strip()
    return f'<script>\n{source}\n</script>'

  output = re.sub(r'<!-- INCLUDE:(.*) -->', repl, output)

  output_file = output_model_dir / src_file.name
  output_file.write_text(output)
  print(f'Generated {output_file}')

for model in ['Math', 'Math Cloze']:
  model_dir = src_dir / model
  output_model_dir = build_dir / model
  output_model_dir.mkdir()
  apply_template(model_dir / 'back.html', output_model_dir)
  apply_template(model_dir / 'front.html', output_model_dir)
