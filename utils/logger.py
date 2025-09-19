import datetime

def log(msg: str):
    print(f"[{datetime.datetime.now().isoformat()}] {msg}")
