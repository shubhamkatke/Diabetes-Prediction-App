from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
@app.route("/")
def home():
	return render_template("home.html")
@app.route("/prediction")
def pred():
	try:
		if request.args.get("preg") and request.args.get("glu") and request.args.get("bp") and request.args.get("st") and request.args.get("ins") and request.args.get("bmi") and request.args.get("dpf") and request.args.get("age"):
			p = int(request.args.get("preg"))
			g = float(request.args.get("glu"))
			bp = int(request.args.get("bp"))
			st = float(request.args.get("st"))
			ins = int(request.args.get("ins"))
			bmi = float(request.args.get("bmi"))
			dpf = float(request.args.get("dpf"))
			a = int(request.args.get("age"))
			with open("dia.model","rb") as f:
				model = pickle.load(f)
			res = model.predict([[p,g,bp,st,ins,bmi,dpf,a]])
			msg = res[0]
			if msg==1:
				text = "You have diabetes."
			else:
				text = "You dont have diabetes. Stay Safe!"
			return render_template("prediction.html",msg=text)
		else:
			return render_template("prediction.html")
	except Exception as e:
		return render_template("prediction.html",msg=e)
@app.route("/help")
def help():
	return render_template("help.html")
if __name__=="__main__":
	app.run(debug = True, use_reloader = True)