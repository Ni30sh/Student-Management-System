# Student Management System

[![](https://visitcount.itsvg.in/api?id=Student-Management-System&icon=0&color=5)](https://visitcount.itsvg.in)

This is a simple student management system implemented using Python and Tkinter. It allows users to perform various operations such as student admission, fee submission, and searching for student details.

## Features

- Student Admission: Allows users to add details of a new student to the system.
- Fee Submission: Users can submit the fee amount for a specific student by entering their Aadhar number.
- Search Student: Users can search for student details by entering their Aadhar number.
- Principal Access: Provides access to additional features for the principal, including searching for student details and fee information.

## Prerequisites

- Python 3.x
- Tkinter library
- MySQL Connector/Python library

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/student-management-system.git
   ```

2. Install the required libraries:

   ```shell
   pip install mysql-connector-python
   ```

3. Create a MySQL database named "studentpanel" and import the provided SQL file (`studentpanel.sql`) to set up the required tables.

4. Open the `main.py` file and update the MySQL database connection details in the following lines:

   ```python
   conn = mysql.connector.connect(
       host="your-hostname",
       user="your-username",
       password="your-password",
       database="studentpanel"
   )
   ```

5. Run the application:

   ```shell
   python main.py
   ```

## Usage

- Student Admission:
  - Click on the "Admission" button to open the student admission form.
  - Fill in the required details of the student and click the "Submit" button to add the student to the system.
  - The student details will be displayed in the table below.
  - You can click on the "Clear" button to clear the form fields.

- Fee Submission:
  - Click on the "Fee Submission" button to open the fee submission form.
  - Enter the Aadhar number and fee amount of the student.
  - Click the "Submit" button to submit the fee.
  - A notification will be displayed indicating whether the fee submission was successful.

- Search Student:
  - Click on the "Search Student" button to open the search form.
  - Enter the Aadhar number of the student and click the "Search" button.
  - If the student is found, their details will be displayed in the table.

- Principal Access:
  - Enter the ID and password (default ID: "admin", default password: "password") to access the principal portal.
  - In the principal portal, you can search for student details and fee information by entering the Aadhar number.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
