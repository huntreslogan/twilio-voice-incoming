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
	resp = twilio.twiml.Response()
	if from_number in callers:
		resp.say("Hello " + callers[from_number])
	else:
		resp.say("Hello Monkey")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)