from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def route_list():
    with open('list.csv', 'r') as listForms:
        reader = csv.reader(listForms)
        readlist = [row for row in reader]
    print(reader)
    print(readlist)
    return render_template('list.html', readlist=readlist)


@app.route('/story')
def route_edit():
    return render_template('form.html')


@app.route('/story/<entry_id>')
def edit_story(entry_id):
    with open('list.csv', 'r') as d:
        for row in x:
            if entry_id == row[0]:
                value = row[0]
    return render_template('form.html', value=value, entry_id=entry_id)


@app.route('/save', methods=['POST'])
def route_save():
    Story_title = request.form['Story title']
    User_Story = request.form['User Story']
    Acceptance_criteria = request.form['Acceptance criteria']
    Business_value = request.form['Business value']
    Estimation = request.form['Estimation']
    Status = request.form['Status']
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        readlist = [row for row in reader]
    x = int(readlist[-1][0])
    with open('list.csv', 'a') as f:
        x += 1
        f.write(','.join([str(x), Story_title, User_Story, Acceptance_criteria, Business_value, Estimation, Status])+'\n')
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )