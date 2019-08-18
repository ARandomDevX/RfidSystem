import sys
global lv
lv = None

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
class login:
    
class Toplevel1:
    def __init__(self,top=None):
        colorcode = open('colorcode.txt')

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#050154'  # X11 color: 'gray85'
        _fgcolor = '#050154'  # X11 color: 'black'
        _compcolor = '#050154' # X11 color: 'gray85'
        _ana1color = '#050154' # X11 color: 'gray85'
        _ana2color = '#050154' # Closest X11 color: 'gray92'

        top.geometry("600x450+443+244")
        top.title("Hauptmenü")
        top.configure(background="#050154")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.2, rely=0.244, height=24, width=337)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Anmelden''')
        self.Button1.configure(width=337)
        self.Button1.configure(command=Anmelden)

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.2, rely=0.311, height=24, width=337)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Abmelden''')
        self.Button1_1.configure(command=Abmelden)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.2, rely=0.378, height=24, width=337)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Sonstiges''')
        self.Button2.configure(width=337)
        self.Button2.configure(command= Sonstiges)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.117, rely=0.089, height=21, width=434)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#e20000")
        self.Label1.configure(text='''Wilkommen!''')
        self.Label1.configure(width=434)
class  Anmelden:
    def __init__(self):
        import font_vars
        import datetime
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#050154'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("621x417+406+183")
        top.title("Anmelden")
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

        self.var = StringVar()
        self.var.set(str(self.Entry1.get()))

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
        self.Button1.configure(command=Anmeldung.anmelden(ort='Anmeldungs-Tisch', zeit=datetime.datetime.now(),
                                                          incident='ANMELDUNG ERFOLGREICH BEENDET', id=self.var,
                                                          status='ja'))

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
        self.Button2.configure(command=Toplevel1)
class Sonstiges:
    def __init__(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#050154'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+455+225")
        top.title("Sonstige Optionen")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.167, rely=0.044, height=21, width=394)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Optionen:''')
        self.Label1.configure(width=394)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.383, rely=0.133, height=24, width=157)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Notfall''')
        self.Button1.configure(width=157)
        self.Button1.configure(command=raise_frame(t1))

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.383, rely=0.2, height=24, width=157)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Schüler Registrieren''')
        self.Button1_1.configure(command=Schritt1)

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.383, rely=0.267, height=24, width=157)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Schüler Löschen''')
        self.Button1_2.configure(command=S)

        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.017, rely=0.911, height=24, width=127)
        self.Button1_3.configure(activebackground="#ececec")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Zurück''')
        self.Button1_3.configure(width=127)
        self.Button1_3.configure(command=Toplevel1)

        self.Button1_5 = tk.Button(top)
        self.Button1_5.place(relx=0.383, rely=0.333, height=24, width=157)
        self.Button1_5.configure(activebackground="#ececec")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#d9d9d9")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(foreground="#000000")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(text='''Schüler status verändern''')
        self.Button1_5.configure(comand=Sst)
class Abmelden:
    def __init__(self):
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
        self.Button1.configure(command=lambda: Anmeldung.anmelden(ort='Anmeldungs-Tisch', zeit=datetime.datetime.now(),
                                                                  incident='ABMELDUNG ERFOLGREICH BEENDET',
                                                                  id=self.Entry1, status='nein'))

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
        self.Button2.configure(command=Toplevel1())
class Sst:
    from sql import sst
    from sql import ortvar
    '''This class configures and populates the toplevel window.
       top is the toplevel containing window.'''
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'

    top.geometry("600x450+482+265")
    top.title("Schüler status verändern")
    top.configure(background="#050154")

    self.Entry1 = tk.Entry(top)
    self.Entry1.place(relx=0.35, rely=0.444, height=20, relwidth=0.39)
    self.Entry1.configure(background="white")
    self.Entry1.configure(disabledforeground="#a3a3a3")
    self.Entry1.configure(font="TkFixedFont")
    self.Entry1.configure(foreground="#000000")
    self.Entry1.configure(insertbackground="black")
    self.Entry1.configure(width=234)

    duo = self.Entry1
    self.Button = tk.Button(top)
    self.Button.place(relx=0.45, rely=0.300, height=30, relwidth=0.39)
    self.Button.configure(command=lambda: sst.sst(id=duo.get(), self=None))
    self.Button.configure(text='Fertig')

    self.Radiobutton1 = tk.Radiobutton(top)
    self.Radiobutton1.place(relx=0.25, rely=0.2, relheight=0.056
                            , relwidth=0.08)
    self.Radiobutton1.configure(activebackground="#ececec", variable=ortvar, value="hof")
    self.Radiobutton1.configure(activeforeground="#000000")
    self.Radiobutton1.configure(background="#050154")
    self.Radiobutton1.configure(disabledforeground="#a3a3a3")
    self.Radiobutton1.configure(foreground="#ffffff")
    self.Radiobutton1.configure(highlightbackground="#d9d9d9")
    self.Radiobutton1.configure(highlightcolor="black")
    self.Radiobutton1.configure(justify='left')
    self.Radiobutton1.configure(text='''Hof''')

    self.Radiobutton1_1 = tk.Radiobutton(top)
    self.Radiobutton1_1.place(relx=0.25, rely=0.244, relheight=0.056
                              , relwidth=0.097)
    self.Radiobutton1_1.configure(activebackground="#ececec", variable=ortvar, value="garten")
    self.Radiobutton1_1.configure(activeforeground="#000000")
    self.Radiobutton1_1.configure(background="#050154")
    self.Radiobutton1_1.configure(disabledforeground="#a3a3a3")
    self.Radiobutton1_1.configure(foreground="#ffffff")
    self.Radiobutton1_1.configure(highlightbackground="#d9d9d9")
    self.Radiobutton1_1.configure(highlightcolor="black")
    self.Radiobutton1_1.configure(justify='left')
    self.Radiobutton1_1.configure(text='''Garten''')

    self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
    top.configure(menu=self.menubar)

    self.Radiobutton1_2 = tk.Radiobutton(top)
    self.Radiobutton1_2.place(relx=0.233, rely=0.333, relheight=0.056
                              , relwidth=0.213)
    self.Radiobutton1_2.configure(activebackground="#ececec", variable=ortvar, value="sonstiges")
    self.Radiobutton1_2.configure(activeforeground="#000000")
    self.Radiobutton1_2.configure(background="#050154")
    self.Radiobutton1_2.configure(disabledforeground="#a3a3a3")
    self.Radiobutton1_2.configure(foreground="#ffffff")
    self.Radiobutton1_2.configure(highlightbackground="#d9d9d9")
    self.Radiobutton1_2.configure(highlightcolor="black")
    self.Radiobutton1_2.configure(justify='left')
    self.Radiobutton1_2.configure(text='''Sonstiges / BeWe''')
    self.Radiobutton1_2.configure(width=128)

    self.Radiobutton1_3 = tk.Radiobutton(top)
    self.Radiobutton1_3.place(relx=0.233, rely=0.289, relheight=0.056
                              , relwidth=0.147)
    self.Radiobutton1_3.configure(activebackground="#ececec", variable=ortvar, value="bücherei")
    self.Radiobutton1_3.configure(activeforeground="#000000")
    self.Radiobutton1_3.configure(background="#050154")
    self.Radiobutton1_3.configure(disabledforeground="#a3a3a3")
    self.Radiobutton1_3.configure(foreground="#ffffff")
    self.Radiobutton1_3.configure(highlightbackground="#d9d9d9")
    self.Radiobutton1_3.configure(highlightcolor="black")
    self.Radiobutton1_3.configure(justify='left')
    self.Radiobutton1_3.configure(text='''Bücherei''')
    self.Radiobutton1_3.configure(width=88)

    self.Label1 = tk.Label(top)
    self.Label1.place(relx=0.083, rely=0.089, height=21, width=314)
    self.Label1.configure(background="#050154")
    self.Label1.configure(disabledforeground="#a3a3a3")
    self.Label1.configure(foreground="#ffffff")
    self.Label1.configure(text='''Schüler Status Verändern''')
    self.Label1.configure(width=314)

    self.Button1 = tk.Button(top)
    self.Button1.place(relx=0.017, rely=0.933, height=24, width=127)
    self.Button1.configure(activebackground="#ececec")
    self.Button1.configure(activeforeground="#000000")
    self.Button1.configure(background="#d9d9d9")
    self.Button1.configure(disabledforeground="#a3a3a3")
    self.Button1.configure(foreground="#000000")
    self.Button1.configure(highlightbackground="#d9d9d9")
    self.Button1.configure(highlightcolor="black")
    self.Button1.configure(pady="0")
    self.Button1.configure(text='''Zurück''')
    self.Button1.configure(width=127)

    self.Label2 = tk.Label(top)
    self.Label2.place(relx=0.2, rely=0.444, height=21, width=84)
    self.Label2.configure(background="#d9d9d9")
    self.Label2.configure(disabledforeground="#a3a3a3")
    self.Label2.configure(foreground="#000000")
    self.Label2.configure(text='''Chip oder karte''')
    self.Label2.configure(width=84)
class Schritt1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+404+263")
        top.title("New Toplevel")
        top.configure(background="#050154")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.317, rely=0.111, height=20, relwidth=0.423)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=254)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.089, height=31, width=114)
        self.Label1.configure(activebackground="#050154")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(background="#050154")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#050154")
        self.Label1.configure(highlightcolor="#646464")
        self.Label1.configure(text='''Name''')
        self.Label1.configure(width=114)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.317, rely=0.244, height=20, relwidth=0.423)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=254)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.244, height=21, width=104)
        self.Label2.configure(background="#050154")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Nach name''')
        self.Label2.configure(width=104)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.467, rely=0.444, height=24, width=277)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Schritt 2''')
        self.Button1.configure(width=277)
        self.Button1.configure(command=Schritt2)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.0, rely=0.444, height=24, width=277)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Zurück''')
        self.Button2.configure(width=277)
        self.Button2.configure(command=Sonstiges)
class Schritt2:
    def __init__(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#050154'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("1440x837+487+188")
        top.title("Schritt 2")
        top.configure(background="#050154")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.118, rely=0.06, height=20, relwidth=0.267)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=384)

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.118, rely=0.119, height=20, relwidth=0.267)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")
        self.Entry1_1.configure(width=384)

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(relx=0.118, rely=0.179, height=20, relwidth=0.267)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")
        self.Entry1_2.configure(width=384)

        self.Entry1_3 = tk.Entry(top)
        self.Entry1_3.place(relx=0.118, rely=0.239, height=90, relwidth=0.267)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="#c4c4c4")
        self.Entry1_3.configure(selectforeground="black")
        self.Entry1_3.configure(width=384)

        self.Entry1_4 = tk.Entry(top)
        self.Entry1_4.place(relx=0.118, rely=0.358, height=20, relwidth=0.267)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="#c4c4c4")
        self.Entry1_4.configure(selectforeground="black")
        self.Entry1_4.configure(width=384)

        self.Entry1_5 = tk.Entry(top)
        self.Entry1_5.place(relx=0.118, rely=0.418, height=20, relwidth=0.267)
        self.Entry1_5.configure(background="white")
        self.Entry1_5.configure(disabledforeground="#a3a3a3")
        self.Entry1_5.configure(font="TkFixedFont")
        self.Entry1_5.configure(foreground="#000000")
        self.Entry1_5.configure(highlightbackground="#d9d9d9")
        self.Entry1_5.configure(highlightcolor="black")
        self.Entry1_5.configure(insertbackground="black")
        self.Entry1_5.configure(selectbackground="#c4c4c4")
        self.Entry1_5.configure(selectforeground="black")

        self.Entry1_6 = tk.Entry(top)
        self.Entry1_6.place(relx=0.215, rely=0.454, height=70, relwidth=0.169)
        self.Entry1_6.configure(background="white")
        self.Entry1_6.configure(disabledforeground="#a3a3a3")
        self.Entry1_6.configure(font="TkFixedFont")
        self.Entry1_6.configure(foreground="#000000")
        self.Entry1_6.configure(highlightbackground="#d9d9d9")
        self.Entry1_6.configure(highlightcolor="black")
        self.Entry1_6.configure(insertbackground="black")
        self.Entry1_6.configure(selectbackground="#c4c4c4")
        self.Entry1_6.configure(selectforeground="black")
        self.Entry1_6.configure(width=244)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.06, height=21, width=154)
        self.Label1.configure(background="#050154")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''RFID Karte Oder Chip''')
        self.Label1.configure(width=154)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.007, rely=0.131, height=21, width=134)
        self.Label2.configure(background="#050154")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Mutter name''')
        self.Label2.configure(width=134)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.0, rely=0.191, height=21, width=154)
        self.Label3.configure(background="#050154")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Vater name''')
        self.Label3.configure(width=154)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.028, rely=0.275, height=21, width=94)
        self.Label4.configure(background="#050154")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(text='''Adressen''')
        self.Label4.configure(width=94)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.014, rely=0.358, height=21, width=124)
        self.Label5.configure(background="#050154")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#ffffff")
        self.Label5.configure(text='''Tel.Mutter''')
        self.Label5.configure(width=124)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.0, rely=0.418, height=21, width=154)
        self.Label6.configure(background="#050154")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#ffffff")
        self.Label6.configure(text='''Tel.Vater''')
        self.Label6.configure(width=154)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.007, rely=0.012, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Zurück''')
        self.Button1.configure(width=87)
        self.Button1.configure(command=Schritt1)
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.069, rely=0.012, height=24, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Schritt3''')
        self.Button2.configure(width=97)
        self.Button2.configure(command=Schritt3)
class Schritt3:
    def __init__(self):
        karte = Schritt2.Entry1.get()
        mutterName = Schritt2.Entry1_1.get()
        VaterName = Schritt2.Entry1_2.get()
        Add = Schritt2.Entry1_3.get()
        tm = Schritt2.Entry1_4.get()
        tv = Schritt2.Entry1_5.get()
        from sql import nsa
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1440x837+485+226")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.TSizegrip2 = ttk.Sizegrip(top)
        self.TSizegrip2.place(anchor='se', relx=1.0, rely=1.0)

        self.TSizegrip3.place(anchor='se', relx=1.0, rely=1.0)

        self.style.map('TRadiobutton', background=
        [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton1 = ttk.Radiobutton(top)
        self.TRadiobutton1.place(relx=0.049, rely=0.167, relwidth=0.119
                                 , relheight=0.0, height=21)
        self.TRadiobutton1.configure(takefocus="")
        self.TRadiobutton1.configure(text='''Soll gerade angemeldet sein''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.09, rely=0.119, relheight=0.025
                           , relwidth=0.088)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.049, rely=0.131, height=19, width=36)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Klasse''')

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.083, rely=0.311, relwidth=0.257
                                 , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="370")
        self.TProgressbar1.configure(variable=Schritt3_support.probar)
        self.TProgressbar1.configure(value="1.0")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.181, rely=0.454, height=25, width=76)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Fertig''')
        self.TButton1.configure(command=nsa.nsa())

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.014, rely=0.358, relwidth=0.396)
class l:
    def __init__(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("580x464+658+510")
        top.title("Entfernen")
        top.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.345, rely=0.183, height=26, relwidth=0.61)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=354)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.052, rely=0.172, height=31, width=127)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''RFID Karte''')
        self.Label1.configure(width=127)

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.121, rely=0.474, relwidth=0.81
                                 , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="470")
        self.TProgressbar1.configure(variable=unknowen_support.prbarvar)
        self.TProgressbar1.configure(value="10")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=-0.017, rely=0.388, relwidth=1.069)

        self.Checkbutton1 = tk.Checkbutton(top)
        self.Checkbutton1.place(relx=0.086, rely=0.28, relheight=0.08
                                , relwidth=0.36)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.414, rely=0.582, height=35, width=130)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Start''')
        self.TButton1.configure(width=130)

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.TSizegrip2 = ttk.Sizegrip(top)
        self.TSizegrip2.place(anchor='se', relx=1.0, rely=1.0)
