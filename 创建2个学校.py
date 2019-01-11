Course_list = []
class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers_list = []
        self.students_list = []

        global Course_list

    def hire(self,obj):
        self.teachers_list.append(obj.name)
        print("我们聘请了一位新老师", obj.name)

    def enroll(self,obj):
        self.students_list.append(obj.name)
        print("欢迎我们的新学员",obj.name)

class Grade(School):
    def __init__(self,school_name,grade_code,grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("{}校区{}期{}课程".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲{} day01, day02, day03".format(self.course))

Python = Grade("北京", 3, "Python")
Linux = Grade("成都", 1, "Linux")

class School_members(object):
    def __init__(self,name,age,sex,role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("姓名:{} 年龄:{} 性别:{} 角色:{}".format(self.name, self.age, self.sex, self.role))

members = School_members("陈殷峰", 21, "男", "学员")

stu_num_id = 0

class Students(School_members):
    def __init__(self,name,age,sex,role,course):
        super(Students, self).__init__(name,age,sex,role)
        global stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + str(course.code) + str(stu_num_id).zfill(2)
        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我学习的课程是{}，我的学号{}".format(course.course, self.id))

    def pay(self, course):
        print("我花了1000块学习这门{}课程".format(course.course))

    def praise(self, obj):
        print("{}觉得这个{}很赞".format(self.name, obj.name))

    def mark_list(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("{}退出888".format(self.name))

Tea_id = 0
class Teachers(School_members):
    def __init__(self, name, age, sex, role, course):
        super(Teachers, self).__init__(name, age, sex, role)
        global Tea_id
        Tea_id += 1
        Tea_id = course.school_name + str(course.code) + str(Tea_id).zfill(2)
        self.tea_id = Tea_id

    def teacher(self, course):
        print("我教的课程是{},我的id是{}".format(course.course, self.tea_id))

    def record_mark(self, date, course, obj,level):
        print("Day{} {}课 {} 等级{}".format(date, course, obj.name, level))


R = Students("Rimm", 22, "M", "学员", Python)
Python.enroll(R)
R.study(Python)
R.pay(Python)

W = Students("老王", 23, "M", "学员", Linux)
Linux.enroll(W)
W.study(Linux)
W.pay(Linux)

Z = Teachers("周老师", 30, "M", "老师", Python)
Python.hire(Z)
Z.teacher(Python)
Z.record_mark(1, "Python", R, "A")
R.out()
R.praise(Z)
