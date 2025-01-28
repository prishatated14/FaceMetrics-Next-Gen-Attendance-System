CREATE DATABASE attendance_system;

USE attendance_system;

CREATE TABLE students (
  reg_no INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  photo_reference VARCHAR(255),
  photo_reference2 varchar(255),
  email varchar(255) unique
);
create table authentication(
id int primary key auto_increment,
student_id int not null,
username varchar(255) not null,
hashed_password varchar(255) not null,
foreign key (student_id) references students(reg_no)
);

CREATE TABLE attendance (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id int NOT NULL,  -- References student reg_no in students table
  date DATE NOT NULL,  
  status ENUM('present', 'absent', 'excused') NOT NULL,  
  FOREIGN KEY (student_id) REFERENCES students(reg_no)  
);

