from flask import Flask,request,jsonify,render_template,json
import random

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
	if request.method=="POST":
		#print request
		p1=request.form.get('session','')
		print p1
		data=request.get_json()
		print data
		data=request.get_data()
		print data
		#return "1"
		#return jsonify('ok')
		#return "1"
		return jsonify({'modbus': random.randint(1,100)})
		#return Response(data=json.dumps({'ok': True}), mimetype='application/json')
	else:
		return jsonify(['msg','1'])
		return render_template('1.html')

@app.route("/ajax",methods=["GET"])
def ajx():
	return render_template('ajax.html')
if __name__=='__main__':
	app.run(port=7777,host='0.0.0.0',debug=False)