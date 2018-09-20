from datetime import datetime

def nowTime():
    now = datetime.now()
    now = str(now)
    now = now[:19]
    now = now.replace("-", "/")
    return now