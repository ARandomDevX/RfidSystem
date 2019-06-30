# coding=utf-8
from tkinter import *
from Personalanmelden import Toplevel1
import os
# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Registrieren")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Bitte daten unten eingeben").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Beutzername * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Passwort * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    storefile = open("{}.key","a".format(username))
    storefile.append("{}".format(username))
    storefile.append("{}".format(password))
    from sql import cur
    from crypt import 
    cur.execute("INSERT INTO rbs VALUES({},{})")
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Fertig", width=10, height=1,command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Einloggen")
    login_screen.geometry("300x250")
    Label(login_screen, text="Bitte geben sie die daten unten an").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Name ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Passwort ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Fertig", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 == "Admin" and password1 == "RootAdministrator":
        print("Helllotak9ismy9")

    else:
        import crypt
        crypt.encrypt(password1,username1)
        if res == True :
            login_sucess()
        if res == False:
            import crypt
            crypt.decrypt(password1, username1)
            from tkinter import messagebox
            messagebox.showerror(decrypted)
# Designing popup for login success

def login_sucess():
        import Hauptmenü
        Hauptmenü.Toplevel1()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Ok")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Passwort nicht erkannt ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Ok")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Bentutzer nicht gefunden").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Einloggen")
    Label(text="Suchen sie was aus",width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Einloggen", height="2", width="30", command=login).pack()
    Button(text="Registrieren", height="2", width="30", command=register).pack()

    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()