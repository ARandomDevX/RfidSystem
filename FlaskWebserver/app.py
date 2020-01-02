
# Importing the required modules

from flask import Flask, render_template, request, jsonify, redirect, session
import json
import mysql.connector
import Hash
from datetime import datetime



# Creating Globals (So i can acces these variables everywhere)

global isLogin

global loginFile

global run

global cur

global mydb

global now

global now2

global Locations

isLogin = {}

loginFile = open('lif.lginfo','w')

run = 0

users = {}

now = datetime.now()

mydb = mysql.connector.connect(
    host='localhost',
    database ="dev",
    user='demouser',
    passwd='demo$#123',
    auth_plugin='mysql_native_password'
)


cur = mydb.cursor(buffered=True)

now2 = datetime.now()

print(now2.strftime("%H:%M:%S"))



cur.execute("SELECT id FROM sonderab WHERE datum = '{}' AND zeit = '{}'".format(now2.strftime("%Y-%m-%d"),now2.strftime("%H:%M:%S")))

PreKidsVar = cur.fetchall()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

now2 = datetime.now()

Locations = {"0001":"Hof","0002":"Garten"}

# Creating the Flask object

app = Flask(__name__)


# Listening For connections on the Main directory

@app.route("/",methods=['GET'])

def main():

    # Rendering the Login

    return render_template('Login.html')
@app.route("/",methods=['POST'])
def Login():

    now2 = datetime.now()

    cur.execute("SELECT id FROM sonderab WHERE datum = '{}' AND zeit = '{}'".format(now2.strftime("%Y-%m-%d"),current_time))

    PreKidsVar = cur.fetchall()

    uname = request.form['uname']

    passw = request.form['pass']
    passw = Hash.hashPassword(passw)

    passw = passw.decode("utf-8")

    print(passw)

    cur.execute('SELECT uname, password FROM users')

    details = cur.fetchall()

    details = list(details)

    if (uname,(passw)) in details:
        global isLogin

        isLogin = True

        return render_template('index.html',names=PreKidsVar,Names=["Hallo, " + uname])
    else:
        return render_template('Fail.html')



@app.route("/index",methods=['GET','POST'])

def maain():

    if isLogin == True:
    # Rendering the index file

        now2 = datetime.now()

        cur.execute("SELECT id FROM sonderab WHERE datum = '{}' AND zeit= '{}'".format(now2.strftime("%Y-%m-%d"),current_time))

        PreKidsVar = cur.fetchall()

        return render_template('index.html',names=PreKidsVar)
    else:

        return render_template('noLogin.html')

# Listening For connections on the /procces directory (Only for test)

@app.route("/procces",methods=['POST'])
def sendJson():

    # Letting the Code to recive the JSON code

    data = request.get_json()


    # Returning the daba value

    return jsonify({'value':'succes'})

@app.route('/rpisst')
def ListenAndFunction():

    Data = request.json()

    Id = Data.keys()

    Ort = Data.values()

    cur.execute("INSERT INTO ort VALUES({},{})".format(Id,Ort))

@app.route("/getNames",methods=['GET'])
def GetNames():

    return jsonify({'resault':'succes'})
@app.route("/anmelden", methods=['POST'])
def Anmelden():

    data = request.get_data().decode()

    card, status = data.split('&')

    Misc, Number = card.split('=')

    Misc, Location = status.split("=")

    print('Rfid Code : ' + Number)

    print('Current Location : ' + Location)

    return data

@app.route('/abmelden',methods=['POST'])
def Abmelden():

    data = request.get_json()

    return jsonify({'No':'ErrorsAccoured'})


@app.route("/bin/server.get",methods=['POST'])
def get_cuurent_send_Json():

    data = request.get_json()

    return jsonify(data)


@app.route('/bin',methods=['GET'])
def return_bins():
    return jsonify({''})




@app.route("/raspberrypi/test/gui",methods=['GET'])
def test_Gui_Raspberrypi():

    return render_template('Raspberrypitest.html')


@app.route("/raspberrypi",methods=['POST'])
def raspberrypi_json_test():

    data = request.get_json()



    return jsonify({'JSON':'TEST.rpi'})


@app.route("/test")
def test():

    return "<h1>TEST test </h1>"


@app.route("/sst",methods=['POST'])
def sst():
    data = request.get_data().decode()

    card, status = data.split('&')

    Misc, Number = card.split('=')

    Misc, Status = status.split("=")

    Status,misc = Status.split("%")

    print(f"Debug.Log(Number : {Number}, Status : {Status})")

    return data


@app.route("/del/<string:name>", methods=['DELETE'])
def delete(name):

    print(f'Deleted: {name} and is a Rfid number')

    return jsonify({'...':'...'})

@app.route("/closeServer",methods=['GET'])
def clsServer():

    import os

    os.system('sudo git pull')

    os.system("sudo su")

    cur.execute("TRUNCATE TABLE sonderab")

    os.system("mysqldump -uroot --databases dev > devx.sql")

    os.system('sudo shutdown -h now')

@app.route("/notfall",methods=['GET'])
def notfall():

    data=request.get_data().decode()

    id = data

    misc, Use = data.split('=')

    print(id)

    print('Identifier = ' + Use)

    return jsonify({'test':'123'})

# Getting data from raspberrypis

@app.route('/Data',methods=['POST'])
def Data():

    data = request.get_data()

    print(data)

    data = data.decode()

    Rfid, Status = data.split("&")

    Status, Misc = Status.split('%')

    del Misc

    print(Rfid)
    print(Status)

    return jsonify({'ok':'ok'})

@app.route('/Form')
def maion():
    if isLogin == True:
        return render_template("Online_Reg.html")
    else:

        return render_template('noLogin.html')

@app.route('/Form',methods=['POST'])
def GetValue():
    if isLogin == True:
        name = request.form['firstname']
        lname = request.form['lastname']
        id = request.form['id']
        mon = request.form['Montag']
        die = request.form['Dienstag']
        mit= request.form['Mitwoch']
        don = request.form['Donnerstag']
        fri = request.form['Freitag']
        Eltern1 = request.form['Erw1']
        Eltern2 = request.form['Erw2']

        print(name, lname, id, mon, die)
        # Logic

        cur.execute("INSERT INTO schuler VALUES('{}','{}','{}','{}','{}')".format(name, lname, id, Eltern1, Eltern2))
        cur.execute("INSERT INTO heim VALUES('{}','{}','{}','{}','{}','{}')".format(mon,die,mit,don,fri,id))
        mydb.commit()
        return render_template('procces_done.html')
    else:

        return render_template('noLogin.html')



@app.route('/Del')
def Delete():
    if isLogin == True:
        return render_template("Del.html")
    else:

        return render_template('noLogin.html')

@app.route("/Del",methods=['POST'])
def Deleite():
    if isLogin == True:
        id = request.form['id']

        cur.execute("DELETE FROM schuler, heim WHERE id = '{}".format(id))

        return render_template('Done.html')
    else:

        return render_template('noLogin.html')

@app.route("/ea",methods = ["GET"])
def ea():

    return render_template("Te.html")
@app.route("/ea",methods=['POST',"GET","HEAD","PUT","DELETE"])
def eas():
        if isLogin == True:
            name = request.form['name']
            lname = request.form['lname']
            email = request.form['email']
            uname = request.form['uname']
            password = request.form['pass']
            password = Hash.hashPassword(password)

            password = password.decode("utf-8")

            cur.execute('SELECT id FROM users')

            curid = cur.fetchall()



            lenid = len(curid)

            index = lenid + 1

            print(index)


            cur.execute("INSERT INTO details(id,email,password,name,lname) VALUES('{}','{}','{}','{}','{}')".format(index,email,password,name,lname))

            cur.execute("INSERT INTO users(id,uname,password) VALUES('{}','{}','{}')".format(index,uname,password))

            mydb.commit()

            import smtplib
            import ssl
            from random import random

            smtp_server = "smtp.gmail.com"
            port = 587  # For starttls
            sender_email = "resetbot46@gmail.com"
            password = "Resetbot2019"

            number = random()
            Misc, Use = str(number).split("0.")

            message = """\
            Subject: Angemeldet!

            Bitte Keine Antwort Senden

            Hallo, Sie haben sich hier angemeldet, sie koennen sich mit den angegebenen loggin daten anmelden!

            Falls es dazu kommt das sie ihr passwort vergessen haben dann koennen sie einfach ihr passwort wiederherstellen(Unfunktionell ist gerade noch am entwikeln)

            Danke!


            (Falls sie sich nicht angemeldet haben dann ignorieren sie diese nachricht)"""

            # Create a secure SSL context
            context = ssl.create_default_context()

            # Try to log in to server and send email
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)

            server.sendmail(sender_email, email, message)

            server.quit()

            return render_template('Done2.html')

        else:

            return render_template('noLogin.html')
@app.route("/an")
def an():



    return render_template('noLogin.html')
@app.route("/an", methods=['POST'])
def ani():

    if isLogin == True:

        id = request.form['id']

        print(id)

        return render_template('Done3.html')
    else:
        return render_template('noLogin.html')
@app.route('/ab')
def ad_def():

    return render_template('Abmelden.html')
@app.route("/ab", methods=['POST'])
def ania():

    if isLogin == True:

        id = request.form['id']

        print(id)

        return render_template('Done4.html')
    else:
        return render_template('noLogin.html')

@app.route('/Sst')
def RunAction():

    if isLogin == True:

        return render_template('sst.html')
@app.route('/Sst')
def Actions():

    if isLogin == True:

        Status = request.form['Status']
        Id = request.form['id']

@app.route('/sonder')
def Render():

    if isLogin == True:

        return render_template('Sonderabholzeiten.html')
    else:
        return render_template('noLogin.html')
@app.route('/sonder',methods=['POST'])
def Working():
    min = request.form['min']
    stunden = request.form['ho']
    sekun = request.form['sek']
    id = request.form['id']
    date = request.form['date']

    time = stunden + ':' + min + ':' + sekun


    cur.execute("INSERT INTO sonderab VALUES('{}','{}','{}')".format(id,time,date))
    mydb.commit()

    return render_template("ReturnSonder.html")

@app.route("/isloginfalse")
def SD():

    isLogin = False

    return redirect("/")

@app.route("/schuleruber")
def Graphics():



    if isLogin == True:

        now2 = datetime.now()

        item_list = None

        Outputofcur = [()]

        cur.execute("SELECT id FROM sonderab WHERE datum = '{}' AND zeit = '{}'".format(now2.strftime("%Y-%m-%d"),current_time))

        Headings = ["Montag","Dienstag","Mitwoch","Donnerstag","Freitag","Samstag","Sonntag","Karten Nummer"]

        HomeTime = cur.fetchall()

        now3 = datetime.now()

        cur.execute("SELECT * from heim")

        Current_Weekday = now2.strftime("%A")

        Outputofcur = cur.fetchall()

        print(Outputofcur)
        for item in Outputofcur:
            print(item)

        cur.execute("SELECT * FROM ort")

        objjjj = cur.fetchall()

        hds = ["Karten nummer","ort"]




        if int(len(Outputofcur)) != 0:
            return render_template("schulerubersicht.html",columns=Headings,items=Outputofcur,ds=hds,obj=objjjj)
        else:
            return render_template("schulerubersicht.html",columns=Headings,items=[('Nichts','Leer'),('Wiedernichts','SehrLeer')])
    else:
        return render_template("noLogin.html")
@app.route("/getSgData")
def Rnder():

    return render_template("sgData.html")
@app.route("/getSgData",methods=["POST"])
def Escript():

    Id = request.form["Idc"]

    return redirect("/gsgd/" + Id)
@app.route("/gsgd/<card>",methods=["POST","GET"])
def Escripft(card):

    cur.execute("SELECT * FROM heim WHERE id = {}".format(card))

    Out = cur.fetchall()

    Headings = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag",'Karten Nummer']

    Xyz = []

    for row in Out:

        for x in row:

            Xyz.append(row[x])

    cur.execute("SELECT * FROM schuler WHERE id = {}".format(Xyz[8]))

    eight = cur.fetchall()

    nine = []

    for rowx in eight:

        for y in rowx:

            nine.append(rowx[y])

    Xyz[8] = nine[0]

    return render_template("Display.html",ds=Headings,obj=Xyz)



@app.route("/reset")
def Screen():

    return render_template("Passwordreset.html")

@app.route("/reset",methods=["POST"])
def SendEmail():

    import smtplib

    email = request.form["email"]

    import smtplib
    import ssl
    from random import random


    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "resetbot46@gmail.com"
    password = "Resetbot2019"

    number = random()
    Misc, Use = str(number).split("0.")

    message = """\
Subject: Passwort Wiederherstellen

Bitte Keine Antwort Senden

Hallo, Ihr passwort wiederherstellungscode lautet : """



    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)

        server.sendmail(sender_email, email, message + Use)

        cur.execute("INSERT INTO passwordreset VALUES({},{})".format(email,Use))

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
        return redirect("/reset2/" + email + "/" + Use)


@app.route("/reset2/<mail>/<code>")
def Graph(mail,code):

    return render_template("Passowerdreste2.html")
@app.route("/reset2/<mail>/<code>",methods=["POST"])
def Core(mail,code):

    try:
        code = request.form["code"]

        cur.execute("SELECT email from details WHERE email = {}".format(mail))

        cur.execute("SELECT code FROM passwordreset WHERE code = {}".format(code))

        return redirect("/reset3/" + code + "/" + mail)

    except Exception as e:

        print(e)


@app.route("/reset3/<code>/<email>")
def Screend(code,email):

    return render_template("NewPassword.html")
@app.route("/reset3/<code>/<email>",methods = ["POST"])
def BAckend(code):

    password = request.form["password"]
    username = request.form["uname"]

    cur.execute("UPDATE users(uname,password) VALUES({},{}) WHERE uname={}".format(username,Hash.hashPassword(password),username))

@app.route("/update")
def Update():

    import os

    os.system("sudo git pull")

    return redirect("/index")

@app.route("/names")
def Gnms():

    return render_template('nameso.html')
@app.route("/names",methods =['POST'])
def Gnmts():

    id = request.form['id']



    return redirect('/nms/' + id)

@app.route("/assignLocation/<id>")
def Dosoemthing(id):

    return Locations[id]
@app.route('/nms/<id>')
def edf(id):

    if isLogin == True:

        cur.execute('SELECT name FROM schuler WHERE id = {}'.format(id))

        out = cur.fetchall()

        hd = ['Karten Nummer','Name']

        return render_template('namest.html',ds = hd, obj = out, id = id)

    else :

        return render_template('noLogin.html')

@app.route("/Raspireffer")
def RaspiGraphic():

    return render_template("ChooseRaspilocation.html")


@app.route("/Raspireffer",methods=["POST"])
def RaspeiGraphic():

    ooo1 = request.form["0001"]

    ooo2 = request.form["0002"]

    Locations["0001"] = ooo1

    Locations["0002"] = ooo2

    return render_template("Done5.html")


#End/Startup options

import atexit

def clqs():

    cur.execute("TRUNCATE TABLE sonderab")
    mydb.commit()
    mydb.close()

    exit()

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)


if __name__ == '__main__':

    try:
        app.run(debug=True,host='0.0.0.0',port=80)
    except OSError:
        import os

        os.system('sudo service nginx stop')

        app.run(debug=True, host='0.0.0.0',port=80)
