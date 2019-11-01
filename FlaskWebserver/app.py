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

isLogin = None

loginFile = open('lif.lginfo','w')

run = 0

users = {}

now = datetime.now()

mydb = mysql.connector.connect(
    host='localhost',
    database ="dev",
    user='developer',
    passwd='Waldschule',
    auth_plugin='mysql_native_password'
)



cur = mydb.cursor()

cur.execute('SELECT * FROM sonderab')

PreKidsVar = cur.fetchall()

Time = {i[0]:i[1] for i in PreKidsVar}

Time = str(Time.keys()).join("/")

Date = {i[0]:i[2] for i in PreKidsVar}

print(str(Date) + "and" + str(Time))

kids = []

for item in Time:

    print(item)



Length = len(PreKidsVar)

print(PreKidsVar)

list(PreKidsVar)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Creating the Flask object

app = Flask(__name__)

# Listening For connections on the Main directory

@app.route("/",methods=['GET'])

def main():

    # Rendering the Login

    return render_template('Login.html')
@app.route("/",methods=['POST'])
def Login():

    uname = request.form['uname']
    print(uname)
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

        return render_template('index.html',time=current_time,names=kids)
    else:
        return render_template('Fail.html')



@app.route("/index",methods=['GET','POST'])

def maain():

    if isLogin != False:
    # Rendering the index file

        return render_template('index.html',names=kids)
    else:

        return render_template('noLogin.html')

# Listening For connections on the /procces directory (Only for test)

@app.route("/procces",methods=['POST'])
def sendJson():

    # Letting the Code to recive the JSON code

    data = request.get_json()


    # Returning the daba value

    return jsonify({'value':'succes'})

# Listening For connections on the /getNames directory


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


@app.route("/raspberrypi",methods=['GET'])
def raspberrypi_json_test():

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

    os.system('sudo shutdown now')

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
        cur.execute("INSERT INTO heim VALUES('{}','{}',{}','{}','{}','{}')".format(id,mon,die,mit,don,fri))
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

        print(id)

        return render_template('Done.html')
    else:

        return render_template('noLogin.html')

@app.route("/ea")
def ea():

    return render_template("Te.html")
@app.route("/ea",methods=['POST'])
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


@app.route("/schuleruber")
def Graphics():

    if isLogin == True:

        return render_template("schuleruber.html")
    else:
        return render_template("noLogin.html")
#End/Startup options

import atexit

def clqs():

    mydb.commit()
    mydb.close()

atexit.register(clqs)

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)


if __name__ == '__main__':

    try:
        app.run(debug=True,host='0.0.0.0',port=80)
    except OSError:
        import os

        os.system('sudo service apache2 stop')

        app.run(debug=True, host='0.0.0.0',port=80)
