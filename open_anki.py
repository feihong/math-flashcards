"""
Open Anki and force it to use anki-data as its data directory
"""
from pathlib import Path
import subprocess

anki_data = Path(__file__).parent / 'anki-data'

if not anki_data.exists():
  anki_data.mkdir()

subprocess.run([
  'open', '-a', 'Anki',
  '--args',
  '-b', anki_data,
])
