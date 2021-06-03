from tkinter import *
import function

class course:
    def __init__(self, SNO):
        self.root = Tk()
        self.root.wm_title(SNO + "的选课界面")
        self.root.geometry("900x500")
        self.SNO = SNO
        self.student_label = Label(self.root, text = "学生信息")
        self.course_label = Label(self.root, text = "可选课程")
        self.score_label = Label(self.root, text = "课程成绩")
        self.choosed_label = Label(self.root, text = "已选课程")
        self.course_entry_label = Label(self.root, text = "请输入课程号：")
        self.student_text = Text(self.root, height = 10, width = 50)
        self.course_text = Text(self.root, height = 10, width = 50)
        self.score_text = Text(self.root, height = 10, width = 50)
        self.choosed_text = Text(self.root, height = 10, width = 50)
        self.choose_entry_text = Entry(self.root, width = 5)
        self.course_choose_button = Button(self.root, text = "选课", command = self.choose_course)
        self.course_delete_button = Button(self.root, text = "退课", command = self.delete_course)
        self.shut_button = Button(self.root, text = "关闭", command = exit)

    def initial(self):
        self.student_label.grid(row = 0, column = 0, sticky = W)
        self.student_text.grid(row = 1, column = 0, sticky = E)
        self.course_label.grid(row = 0, column = 1, sticky = W)
        self.course_text.grid(row = 1, column = 1, sticky = E)
        self.score_label.grid(row = 3, column = 0, sticky = W)
        self.score_text.grid(row = 4, column = 0, sticky = E)
        self.choosed_label.grid(row = 3, column = 1, sticky = W)
        self.choosed_text.grid(row = 4, column = 1, sticky = E)
        self.course_entry_label.grid(row = 0, column = 3)
        self.choose_entry_text.grid(row = 1, column = 3)
        self.course_choose_button.grid(row = 1, column = 4)
        self.course_delete_button.grid(row = 2, column = 4)
        self.shut_button.grid(row = 4, column = 4)

    def choose_course(self):
        course_no = self.choose_entry_text.get()
        course_no = function.pre_process(course_no)
        function.choose_course(self.SNO, str(course_no), 0)
        self.update()

    def delete_course(self):
        course_no = self.choose_entry_text.get()
        course_no = function.pre_process(course_no)
        function.delete_course(str(course_no))
        self.update()

    def update(self):
        self.student_text.delete(1.0, END)
        self.course_text.delete(1.0, END)
        self.score_text.delete(1.0, END)
        self.choosed_text.delete(1.0, END)
        function.display_information(self.student_text, self.SNO)
        function.avai_course(self.course_text, self.SNO)
        function.display_score(self.score_text, self.SNO)
        function.choosed_course(self.choosed_text, self.SNO)

    def init(self):
        if function.integrity_check():
            self.initial()
            self.update()
            self.root.mainloop()
        else:
            exit()

if __name__ == "__main__":
    c = course('S2')
    c.init()