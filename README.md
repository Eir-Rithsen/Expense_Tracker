Expense Tracker
A simple command-line application to manage your personal finances. This application allows you to add, update, delete, and view expenses, as well as generate summaries and export expenses to a CSV file. The expenses are stored persistently in a JSON file.

Features
Add an expense with a description and amount.
Update an existing expense.
Delete an expense by its ID.
View a list of all expenses in a tabular format.
Get a summary of total expenses, optionally for a specific month.
Export expenses to a CSV file for further analysis.
Requirements
Python 3.6 or higher
tabulate Python module for displaying data in table format
Installation
Clone the repository or download the script:

bash
Copiar código
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
Install the required dependencies:

bash
Copiar código
pip install tabulate
You're ready to use the application!

Usage
Commands
Add an Expense

bash
Copiar código
python expense_tracker.py add --description "Lunch" --amount 15.5
Adds a new expense with the specified description and amount.

List All Expenses

bash
Copiar código
python expense_tracker.py list
Displays all expenses in a table format.

Delete an Expense

bash
Copiar código
python expense_tracker.py delete --id 2
Deletes the expense with the specified ID.

Update an Expense

bash
Copiar código
python expense_tracker.py update --id 1 --description "Dinner" --amount 20
Updates the description and/or amount of the specified expense.

Get a Summary

Overall Summary:
bash
Copiar código
python expense_tracker.py summary
Monthly Summary:
bash
Copiar código
python expense_tracker.py summary --month 8
Export to CSV

bash
Copiar código
python expense_tracker.py export --output expenses.csv
Exports all expenses to a specified CSV file.

Example Usage
Add Expenses
bash
Copiar código
python expense_tracker.py add --description "Coffee" --amount 4.5
python expense_tracker.py add --description "Lunch" --amount 12.75
List Expenses
bash
Copiar código
python expense_tracker.py list
Output:

lua
Copiar código
+----+------------+-------------+--------+
| id | date       | description | amount |
+----+------------+-------------+--------+
| 1  | 2024-12-07 | Coffee      | 4.5    |
| 2  | 2024-12-07 | Lunch       | 12.75  |
+----+------------+-------------+--------+
Get a Summary
bash
Copiar código
python expense_tracker.py summary
Output:

bash
Copiar código
Total expenses: $17.25
Data Storage
Expenses are stored in a JSON file (expenses.json) in the same directory as the script. The file is automatically created if it doesn't exist.

Sample JSON Format:
json
Copiar código
[
    {
        "id": 1,
        "date": "2024-12-07",
        "description": "Coffee",
        "amount": 4.5
    },
    {
        "id": 2,
        "date": "2024-12-07",
        "description": "Lunch",
        "amount": 12.75
    }
]
Error Handling
Handles invalid IDs for deletion or updates.
Prevents adding expenses with negative amounts.
Ensures data integrity during file operations.
Customization
Feel free to extend the application with these features:

Add expense categories and filter by category.
Set monthly budgets and display warnings when exceeded.
Support importing expenses from a CSV file.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your branch.
Submit a pull request.
Author
Developed by Nicky, a Junior Full Stack Developer passionate about creating functional tools.

Feedback and Issues
If you encounter any issues or have suggestions for improvement, please open an issue in the repository or contact me directly.
