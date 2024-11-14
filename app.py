from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'employee_management.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/employees', methods=['GET'])
def get_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    conn.close()
    employees = [{'id': row[0], 'name': row[1], 'age': row[2], 'department': row[3], 'position': row[4], 'salary': row[5]} for row in rows]
    return jsonify(employees)

@app.route('/api/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    
    # Check if any field is missing
    required_fields = ['name', 'age', 'department', 'position', 'salary']
    for field in required_fields:
        if field not in data or data[field] == '':
            return jsonify({'error': f"{field.capitalize()} is required"}), 400
    
    # Add employee to the database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, age, department, position, salary)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['name'], data['age'], data['department'], data['position'], data['salary']))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Employee added successfully!'})

@app.route('/api/employee/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE employees SET name = ?, age = ?, department = ?, position = ?, salary = ?
        WHERE id = ?
    ''', (data['name'], data['age'], data['department'], data['position'], data['salary'], emp_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee updated successfully!'})

@app.route('/api/employee/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
