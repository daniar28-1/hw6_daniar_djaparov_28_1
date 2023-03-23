class Person:
    def __init__(self, the_fullname, the_age, the_is_married ):
        self.fullname = the_fullname
        self.age = the_age
        self.is_married = the_is_married


Human_Person = Person('djaparov daniyar bakutovich', '16','not married'  )
print(Human_Person)
print(f'Fullname {Human_Person.fullname} age:{Human_Person.age} is_married:{Human_Person.is_married}')

class Student(Person):
    number_of_ratings = 350
    def __init__(self, the_fullname, the_age, the_is_married):
      super().__init__(the_fullname, the_age, the_is_married)

marks = {
    'algebra': '80' ,
    'physics': '60' ,
    'biology': '100' ,
    'story': '40' ,
}
print(f'We need {Student.number_of_ratings / 4}'f'average rating ')

class Taecher(Person):
    salary = 10000

    def __init__(self, the_fullname, the_age, the_is_married ):
        self.fullname = the_fullname
        self.age = the_age
        self.is_married = the_is_married

Human_Taecher = Taecher('djaparova aygyl bakutovna', '38','married'  )
print(Human_Taecher)
print(f'Fullname {Human_Taecher.fullname} age:{Human_Taecher.age} is_married:{Human_Taecher.is_married}')





print(f'We need {Taecher.salary }')
