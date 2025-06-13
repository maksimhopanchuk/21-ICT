class StudentInfo(Name):n
    def __init__(self, name=None, surname=None, birth_year=None, city=None, university=None, email=Noe):
        super().__init__(name, surname, birth_year)
        self.city = city
        self.university = university
        self.email = email

    def _is_adult(self):
        if self.birth_year is None:
            return False
        return (2025 - self.birth_year) >= 18

    def get_full_info(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "birth_year": self.birth_year,
            "city": self.city,
            "university": self.university,
            "email": self.email,
            "adult": self._is_adult()
        }
        student = StudentInfo("Максим", "Гопанчук", 2008, "Луцьк", "ТфКЛНТУ", "asdasd@gmail.com")

print("Курс:", student.calculate_course())
print("Ім'я + Прізвище:", student.create_name_list())
print("Повна інформація:")
print(student.get_full_info())
