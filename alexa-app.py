from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

from PEP_INDEX import PEP_INDEX

app = Flask(__name__)
ask = Ask(app, "/")


@app.route('/')
def index():
    return "DFW Python Meetup"


@ask.launch
def launch():
    return statement(render_template('welcome'))


@ask.intent('GetPythonHistory')
def get_python_history():
    return statement(render_template('history'))


@ask.intent('GetPythonReleaseInfo')
def get_python_release():
    return statement(render_template('next_python_release'))


@ask.intent('GetPEPInfo', mapping={'index': 'index'})
def get_pep_info(index):
    if not index:
        return question('What is PEP index number ?')
    pep_text = PEP_INDEX.get(index, 'invalid')
    return statement(f'PEP {index} is {pep_text}')


@ask.intent('AMAZON.HelpIntent')
def cancel():
    print('AMAZON.HelpIntent')
    return statement(render_template('welcome'))


@ask.intent('AMAZON.StopIntent')
def stop():
    print('AMAZON.StopIntent')
    return statement('Okay, thank you for using Python Info Skill')


@ask.intent('AMAZON.CancelIntent')
def cancel():
    print('AMAZON.CancelIntent')
    return statement('Allright')


if __name__ == '__main__':
    app.run(debug=True)
