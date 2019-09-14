from flask import Flask
import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
  
@app.route('/spreadsheet',methods=['GET','POST'])
def spreadsheet():
  if request.method == 'GET':
    return render_template('speadsheet.html')
  if request.method == "POST":
    # logic here
    return