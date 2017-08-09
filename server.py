from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def route_list():
    with open('list.csv', 'r') as listForms:
        reader = csv.reader(listForms)
        readlist = [row for row in reader]
    print(readlist)
    return render_template('list.html', readlist=readlist)


@app.route('/story')
def route_edit():
    note_text = None
    if 'note' in 'list.csv':
        note_text = 'list.csv'['note']
    return render_template('form.html', note=note_text)


@app.route('/save', methods=['POST'])
def route_save():
    Story_title = request.form['Story title']
    User_Story = request.form['User Story']
    Acceptance_criteria = request.form['Acceptance criteria']
    Business_value = request.form['Business value']
    Estimation = request.form['Estimation']
    Status = request.form['Status']
    
    f = open('list.csv', 'a')
    f.write(','.join([Story_title, User_Story, Acceptance_criteria, Business_value, Estimation, Status])+'\n')
    f.close()
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )