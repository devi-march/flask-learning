from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for employees
employees = [
    {'id': 1, 'name': 'Santhosh'},
    {'id': 2, 'name': 'Krishna Vamsi'},
    {'id': 3, 'name': 'Devi'},
    {'id': 4, 'name': 'Jibu george'}
]

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        new_id = int(request.form['id'])
        new_name = request.form['name']
        employees.append({'id': new_id, 'name': new_name})
        return redirect(url_for('index'))
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)
