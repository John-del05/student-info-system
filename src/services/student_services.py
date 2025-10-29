import json
import os
import logging
from datetime import datetime
from models.student import Student

logger = logging.getLogger(__name__)

class StudentService:
    def __init__(self, data_file='data/students.json'):
        self.data_file = data_file
        self._ensure_data_file()

    def _ensure_data_file(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def _load_students(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_students(self, students):
        with open(self.data_file, 'w') as f:
            json.dump(students, f, indent=2)

    def add_student(self, student_data):
        students = self._load_students()
        student = Student(**student_data)
        students.append(student.to_dict())
        self._save_students(students)
        logger.info(f"Added student: {student.student_id}")
        return student.to_dict()

    def get_all_students(self):
        logger.info("Viewed all students")
        return self._load_students()

    def get_student(self, student_id):
        students = self._load_students()
        for student in students:
            if student['student_id'] == student_id:
                logger.info(f"Viewed student by ID: {student_id}")
                return student
        logger.warning(f"Student ID not found: {student_id}")
        return None

    def update_student(self, student_id, update_data):
        students = self._load_students()
        for student in students:
            if student['student_id'] == student_id:
                student.update(update_data)
                student['updated_at'] = datetime.now().isoformat()
                self._save_students(students)
                logger.info(f"Updated student: {student_id}")
                return student
        logger.warning(f"Update failed — Student ID not found: {student_id}")
        return None

    def delete_student(self, student_id):
        old_students = self._load_students()
        students = [s for s in old_students if s['student_id'] != student_id]
        self._save_students(students)
        if len(students) != len(old_students):
            logger.info(f"Deleted student: {student_id}")
            return True
        logger.warning(f"Delete failed — Student ID not found: {student_id}")
        return False
