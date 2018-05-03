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
    return question(render_template('welcome')).reprompt(render_template('welcome_reprompt')).simple_card('Python Info - Launch', render_template('welcome'))


@ask.intent('GetPythonHistory')
def get_python_history():
    return statement(render_template('history')).simple_card('Get Python History', render_template('history'))


@ask.intent('GetPythonReleaseInfo')
def get_python_release():
    return statement(render_template('next_python_release')).simple_card('Get Python Release Info', render_template('history'))


@ask.intent('GetPEPInfo', mapping={'index': 'index'})
def get_pep_info(index):
    if not index:
        question_text = 'What is PEP index number ?'
        return question(question_text).simple_card('Get PEP Info', question_text)
    pep_text = PEP_INDEX.get(index, 'invalid')
    pep_info = f'PEP {index} is {pep_text}'
    return statement(pep_info).simple_card(f'Get PEP Info - PEP {index}', pep_info)


@ask.intent('AMAZON.HelpIntent')
def cancel():
    print('AMAZON.HelpIntent')
    return statement(render_template('welcome')).simple_card('Python Info - Launch', render_template('welcome'))


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
