import shutil
import zipfile
from flask import Flask, request, jsonify
from multiprocessing import Process
import os, signal

saveLocation = ""
app = Flask(__name__)

@app.route('/stopServer', methods=['GET'])
#kill the server and program
def stopServer():
    #find pid and kill
    os.kill(os.getpid(), signal.SIGINT)
    #dont know if this is needed rly
    return jsonify({ "success": True, "message": "Server is shutting down..." })
    
@app.route('/', methods=['POST'])
def index():
    #might be some better way to do this but i dont want to figure out flask stuff rn
    for field, data in request.files.items():
        #make up to two backups
        if data.filename:
            if os.path.exists(saveLocation+"-back1") and os.path.exists(saveLocation+"-back2"):
                shutil.rmtree(saveLocation+"-back2")
                shutil.copytree(saveLocation+"-back1", saveLocation+"-back2")
                shutil.rmtree(saveLocation+"-back1")
                shutil.copytree(saveLocation, saveLocation+"-back1")
                shutil.rmtree(saveLocation)
            elif os.path.exists(saveLocation+"-back1"):
                shutil.copytree(saveLocation+"-back1", saveLocation+"-back2")
                shutil.rmtree(saveLocation+"-back1")
                shutil.copytree(saveLocation, saveLocation+"-back1")
                shutil.rmtree(saveLocation)
            else:
                shutil.copytree(saveLocation, saveLocation+"-back1")
                shutil.rmtree(saveLocation)
            #save uploaded file
            data.save(os.path.join(data.filename))
            os.mkdir(saveLocation)
            #unzip it to chosen place
            with zipfile.ZipFile(data.filename, 'r') as zip_ref:
                zip_ref.extractall(saveLocation)
            #delete the zip
            os.remove(data.filename)
            return "OK"

def run(port, saveLocationx):
    global saveLocation 
    saveLocation = saveLocationx
    app.run(port=port)