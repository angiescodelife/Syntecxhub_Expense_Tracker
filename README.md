# Expense Tracker CLI 

A simple command-line application built with Python to help users record income and expenses, monitor their monthly finances, and export transaction reports.

This project was developed as part of a virtual internship task to demonstrate Python programming, file handling, date processing, data aggregation, and report generation.

## Features

- **Record income and expenses** with dates, categories, amounts, and descriptions.
- **Persistent storage** using CSV files.
- **View transactions** to review recorded financial entries.
- **Monthly financial summaries** showing total income, total expenses, and net balance.
- **Category-based expense breakdowns** to identify spending patterns.
- **CSV export** for sharing and analyzing transaction records.
- **Excel export** in `.xlsx` format.
- **Expense visualization** with charts generated using Matplotlib.
- **Input validation** for dates, categories, and transaction amounts.

## Technologies Used

- Python 3
- CSV module
- `datetime` for date handling
- `decimal` for financial calculations
- `openpyxl` for Excel export
- Matplotlib for chart generation
- Git and GitHub for version control

## Project Structure

```text
Expense-tracker-cli/
├── main.py
├── transactions.csv
├── requirements.txt
├── .gitignore
├── README.md
└── exports/
```

**Note:** The local `transactions.csv` file stores transaction data and is excluded from version control. The `exports/` directory stores generated reports and charts.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker-cli.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the project directory

```bash
cd expense-tracker-cli
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

## How to Use

When you launch the application, a menu displays the available options:

1. Add income
2. Add expense
3. View transactions
4. Monthly summary
5. Export transactions
6. Export expense chart
7. Exit

Select an option by entering its corresponding number in the terminal.

### Adding a Transaction

Enter the requested details:

- Date in `YYYY-MM-DD` format, or press Enter to use today's date.
- Transaction category, such as Salary, Food, or Transport.
- Positive transaction amount.
- Optional description.

### Viewing a Monthly Summary

Choose option `4` and enter the month in `YYYY-MM` format.

The application calculates:

- Total income
- Total expenses
- Net balance
- Expenses grouped by category

### Exporting Reports

Choose option `5` to export transactions to CSV or Excel.

Choose option `6` to generate a PNG chart showing expenses by category for a selected month.

Generated files are saved in the `exports/` directory.

## Example

Suppose the following transactions have been recorded for October 2026:

| Type | Category | Amount |
|---|---|---:|
| Income | Salary | 30,000.00 |
| Expense | Food | 1,500.00 |
| Expense | Transport | 500.00 |
| Expense | Food | 1,000.00 |

The monthly summary would show:

| Summary | Amount |
|---|---:|
| Total income | 30,000.00 |
| Total expenses | 3,000.00 |
| Net balance | 27,000.00 |

*Amounts are illustrative and do not represent actual financial records.*

## Learning Objectives

This project demonstrates practical application of:

- Python functions, loops, and conditional statements.
- File input/output and CSV data management.
- Date parsing and validation.
- Financial calculations and data aggregation.
- Third-party library integration.
- Exporting structured data and generating charts.
- Git version control and project documentation.

## Future Improvements

Potential enhancements include:

- Editing and deleting transactions.
- Filtering transactions by date range or category.
- Budget limits and spending alerts.
- Password-protected user accounts.
- A graphical user interface or web-based dashboard.

## Author

Developed as a Python programming internship project.

GitHub: (https://github.com/angiescodelife)

---

*This application is intended for basic personal expense tracking and educational purposes.*
