from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (replace with your actual data handling logic)
employees = [
    {"emp_id": 1, "emp_name": "John Doe", "department": "HR", "designation": "Manager", "salary": 50000, "mob": "1234567890", "doj": "2024-01-01"},
    {"emp_id": 2, "emp_name": "Jane Smith", "department": "IT", "designation": "Developer", "salary": 60000, "mob": "9876543210", "doj": "2024-01-15"},
]

# Routes for each HTML file

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form submission logic
        emp_id = request.form['emp_id']
        emp_name = request.form['emp_name']
        department = request.form['department']
        designation = request.form['designation']
        salary = request.form['salary']
        mob = request.form['mob']
        doj = request.form['doj']
        # Assuming you have some logic to add employee data to 'employees' list/database
        employees.append({"emp_id": emp_id, "emp_name": emp_name, "department": department, "designation": designation, "salary": salary, "mob": mob, "doj": doj})
        return redirect(url_for('menu'))  # Redirect to main menu after registration
    return render_template('register.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # Handle form submission logic
        emp_name = request.form['emp_name']
        field_name = request.form['field_name']
        new_value = request.form['new_value']
        # Assuming you have logic to update employee details
        # Replace with your actual update logic
        return f"Updating {field_name} for employee {emp_name} to {new_value}"
    return render_template('update.html')

@app.route('/display', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        # Handle form submission logic
        emp_id = request.form['emp_id']
        # Assuming you have logic to fetch employee details
        # Replace with your actual display logic
        return f"Displaying details for employee ID {emp_id}"
    return render_template('display.html')

# Additional routes for other HTML files

@app.route('/display_all', methods=['GET', 'POST'])
def display_all():
    if request.method == 'POST':
        # Handle display all logic
        return render_template('display_all.html', employees=employees)
    return render_template('display_all.html', employees=[])

@app.route('/display_left', methods=['GET', 'POST'])
def display_left():
    if request.method == 'POST':
        # Handle display left logic
        # Replace with your actual logic to filter employees who have left
        left_employees = []  # Example: filter or retrieve left employees
        return render_template('display_left.html', left_employees=left_employees)
    return render_template('display_left.html', left_employees=[])

@app.route('/display_sorted', methods=['GET', 'POST'])
def display_sorted():
    if request.method == 'POST':
        field_name = request.form['field_name']
        # Assuming you have logic to sort employees by field_name
        sorted_employees = sorted(employees, key=lambda x: x.get(field_name, ""))
        return render_template('display_sorted.html', sorted_employees=sorted_employees, field_name=field_name)
    return render_template('display_sorted.html')

@app.route('/avg_salary', methods=['GET', 'POST'])
def avg_salary():
    if request.method == 'POST':
        # Assuming you have logic to calculate average salary
        avg_salary = sum(emp['salary'] for emp in employees) / len(employees) if employees else 0
        return render_template('avg_salary.html', avg_salary=avg_salary)
    return render_template('avg_salary.html', avg_salary=0)

@app.route('/create_pay_slip', methods=['GET', 'POST'])
def create_pay_slip():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        month = request.form['month']
        # Assuming you have logic to create pay slip
        # Replace with your actual logic to generate pay slip
        return f"Generating pay slip for employee ID {emp_id} for {month}"
    return render_template('create_pay_slip.html')

@app.route('/delete_all', methods=['GET', 'POST'])
def delete_all():
    if request.method == 'POST':
        # Assuming you have logic to delete all employees
        employees.clear()
        return "All employee details deleted."
    return render_template('delete_all.html')

@app.route('/create_table', methods=['GET', 'POST'])
def create_table():
    if request.method == 'POST':
        # Assuming you have logic to create a database table
        # Replace with your actual logic to create table
        return "Database table created."
    return render_template('create_table.html')

@app.route('/display_tables', methods=['GET', 'POST'])
def display_tables():
    if request.method == 'POST':
        # Assuming you have logic to fetch and display all tables
        # Replace with your actual logic to display tables
        return "Displaying all tables."
    return render_template('display_tables.html')
@app.route('/remove', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        # Assuming you have logic to remove an employee from 'employees' list/database
        # Replace with your actual remove logic
        employees[:] = [emp for emp in employees if emp.get('emp_id') != int(emp_id)]
        return redirect(url_for('menu'))  # Redirect to main menu after removal
    return render_template('remove.html')



if __name__ == '__main__':
    app.run(debug=True)
