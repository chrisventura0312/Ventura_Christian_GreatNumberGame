from flask import Flask, session, redirect, url_for, request, render_template
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your own secret key

@app.route('/')
def index():
    session['number'] = random.randrange(0, 100)  # generates random number between 0 and 100
    print(session['number'])  # prints the number to the console so you can test it
    session['guess'] = 0  # sets guess to 0
    return render_template('index.html')  # returns template

@app.route('/guess', methods=['POST'])
def guess():
    guess_input = request.form['guess']
    if guess_input:  # check if the input is not empty
        session['guess'] = int(guess_input)  # sets guess to the value of the form
    else:
        session['guess'] = 0  # set guess to 0 if the input is empty

    if session['guess'] == 0:  # check if the guess input is zero
        return render_template('index.html')  # returns template for invalid guess

    if session['guess'] == session['number']:  # checks if they guessed the number
        return render_template('success.html')  # returns template if they win
    elif session['guess'] > session['number']:  # returns template if they guess too high
        return render_template('high.html')
    else:
        return render_template('low.html')  # returns template if they guess too low

@app.route('/reset')
def reset():
    session.clear()  # clear all values in the session
    return redirect(url_for('index'))  # redirects to index

if __name__ == '__main__':
    app.run(debug=True)
