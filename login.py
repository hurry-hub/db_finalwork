from tkinter import *
import student
import teacher
import function
import pymysql
import hashlib

def judge():
    login = user_entry.get()
    login = function.pre_process(login)
    if login[0] != 'S' and login[0] != 'T':
        Label(root, text = "请输入正确的信息").grid(row = 1, column = 2)
    else:
        password = password_entry.get()
        password = function.pre_process(password)
        password = hashlib.md5(password.encode('utf8')).hexdigest()
        db = pymysql.connect(host = "127.0.0.1", user = "hurry", passwd = "123456", db = "course_system", port = 3306, charset = "utf8")
        cursor = db.cursor()
        sql = "select S.SNO from S where S.LOGN = '%s' and S.hash = '%s'" % (login, password)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            cursor = db.cursor()
            sql = "select T.TNAME from T where T.LOGN = '%s' and T.hash = '%s'" % (login, password)
            cursor.execute(sql)
            result = cursor.fetchall()
        else:
            return result
        return result

def init():
    result = judge()
    if len(result) != 0:
        root.destroy()
        if result[0][0][0] == 'S':
            c = student.course(result[0][0])
            c.init()
        else:
            t = teacher.teacher(result[0][0])
            t.init()
    else:
        Label(root, text = "用户名或密码错误，请重新输入：").grid(row = 3, column = 1)

root = Tk()
root.title("教务系统登录")
root.geometry("300x150")

Label(root, text = "请输入账号和密码").grid(row = 0, column = 1)
Label(root, text = "用户名").grid(row = 1, column = 0)
user_entry = Entry(root, width = 15)
user_entry.grid(row = 1, column = 1)
Label(root, text = "密码").grid(row = 2, column = 0)
password_entry = Entry(root, width = 15)
password_entry.grid(row = 2, column = 1)

start_button = Button(root, text = "登陆", command = init)
start_button.grid(row = 3, column = 1)
root.mainloop()