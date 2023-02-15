class Student:
    name = 'Ivan'
    age = 18
    group_number = '10A'

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_group_number(self):
        print(self.group_number)

    def set_name_age(self, name, age):
        Student.name = name
        Student.age = age

    def set_group_number(self, group_number):
        Student.group_number = group_number


student_1 = Student()
student_2 = Student()
student_3 = Student()
student_4 = Student()
student_5 = Student()

student_1.get_name()
student_1.get_age()
student_1.get_group_number()

student_2.set_name_age('Petr', 19)
student_2.set_group_number('11Б')
student_2.get_name()
student_2.get_age()
student_2.get_group_number()

student_3.set_name_age('Vitya', 17)
student_3.set_group_number('9В')
student_3.get_name()
student_3.get_age()
student_3.get_group_number()

student_4.set_name_age('Misha', 15)
student_4.set_group_number('7Г')
student_4.get_name()
student_4.get_age()
student_4.get_group_number()

student_5.set_name_age('Nikolay', 16)
student_5.set_group_number('8Д')
student_5.get_name()
student_5.get_age()
student_5.get_group_number()


##################################################


class Solution:
    def tree(self, n, c = '*'):
        k = c
        while n != 0:
            print('{:^100}'.format(c))
            n -= 1
            c = c + 2 * k


tree_1 = Solution()
tree_1.tree(int(input()), input())
