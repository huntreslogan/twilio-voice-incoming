from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
	"+14158664966" : "Jessica",
	"+17073383931" : "Donna"
}

@app.route('/', methods=['GET', 'POST'])
def hello_monkey():

	from_number = request.values.get('From', None)

	if from_number in callers:
		caller = callers[from_number]
	else:
		caller = "Monkey"

	resp = twilio.twiml.Response()

	resp.say("Hello " + caller)

	resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)