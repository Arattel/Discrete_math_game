import  random
import copy
from flask import Flask, render_template, request
from webbrowser import open_new_tab

app = Flask(__name__)
questions = ['A', 'B', 'C', "D", "E", 'F']
ans = ['1', '2', '3', '4', '5', '6']
right = 0
numofq = 0
numr = 0
disabled = ''

@app.route("/", methods = ['GET','POST'])
def question():
    global questions, right, disabled
    if disabled == 'disabled':
        choice = "Питання закінчились("
    else:
        choice = random.choice(questions)
        right = questions.index(choice)
    return  render_template("hello.html", question = choice, disabled = disabled)
@app.route("/login", methods = ['GET','POST'])
def login():
    global ans, right, numofq, numr, disabled
    answer = request.form['answer']
    a = ''
    g = ''
    col = ''
    if answer == ans[right]:
        a = "Відповідь  " + str(answer) + " правильна"
        g = ''
        col = "green"
        numr += 1
    else:
        a = "Відповідь  " + str(answer) + " неправильна"
        g = 'Правильна відповідь: ' + ans[right]
        col = "red"
    numofq += 1
    temp1  = copy.deepcopy(questions[right])
    questions.pop(right)
    ans.pop(right)
    if len(questions) == 0:
        disabled = 'disabled'
    return render_template("right.html", response=a, question = temp1, color = col, good = g)
@app.route('/results', methods = ['GET','POST'])
def results_of_test():
    global numr, numofq
    percent = round((numr / numofq), 2) * 100
    replic = ''
    if numr // numofq == 1 and numofq >= 25:
        replic = 'Та ти ж пророк Щербини'
    elif percent < 60:
        replic = 'Талон)'
    return render_template('results.html', numof = numofq, percentr = str(percent) + '%', scherbyna = replic)
if __name__ == "__main__":
    open_new_tab('http://localhost:8000')
    app.run(port=8000)
