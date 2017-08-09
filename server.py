from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def route_list():
    note_text = None
    if 'note' in 'list.csv':
        note_text = 'list.csv'['note']
    return render_template('list.html', note=note_text)


@app.route('/story')
def route_edit():
    note_text = None
    if 'note' in 'list.csv':
        note_text = 'list.csv'['note']
    return render_template('form.html', note=note_text)


@app.route('/save-note', methods=['POST'])
def route_save():
    print('POST request received!')
    'list.csv'['note'] = request.form['note']
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )