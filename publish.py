import subprocess
import shutil
from pathlib import Path

src_dir = Path('src')
content_dir = Path('content')
build_dir = Path('_build')

js_file = 'ASCIIMathTeXImg.js'
shutil.copy(src_dir / js_file, content_dir / js_file)

shutil.copytree(build_dir, content_dir / 'build', dirs_exist_ok=True)

cmd = [
  'ghp-import',
  '--no-jekyll',
  '--push',
  '--no-history',
  content_dir
]
subprocess.run(cmd)

print(f'Deployed to https://feihong.github.io/math-flashcards/')
