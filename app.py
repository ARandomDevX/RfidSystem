from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def main():

    return render_template('index.html')

@app.route("/procces",methods=['POST'])
def sendJson():

    data = request.get_json()


    return jsonify({'value':'succes'})
    
@app.route("/getNames",methods=['GET'])
def GetNames():

    return jsonify({'resault':'succes'})
@app.route("/anmelden", methods=['POST'])
def Anmelden():

    data = request.get_json()

    return jsonify({'return':'succes'})
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

@app.route('/nsa',methods=['POST'])
def nsa_nsa():

    data = request.get_json()

    return data
@app.route("/raspberrypi/test/gui",methods=['GET'])
def test_Gui_Raspberrypi():

    return render_template('Raspberrypitest.html')
@app.route("/raspberrypi",methods=['GET'])
def raspberrypi_json_test():

    return jsonify({'JSON':'TEST.rpi'})

@app.route("/test")
def test():

    return "<h1>TEST test </h1>"

# End

if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=80)

