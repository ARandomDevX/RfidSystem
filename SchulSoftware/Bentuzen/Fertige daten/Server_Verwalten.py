import requests


def Server():
    '''This class configures and populates the toplevel window.
    top is the toplevel containing window.'''
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font10 = "-family {Segoe UI Black} -size 17 -weight bold "  \
    "-slant roman -underline 0 -overstrike 0"
    self.style = ttk.Style()
    if sys.platform == "win32":
    self.style.theme_use('winnative')
    self.style.configure('.',background=_bgcolor)
    self.style.configure('.',foreground=_fgcolor)
    self.style.configure('.',font="TkDefaultFont")
    self.style.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])

    top.geometry("590x549+838+407")
    top.title("Server verwalten")
    top.configure(background="#d9d9d9")

    self.Label1 = tk.Label(top)
    self.Label1.place(relx=-0.093, rely=0.018, height=71, width=677)
    self.Label1.configure(background="#d9d9d9")
    self.Label1.configure(disabledforeground="#a3a3a3")
    self.Label1.configure(font=font10)
    self.Label1.configure(foreground="#000000")
    self.Label1.configure(text='''Server optionen''')
    self.Label1.configure(width=677)

    self.Button1 = tk.Button(top)
    self.Button1.place(relx=0.322, rely=0.228, height=82, width=198)
    self.Button1.configure(activebackground="#ececec")
    self.Button1.configure(activeforeground="#000000")
    self.Button1.configure(background="#d9d9d9")
    self.Button1.configure(command=servererwalten_support.boot)
    self.Button1.configure(disabledforeground="#a3a3a3")
    self.Button1.configure(foreground="#000000")
    self.Button1.configure(highlightbackground="#d9d9d9")
    self.Button1.configure(highlightcolor="black")
    self.Button1.configure(pady="0")
    self.Button1.configure(relief="groove")
    self.Button1.configure(text='''Starten''')
    self.Button1.configure(width=198)

    self.Button1_1 = tk.Button(top)
    self.Button1_1.place(relx=0.322, rely=0.483, height=82, width=198)
    self.Button1_1.configure(activebackground="#ececec")
    self.Button1_1.configure(activeforeground="#000000")
    self.Button1_1.configure(background="#d9d9d9")
    self.Button1_1.configure(command=servererwalten_support.reboot)
    self.Button1_1.configure(disabledforeground="#a3a3a3")
    self.Button1_1.configure(foreground="#000000")
    self.Button1_1.configure(highlightbackground="#d9d9d9")
    self.Button1_1.configure(highlightcolor="black")
    self.Button1_1.configure(pady="0")
    self.Button1_1.configure(relief="groove")
    self.Button1_1.configure(text='''Neu-starten''')

    self.Button1_2 = tk.Button(top)
    self.Button1_2.place(relx=0.322, rely=0.71, height=82, width=198)
    self.Button1_2.configure(activebackground="#ececec")
    self.Button1_2.configure(activeforeground="#000000")
    self.Button1_2.configure(background="#d9d9d9")
    self.Button1_2.configure(command=servererwalten_support.shutdown)
    self.Button1_2.configure(disabledforeground="#a3a3a3")
    self.Button1_2.configure(foreground="#000000")
    self.Button1_2.configure(highlightbackground="#d9d9d9")
    self.Button1_2.configure(highlightcolor="black")
    self.Button1_2.configure(pady="0")
    self.Button1_2.configure(relief="groove")
    self.Button1_2.configure(text='''Herrunterfahren''')

    self.TSeparator1 = ttk.Separator(top)
    self.TSeparator1.place(relx=-0.068, rely=0.164, relwidth=1.051)

Server()
