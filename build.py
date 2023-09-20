from pathlib import Path
import shutil
import re

here = Path(__file__).parent
src_dir = here / 'src'
math_dir = src_dir / 'Math'
build_dir = here / '_build'

if build_dir.exists():
  shutil.rmtree(build_dir)
build_dir.mkdir()

math_build_dir = build_dir / 'Math'
math_build_dir.mkdir()

def apply_template(src_file: Path):
  output = src_file.read_text()

  def repl(match):
    filename = match.group(1)
    source = (src_dir / filename).read_text().strip()
    return f'<script>\n{source}\n</script>'

  output = re.sub(r'<!-- INCLUDE:(.*) -->', repl, output)

  output_file = math_build_dir / src_file.name
  output_file.write_text(output)
  print(f'Generated {output_file}')


shutil.copy(math_dir / 'styles.css', math_build_dir)
apply_template(math_dir / 'back.html')
apply_template(math_dir / 'front.html')
shutil.copytree(math_build_dir, build_dir / 'Math Cloze')
