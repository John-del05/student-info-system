def is_valid_student_id(student_id):
    return isinstance(student_id, str) and len(student_id.strip()) > 0

def is_valid_name(name):
    return isinstance(name, str) and len(name.strip()) > 0
