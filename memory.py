## Nicholas Capsimalis, CS20, 10/19/2018
import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key='abcdefg';

@app.route('/')
def renderMain():
    session['hideReset']=True
    session['warning']=False
    session["score"]=0
    return render_template('main.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('renderMain'))

@app.route('/about')
def renderAbout():
    return render_template('about.html')

@app.route('/question1')
def render_question1():
    session['warning']=False
    return render_template('question1.html')

@app.route('/question2', methods=['GET', 'POST'])
def render_question2():
    try:
        session['warning']=False
        session['answer1']=int(request.form['answer1'])
        if float(session['answer1'])==2:
            session["score"]=session["score"]+1
        session['hideReset']=False
        return render_template('question2.html')
    except ValueError:
        session['warning']=True
        return render_template('question1.html')

@app.route('/question3', methods=['GET', 'POST'])
def render_question3():
    try:
        session['warning']=False
        session['answer2']=int(request.form['answer2'])
        if float(session['answer2'])==9:
            session["score"]=session["score"]+1
        return render_template('question3.html')
    except ValueError:
        session['warning']=True
        return render_template('question2.html')

@app.route('/question4', methods=['GET', 'POST'])
def render_question4():
    try:
        session['warning']=False
        session['answer3']=int(request.form['answer3'])
        if float(request.form['answer3'])==120:
            session["score"]=session["score"]+1
        return render_template('question4.html')
    except ValueError:
        session['warning']=True
        return render_template('question3.html')

@app.route('/trickquestion', methods=['GET', 'POST'])
def render_trickquestion():
    try:
        session['warning']=False
        session['answer4']=int(request.form['answer4'])
        if float(request.form['answer4'])==112:
            session["score"]=session["score"]+1
        return render_template('trickquestion.html')
    except ValueError:
        session['warning']=True
        return render_template('question4.html')

@app.route('/scorecard', methods=['GET', 'POST'])
def render_scorecard():
    try:
        session['warning']=False
        session['trickAnswer']=int(request.form['trickAnswer'])
        if float(request.form['trickAnswer'])==float(session['answer1']):
            session["score"]=session["score"]+1
        return render_template('scorecard.html')
    except ValueError:
        session['warning']=True
        return render_template('trickquestion.html')
                                            
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
