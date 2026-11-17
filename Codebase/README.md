# Placement Data Analyzer

## 1. Project Overview

Placement Data Analyzer is a Python-based project developed to analyze student placement records. It processes placement data, calculates important placement statistics, identifies invalid records, and performs branch-wise analysis.

The project uses Pandas for data manipulation and Matplotlib for data visualization. It includes four different test cases to demonstrate how placement data can be processed and analyzed under different conditions.

## 2. Project Objectives

- To analyze student placement records.
- To calculate average and highest placement packages.
- To identify invalid and negative package values.
- To compare placement statistics across different branches.
- To filter students based on package criteria.
- To represent placement information using graphical charts.

## 3. Features

- Four different test cases for placement analysis.
- Reading and processing placement data using CSV files.
- Calculation of total students placed.
- Calculation of average and highest packages.
- Identification of students receiving packages above 7 LPA.
- Detection and removal of invalid records.
- Handling of negative and non-numeric package values.
- Branch-wise placement analysis.
- Pie chart for branch-wise placement distribution.
- Bar chart for comparing average packages.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |

## 5. Test Cases

**Test Case 1 – Normal Input**

Processes regular student placement records and calculates total placements, average package, and highest package.

**Test Case 2 – Minimum Input**

Tests the program using a dataset containing only one student record.

**Test Case 3 – Invalid Input**

Checks how the program handles invalid and negative package values while retaining valid records.

**Test Case 4 – Branch-wise Analysis**

Analyzes placements across different branches, calculates branch-wise average packages, identifies students above 7 LPA, and generates pie and bar charts.

## 6. Project Structure

```text
Placement_Data_Analyzer/
│
├── Codebase/
│   └── code.py
│   └── README.MD
│
├── TestCases/
│   ├── TC1.png
│   ├── TC2.png
│   ├── TC3.png
│   └── TC4.png
│
└── README.md
```

## 7. Libraries Required

Install the required Python libraries using:

```bash
pip install pandas matplotlib
```

## 8. How to Run the Project

1. Clone or download the GitHub repository.
2. Open the project in VS Code or GitHub Codespaces.
3. Install the required libraries.
4. Run the Python source file.
5. Select a test case from the menu.
6. View the generated results and charts.

## 9. Expected Outcomes

The project produces placement statistics, validates placement records, compares branch-wise performance, and displays graphical representations of placement information.

## 10. Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and logical operations.
- Working with Pandas DataFrames.
- Reading and processing CSV files.
- Data validation and cleaning.
- Statistical calculations and data filtering.
- Grouping and analyzing datasets.
- Creating visualizations using Matplotlib.

## 11. Developer Information

**Developed by:** Ritika Sahu

**Field of Study:** Cybersecurity

**Project:** Python Programming – Placement Data Analyzer

This project was developed as part of an academic self-learning activity to improve practical programming skills and understanding of data analysis.