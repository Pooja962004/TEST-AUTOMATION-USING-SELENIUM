# TEST-AUTOMATION-USING-SELENIUM

"COMPANY": CODTECH IT SOLUTIONS

"NAME": POOJA M

"INTERN ID": CT04DY2463

"DOMAIN": SOFTWARE TESTING

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTOSH

## Project Overview

The purpose of this project is to perform **automated software testing** for a sample login functionality as part of Task 1 of the Software Testing internship program. Software testing is a crucial step in the software development lifecycle, ensuring that the application functions as intended and meets the required specifications. This project demonstrates the creation and execution of automated tests, capturing results, and generating a detailed report, which can be used to analyze the quality of the application under test.  

The task involves designing **test cases for different login scenarios**, such as valid login, invalid login, and navigation after login. These test cases are executed automatically using the **pytest framework**, which is one of the most widely used Python testing frameworks. Pytest provides a simple syntax, easy configuration, and powerful features for writing scalable and maintainable test scripts. The task also involves using **page object model (POM)** design patterns for maintaining reusable and organized code, which improves readability and reduces redundancy in test scripts.

## Tools and Technologies Used

1. **Python 3.12.6** – The primary programming language used for writing test scripts. Python provides rich support for automation and testing through libraries and frameworks.  
2. **Pytest (v8.4.2)** – A robust Python testing framework used to create, organize, and execute automated tests. It offers features such as fixtures, parameterization, and reporting.  
3. **pytest-html (v4.1.1)** – A plugin for pytest that generates **interactive HTML reports**, capturing the status of each test, duration, and detailed environment information.  
4. **Selenium WebDriver** – A tool for automating web browser interactions to perform UI testing, such as entering credentials, clicking buttons, and verifying navigation.  
5. **VS Code (Visual Studio Code)** – The editor used for writing and managing test scripts, configuration files, and the README. VS Code provides excellent integration with Python, Git, and extensions for code quality and debugging.  
6. **Git and GitHub** – Version control and repository management tools used to manage, track, and upload project files. Git ensures proper versioning of code, and GitHub provides a platform to host the repository for submission and collaboration.  
7. **Chrome Web Browser** – Used in combination with Selenium WebDriver to run automated browser tests.  

## Task Implementation

The project begins by **creating test scripts** for different scenarios using Python and pytest. The tests are structured in a modular way using a `tests/` folder, and reusable components are organized in separate files like `login_page.py`. Configuration is managed via `pytest.ini` and `conftest.py`, which help in setting up fixtures, browser instances, and environment variables.

Once the test scripts are written, they are executed using the **pytest command** in the terminal, which runs all tests automatically. The **pytest-html plugin** generates a detailed HTML report that shows which tests passed, failed, or were skipped, along with execution duration and environment details. The report provides a clear overview of the test results, making it easier for QA engineers and developers to analyze the application quality.  

The automated tests simulate real user behavior by entering valid and invalid credentials, verifying error messages, and checking the application’s navigation flow. This ensures that any regression or bug in the login functionality is detected early, reducing the risk of issues in production.  

## Project Structure

- tests/ : test scripts
- reports/ : HTML report or screenshot
- requirements.txt : Python dependencies
- README.md : project description

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/username/ST-Task1.git

2.Navigate to the project folder:
cd ST-Task1

3.Install dependencies:
pip install -r requirements.txt

4.Run tests and generate report:
pytest --html=reports/report.html --self-contained-html

## Test Summary

- Total tests: 3  
- All tests passed

#OUTPUT

![report_output.jpg](https://github.com/Pooja962004/TEST-AUTOMATION-USING-SELENIUM/blob/d37dbb815b139da840467fef5329824ed67313e0/report_output.jpg)








