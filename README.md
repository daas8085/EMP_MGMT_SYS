# Employee Management System

A responsive web-based Employee Management System built with Flask, SQLite, and vanilla HTML, CSS, and JavaScript. This system allows users to add, view, and delete employees interactively through a simple and clean UI.

## Project Structure

```plaintext
EmployeeManagementSystem/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── app.py
├── employee_management.db
└── database_setup.py
```

### Components

- **Frontend**: HTML, CSS, JavaScript.
- **Backend**: Python with Flask.
- **Database**: SQLite.

### Project Features

1. **Add Employees**: Allows adding new employees with relevant information.
2. **View Employees**: Displays a list of current employees stored in the database.
3. **Delete Employees**: Provides the option to delete employee records.

## Getting Started

### Prerequisites

Ensure you have **Python** and **Flask** installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EmployeeManagementSystem.git
   cd EmployeeManagementSystem
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install Flask:
   ```bash
   pip install flask
   ```

### Project Setup

1. **Initialize the Database**:  
   Run `database_setup.py` to create the SQLite database and the necessary tables:
   ```bash
   python database_setup.py
   ```

   This will create a file named `employee_management.db`, which serves as your SQLite database.

2. **Start the Flask Server**:  
   Run `app.py` to start the Flask backend:
   ```bash
   python app.py
   ```

3. **Open the Application in Browser**:  
   Open your browser and go to `http://127.0.0.1:5000` to access the Employee Management System.

## File Descriptions

- `app.py`: Main Flask application file that defines the routes and connects to the SQLite database.
- `database_setup.py`: Script to initialize the SQLite database and create necessary tables.
- `static/css/style.css`: CSS file for styling the HTML pages.
- `static/js/script.js`: JavaScript file to handle frontend interactions.
- `templates/index.html`: Main HTML page that serves as the frontend interface.

## Usage

- **Adding Employees**: Fill out the employee form on the main page and submit to add a new employee.
- **Viewing Employees**: The list of employees is displayed on the main page, pulled directly from the database.
- **Deleting Employees**: Click on the delete button next to an employee to remove them from the database.

## Additional Verification (Optional)

To verify the database, you can use an SQLite client (like [DB Browser for SQLite](https://sqlitebrowser.org/)) to view the `employee_management.db` file and confirm that the `employees` table has been created and contains data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask documentation for backend setup
- SQLite for lightweight database support
- Vanilla HTML, CSS, and JavaScript for frontend implementation

---

This `README.md` provides a clear overview of your project structure, setup, and usage. Just replace `yourusername` with your actual GitHub username before uploading.
