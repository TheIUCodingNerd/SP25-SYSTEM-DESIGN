import mysql.connector
import random

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="django_user",
    password="your_mysql_password",
    database="student_management"
)

cursor = db.cursor()

# Sample student data
students = [
    ("Alice Johnson", "S1001", "alice@example.com", "555-1234", "A"),
    ("Bob Smith", "S1002", "bob@example.com", "555-5678", "B"),
    ("Charlie Brown", "S1003", "charlie@example.com", "555-8765", "C"),
    ("Diana Ross", "S1004", "diana@example.com", "555-4321", "A"),
]

# Insert student data into the database
for student in students:
    cursor.execute("INSERT INTO students_student (name, student_id, email, phone, grade) VALUES (%s, %s, %s, %s, %s)", student)

db.commit()
cursor.close()
db.close()

print("✅ Student data has been added successfully!")
