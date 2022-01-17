from flask import Flask,redirect,render_template,url_for,request

import utils

app =  Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods = ['POST'])
def prediction():
    if  request.method == 'POST':
        Open = float(request.form.get('Open'))
        High = float(request.form.get('High'))
        Low =  float(request.form.get('Low'))
        Close = float(request.form.get('Close'))
        Adjclose = float(request.form.get('Adjclose'))
        prediction = utils.preprocess(Open,High,Low,Close,Adjclose)

        return render_template('predict.html', value =prediction)
    else:
        return redirect(url_for("home"))

@app.route('/api',methods=['GET'])
def supply():
    return {'json':'Model'}


if __name__ == '__main__':
    app.run(debug=True)