import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/input', methods=['GET','post'])
def hello():
    return render_template("input.html")

@app.route('/output', methods=['GET','post'])
def predict():
	
	GRE_Score = int(request.form['GRE Score'])
	TOEFL_Score = int(request.form['TOEFL Score'])
	University_Rating = int(request.form['University Rating'])
	SOP = float(request.form['SOP'])
	LOR = float(request.form['LOR'])
	CGPA = float(request.form['CGPA'])
	Research = int(request.form['Research'])
	
	final_features = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])
	
	predict = model.predict(final_features)
	
	output = predict[0]*100
	
	if(output>60):
		return render_template('output.html', Admission_Prediction='Admission chances are High {}'.format(output))
	elif(output<40):
		return render_template('output.html', Admission_Prediction='Admission chances are Low {}'.format(output))
	else:
		return render_template('output.html', Admission_Prediction='Admission chances are Moderate {}'.format(output))
	
if __name__ == "__main__":
	app.run(debug=True)