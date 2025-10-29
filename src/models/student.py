from datetime import datetime

class Student:
    def __init__(self, student_id, name, email, course, year_level, gpa=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course = course
        self.year_level = year_level
        self.gpa = gpa
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "course": self.course,
            "year_level": self.year_level,
            "gpa": self.gpa,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
