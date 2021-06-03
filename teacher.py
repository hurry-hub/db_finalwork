from tkinter import *
import function

class teacher:
    def __init__(self, TNO):
        self.TNO = TNO
        self.temp = (1,)
        self.root = Tk()
        self.root.title(TNO + "的任教情况")
        self.root.geometry("500x400")
        self.course_label = Label(self.root, text = "请选择课程名：")
        self.student_label = Label(self.root, text = "选修课程学生：")
        self.student_text = Text(self.root, height = 10, width = 20)
        self.lb = Listbox(self.root, height = 10, width = 20)
        Label(self.root, text = "学号：").grid(row = 3, column = 3)
        Label(self.root, text = "成绩：").grid(row = 5, column = 3)
        self.student_id_entry = Entry(self.root, text = "学号", width = 5)
        self.student_grade_entry = Entry(self.root, text = "成绩", width = 5)
        self.student_button = Button(self.root, text = "查询", command = self.find_score)
        self.score_button = Button(self.root, text = "输入成绩", command = self.change_score)
        self.bak = Button(self.root, text = "备份", command = self.sql_bak)
        self.guide = Button(self.root, text = "恢复", command = self.sql_guide)
        self.exit = Button(self.root, text = "退出", command = exit)

    def initial(self):
        self.course_label.grid(row = 1, column = 0)
        self.student_label.grid(row = 1, column = 1)
        self.student_text.grid(row = 2, column = 1)
        var = StringVar()
        for item in function.teacher_course(self.TNO):
            self.lb.insert(END, item)
        self.lb.grid(row = 2, column = 0)
        self.student_id_entry.grid(row = 4, column = 3)
        self.student_grade_entry.grid(row = 6, column = 3)
        self.student_button.grid(row = 4, column = 0)
        self.score_button.grid(row = 4, column = 1)
        self.bak.grid(row = 7, column = 0)
        self.guide.grid(row = 7, column = 1)
        self.exit.grid(row = 7, column = 3)

    def find_score(self):
        CNAME = self.lb.get(self.lb.curselection())[0]
        self.student_text.delete(1.0, END)
        function.find_student(self.student_text, CNAME, self.TNO)

    def find_new_score(self, index):
        CNAME = self.lb.get(index)[0]
        self.student_text.delete(1.0, END)
        function.find_student(self.student_text, CNAME, self.TNO)

    def change_score(self):
        SNO = self.student_id_entry.get()
        SNO = function.pre_process(SNO)
        GRADE = self.student_grade_entry.get()
        GRADE = function.pre_process(GRADE)
        index = self.lb.curselection()
        if len(index) == 0:
            index = self.temp
        # print(index)
        CNAME = self.lb.get(index)[0]
        function.change_score(SNO, GRADE, CNAME)
        self.find_new_score(index)
        self.temp = index

    def sql_bak(self):
        function.sql_bak()

    def sql_guide(self):
        function.sql_guide()
        self.find_score()

    def init(self):
        if function.integrity_check():
            self.initial()
            self.root.mainloop()
        else:
            exit()

if __name__ == "__main__":
    t = teacher('T2')
    t.init()