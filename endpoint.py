from flask import Flask, request, jsonify
from waitress import serve
from schedule import Monitor, Controller
import json

app = Flask(__name__)
m = Monitor()


@app.route('/calculate', methods=['POST'])
def calculate():
    jsonData = request.json
    uid = jsonData["uid"]
    energy = jsonData["energy"]
    findFlag = False
    res = None
    for loads in m.controllerList:
        if loads.uid == uid:
            findFlag = True
            res = loads
    if findFlag == True:
        json_data = json.dumps(res.schedule(energy))
        return json_data
    else:
        return False


@app.route('/addController', methods=['POST'])
def addController():
    try:
        jsonData = request.json
        loadList = jsonData["Loads"]
        uid = jsonData["uid"]
        c = Controller(l=loadList, uid=uid)
        m.addcontroller(c)
        m.showStatus()
        return jsonify({'success': True, 'message': 'Controller created successfully'})
    except:
        return False

@app.route('/test', methods=['POST'])
def test():
    return "Siuuu"

@app.route('/status', methods=['GET'])
def getStatus():
    res = m.showStatus()
    return res



if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    serve(app, host='0.0.0.0', port=5000)
