from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for employees
employees = [
    {'id': 1, 'name': 'Santhosh'},
    {'id': 2, 'name': 'Krishna'},
    {'id': 3, 'name': 'Devi'},
    {'id': 3, 'name': 'Jibu George'},
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

@app.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    if request.method == 'POST':
        if employee:
            employee['name'] = request.form['name']
        return redirect(url_for('index'))
    return render_template('edit_employee.html', employee=employee)

if __name__ == '__main__':
    app.run(debug=True)
