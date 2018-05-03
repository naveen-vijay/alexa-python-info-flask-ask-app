from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


@app.route('/')
def index():
    pass

@ask.launch
def launch():
    pass


@ask.intent('GetPythonHistory')
def get_pep_info():
    pass


@ask.intent('GetPEPInfo', mapping={'index': 'index'})
def get_pep_info(index):
    pass


@ask.intent('GetPythonReleaseInfo')
def get_pep_info():
    pass


@ask.intent('AMAZON.HelpIntent')
def cancel():
    pass


@ask.intent('AMAZON.StopIntent')
def stop():
    pass


@ask.intent('AMAZON.CancelIntent')
def cancel():
    pass


if __name__ == '__main__':
    app.run(debug=True)
