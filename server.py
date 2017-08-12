from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def route_story():
    update = None
    return render_template('form.html', update=update)


@app.route('/delete/<entry_id>')
def delete_entry(entry_id):
    table = get_table_from_file("list.csv")
    for row in table:
        if row[0] == str(entry_id):
            table.remove(row)
            break
    write_table_to_file("list.csv", table)
    return redirect('/')


@app.route('/story/<entry_id>', methods=['POST', 'GET'])
def edit_story(entry_id):
    entry_id = entry_id
    update = 1
    readlist = get_table_from_file("list.csv")
    for row in readlist:
        if entry_id == row[0]:
            used_list = row
    title = used_list[1]
    story = used_list[2]
    criteria = used_list[3]
    businessvalue = used_list[4]
    estimation = used_list[5]
    status = used_list[6]
    return render_template('form.html', update=update, entry_id=entry_id, title=title, story=story, criteria=criteria,
                           businessvalue=businessvalue, estimation=estimation, status=status)


@app.route('/updating/<entry_id>', methods=['POST'])
def updating(entry_id):
    delete_entry(entry_id)
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    businessvalue = request.form['businessvalue']
    estimation = request.form['estimation']
    status = request.form['status']
    with open('list.csv', 'a') as appender:
        appender.write(','.join([entry_id, title, story, criteria, businessvalue, estimation, status]) + '\n')
    return redirect('/')


@app.route('/')
def route_list():
    with open('list.csv', 'r') as listForms:
        reader = csv.reader(listForms)
        readlist = [row for row in reader]
    return render_template('list.html', readlist=readlist)


@app.route('/save', methods=['POST'])
def route_save():
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    businessvalue = request.form['businessvalue']
    estimation = request.form['estimation']
    status = request.form['status']
    with open('list.csv', 'a') as appender:
        appender.write(','.join([id_generator(), title, story, criteria, businessvalue, estimation, status]) + '\n')
    return redirect('/')


def id_generator():
    table = get_table_from_file("list.csv")
    indices = [int(row[0]) for row in table]
    try:
        return str(max(indices) + 1)
    except BaseException:
        return str(1)


def get_table_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    return table


def write_table_to_file(filename, table):
    with open(filename, "w") as file:
        for record in table:
            row = ','.join(record)
            file.write(row + "\n")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
