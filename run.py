from __future__ import with_statement
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

	with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
		g.say("To speak to a real monkey, press 1. Press any other key to start over. Press 2 to record your own monkey howl. Press any other key to start over.")

	return str(resp)

@app.route("/handle-key", methods=["GET", "POST"])
def handle_key():

	digit_pressed = request.values.get('Digits', None)
	if digit_pressed == '1':
		resp = twilio.twiml.Response()

		resp.dial('+13105551212')

		resp.say('The call failed or the remote party hung up. Goodbye.')

		return str(resp)
	elif digit_pressed == "2":
		resp = twilio.twiml.Response()
		resp.say("Record your monkey howl after the tone.")
		resp.record(maxLength="30", action="/handle-recording")
		return str(resp)
	else:
		return redirect('/')

@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():

	recording_url = request.values.get("RecordingUrl", None)

	resp = twilio.twiml.Response()

	resp.say("Thanks for howling... take a listen to what you howled.")
	resp.play(recording_url)
	resp.say("Goodbye.")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)