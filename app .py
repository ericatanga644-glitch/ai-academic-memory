from pathlib import Path

source = Path(__file__).with_name("app.py")
exec(compile(source.read_bytes(), str(source), "exec"))
