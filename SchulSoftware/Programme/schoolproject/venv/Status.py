from sql import cur, mydb2
cur2 = mydb2.cursor(buffered=True)
from datetime import *
cur.execute("SELECT * FROM stat.stat")
cur2.execute("SELECT * FROM stat.anzahl")

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Bücherei', 'Garten', 'Hof', 'Sonstiges')
y_pos = cur.fetchall()
performance = ["90+",80,70,60,50,"40-"]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Benutzung')
plt.title('Status von {}'.format(datetime.datetime.now()))

plt.show()