from flask import Flask, render_template, request, jsonify
from flask_cors import CORS 
from prediction_model import get_results
import os, glob

app = Flask(__name__)
CORS(app, support_credentials=True)

res = os.path.abspath('./static')
if glob.glob1(res, '*.jpg') != []:
   for fil in glob.glob1(res, '*.jpg'):
     print(os.path.join(res, fil))
     os.remove(os.path.join(res, fil))

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.basename('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['fileupload']
	img_name = file.filename
	
	f = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
	file.save(f)

	result = get_results(img_name)

	if result == "uninfected":
		return render_template('NotAffected.html')
	
	return render_template('affected.html', result=result)


if __name__ == "__main__":
	app.run(debug=True)


