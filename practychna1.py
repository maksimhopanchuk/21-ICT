class Name:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        currentyear = 2025
        age = currentyear - self.birth_year
        course = age - 16
        return course if course > 0 else 0

    def create_name_list(self):
        return [self.name, self.surname]

student = Name("Максим", "Гопанчук", 2008)
print("Курс:", student.calculate_course())
print("Список:", student.create_name_list())
