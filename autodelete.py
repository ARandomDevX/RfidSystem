import time
from sql import cur

class adfh:
    def __init__(self):
        while 1!=2:
            time.sleep(14400)
            cur.execute('TRUNCATE meldung')