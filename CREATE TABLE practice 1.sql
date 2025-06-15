CREATE TABLE students (
    roll_number NUMBER(10) PRIMARY KEY,  
    student_name VARCHAR2(100),         
    department VARCHAR2(50),            
    year_of_study NUMBER(1),             
    grade CHAR(2),                     
    date_of_birth DATE,                  
    contact_number VARCHAR2(15),        
    email VARCHAR2(100) UNIQUE          
);

INSERT INTO students (roll_number, student_name, department, year_of_study, grade, date_of_birth, contact_number, email)
VALUES (1001, 'John Doe', 'Computer Science', 3, 'A', TO_DATE('2002-04-15', 'YYYY-MM-DD'), '123-456-7890', 'johndoe@example.com');
