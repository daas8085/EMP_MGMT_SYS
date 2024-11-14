// Fetch and display all employees
function fetchEmployees() {
    fetch('/api/employees')
        .then(response => response.json())
        .then(data => {
            const employeeList = document.getElementById('employee-list');
            employeeList.innerHTML = '<h2>Employee List</h2>';
            data.forEach(employee => {
                employeeList.innerHTML += `
                    <div class="employee">
                        <p><strong>Name:</strong> ${employee.name}</p>
                        <p><strong>Age:</strong> ${employee.age}</p>
                        <p><strong>Department:</strong> ${employee.department}</p>
                        <p><strong>Position:</strong> ${employee.position}</p>
                        <p><strong>Salary:</strong> $${employee.salary}</p>
                        <button onclick="deleteEmployee(${employee.id})">Delete</button>
                    </div>
                `;
            });
        });
}

// Add new employee
function addEmployee() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const department = document.getElementById('department').value;
    const position = document.getElementById('position').value;
    const salary = document.getElementById('salary').value;
    
    // Check for missing fields
    if (!name || !age || !department || !position || !salary) {
        alert("All fields are required. Please fill in every field.");
        return;
    }

    fetch('/api/employee', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, age, department, position, salary })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => { throw new Error(data.error); });
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
        fetchEmployees();
    })
    .catch(error => alert(error.message));
}

// Delete employee
function deleteEmployee(emp_id) {
    fetch(`/api/employee/${emp_id}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            fetchEmployees();
        });
}

// Initialize employee list on page load
document.addEventListener('DOMContentLoaded', fetchEmployees);

