from flask import Flask, request, jsonify, render_template
from flask_cors import CORS , cross_origin
import pickle
import os
import numpy

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)
@app.route('/',methods=['GET'])
@cross_origin()
def Homepage():
    return render_template('index.html')
@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method =='POST':
        try:
            is_gender=request.form['gender']
            if (is_gender=='male'):gender=1
            else : gender=0
            age=int(request.form['age'])
            education=float(request.form['education'])
            is_chain_smoker=request.form['chain_smoker']
            if (is_chain_smoker=="yes"):chain_smoker=1
            else : chain_smoker=0
            cigsPerDay=float(request.form['cigsPerDay'])
            is_BPMeds=request.form['BPMeds']
            if (is_BPMeds=='yes'):BPMeds=1.0
            else: BPMeds=0.0
            is_prevalentStroke=request.form['prevalentStroke']
            if (is_prevalentStroke=='yes'):prevalentStroke=1
            else: prevalentStroke=0
            is_prevalentHyp=request.form['prevalentHyp']
            if (is_prevalentHyp=='yes'): prevalentHyp=1.0
            else: prevalentHyp=0.0
            is_diabetes=request.form['diabetes']
            if (is_diabetes=='yes'):diabetes=1
            else: diabetes=0
            totChol=float(request.form['totChol'])
            sysBP=float(request.form['sysBP'])
            diaBP=float(request.form['diaBP'])
            BMI=float(request.form['BMI'])
            heartRate=float(request.form['heartRate'])
            glucose=float(request.form['glucose'])
            print(gender,age,education,chain_smoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol ,sysBP,diaBP,BMI,heartRate,glucose)
            filename="finalized_model1.pickle"
            loaded_model=pickle.load(open(filename,'rb'))
            prediction=loaded_model.predict([[gender,age,education,chain_smoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol ,sysBP,diaBP,BMI,heartRate,glucose]])
            print("prediction is",prediction[0])
            if prediction[0]==1:
                res="You might suffer from Heart Attack."
            else :
                res="Hey! GOOD NEWS . You will not suffer from Heart Attack"
            return render_template('results.html',prediction=res)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('index.html')

port = os.getenv("PORT")
if __name__ == '__main__':
	if port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(port), debug=True)




