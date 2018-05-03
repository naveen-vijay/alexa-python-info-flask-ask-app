from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


@app.route('/')
def index():
    return "DFW Python Meetup"

@ask.launch
def launch():
    print('Launch')        
    return statement('Opening Python Info - Alexa Voice Skill')


@ask.intent('GetPythonHistory')
def get_pep_info():
    print('GetPEPInfo')    
    return statement('Get Python History')


@ask.intent('GetPEPInfo', mapping={'index': 'index'})
def get_pep_info(index):
    print('GetPEPInfo')    
    return statement(f'Get PEP Info - {index}')


@ask.intent('GetPythonReleaseInfo')
def get_pep_info():
    print('GetPythonReleaseInfo')
    return statement('Python Release')


@ask.intent('AMAZON.HelpIntent')
def cancel():
    print('AMAZON.HelpIntent')
    return statement('Help Intent')


@ask.intent('AMAZON.StopIntent')
def stop():
    print('AMAZON.StopIntent')
    return statement('Stop Intent')


@ask.intent('AMAZON.CancelIntent')
def cancel():
    print('AMAZON.CancelIntent')
    return statement('Cancel Intent')


if __name__ == '__main__':
    app.run(debug=True)
