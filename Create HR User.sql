-- Create HR User
CREATE USER hr IDENTIFIED BY hr_password
DEFAULT TABLESPACE users
TEMPORARY TABLESPACE temp;

-- Grant necessary privileges
GRANT CONNECT, RESOURCE TO hr;

-- Switch to HR user and create schema objects
CONNECT hr/hr_password;

-- Create tables
CREATE TABLE employees (
    employee_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    email VARCHAR2(100),
    hire_date DATE,
    job_id VARCHAR2(10),
    salary NUMBER
);

CREATE TABLE departments (
    department_id NUMBER PRIMARY KEY,
    department_name VARCHAR2(50)
);

-- Insert sample data
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary) VALUES
(100, 'John', 'Doe', 'jdoe@example.com', SYSDATE, 'IT_PROG', 60000);

INSERT INTO departments (department_id, department_name) VALUES
(10, 'IT');
