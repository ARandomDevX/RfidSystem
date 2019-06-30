from sql import Anmeldung
from zurück import b
import functions
import datetime


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import Abmelde


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    Abmelde.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    Abmelde.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:

    def __init__(self,top=None):
        import guicaller
        adfh(self)
        from Hauptmenü import Toplevel1
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#050154'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("621x417+406+183")
        top.title("Abmelden")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#f0f0f0")
        top.configure(highlightcolor="#646464")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.048, rely=0.192, height=21, width=134)
        self.Label1.configure(background="#d9d9d9", fg='#ffffff')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''RFID-Karte Oder Chip''')
        self.Label1.configure(width=134)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.258, rely=0.192, height=20, relwidth=0.506)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=314)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.789, rely=0.192, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Anmelden''')
        self.Button1.configure(width=87)
        self.Button1.configure(command=lambda : Anmeldung.anmelden(ort='Anmeldungs-Tisch',zeit=datetime.datetime.now(),incident='ABMELDUNG ERFOLGREICH BEENDET',id=self.Entry1,status='nein'))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.032, rely=0.887, height=24, width=77)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Zurück''')
        self.Button2.configure(width=77)
        self.Button2.configure(command=lambda : guicaller.call_Hauptmenu())


if __name__ == '__main__' or __name__ != '__main__':
    vp_start_gui()
