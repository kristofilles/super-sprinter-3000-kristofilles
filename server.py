from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def route_list():
    with open('list.csv', 'r') as listForms:
        reader = csv.reader(listForms)
        readlist = [row for row in reader]
    return render_template('list.html', readlist=readlist)


@app.route('/story')
def route_story():
    update = None
    return render_template('form.html', update=update)


@app.route('/story/<entry_id>', methods=['POST', 'GET'])
def edit_story(entry_id):
    if request.method == 'POST':
        with open('list.csv', 'r') as d:
            for row in d:
                if entry_id == row[0]:
                    value = row[0]
        return render_template('form.html', value=value, entry_id=entry_id)
    else:
        update = 1
        with open('list.csv', 'r') as listForm:
            readlist = list(list(row) for row in csv.reader(listForm, delimiter=','))
        print(readlist)
        Story_title = readlist[int(entry_id)-1][1]
        User_story = readlist[int(entry_id)-1][2]
        Acceptance = readlist[int(entry_id)-1][3]
        Business = readlist[int(entry_id)-1][4]
        Estimation = readlist[int(entry_id)-1][5]
        Status = readlist[int(entry_id)-1][6]
        return render_template('form.html', update=update, Story_title=Story_title, User_story=User_story, Acceptance=Acceptance, Business=Business, Estimation=Estimation, Status=Status)
            

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
    if readlist == []:
        x = 1
    else:
        x = int(readlist[-1][0])
        x += 1
    with open('list.csv', 'a') as f:
        f.write(','.join([str(x), Story_title, User_Story, Acceptance_criteria, Business_value, Estimation, Status])+'\n')
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )