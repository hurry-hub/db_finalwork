# coding=utf-8
import pymysql
import numpy as np
from tkinter import *
import os
import re

# 选课
def choose_course(SNO, CNO, GRADE):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "insert ignore SC (SNO, CNO, GRADE) values ('%s','%s', %d)" % (SNO, CNO, GRADE)
    cursor.execute(sql)
    db.commit()
    db.close()

# 退课
def delete_course(CNO):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "delete from SC where CNO = '%s'" % CNO
    cursor.execute(sql)
    db.commit()
    db.close()

# 展示学生相关信息
def display_information(text, LOGN):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select * from S where S.LOGN = '%s'" % LOGN
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s %4s %4s %4s' % tuple(col[0:5]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s %4s %4s %4s' % tuple(row[0:5]))
        text.insert(END, '\n')
    db.close()

# 显示可选课程
def avai_course(text, SNO):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select * from C where CNO not in (select C.CNO from S,SC,C where S.SNO = SC.SNO and C.CNO = SC.CNO and S.SNO = '%s')" % SNO
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, col)
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, row)
        text.insert(END, '\n')
    db.close()

# 显示已选课程
def choosed_course(text, SNO):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select C.CNO,C.CNAME,C.CREDI,C.CDEPT,C.TNAME from S,SC,C where S.SNO = SC.SNO and C.CNO = SC.CNO and S.SNO = '%s'" % SNO
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, col)
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, row)
        text.insert(END, '\n')
    db.close()

# 显示成绩
def display_score(text, SNO):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select C.CNO,C.CNAME,GRADE from S,SC,C where S.SNO = SC.SNO and C.CNO = SC.CNO and S.SNO = '%s'" % SNO
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, col)
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, row)
        text.insert(END, '\n')
    db.close()

# 教师任课课程
def teacher_course(TNAME):
    db = pymysql.connect(host = "127.0.0.1", user = "hurry", passwd = "123456", db = "course_system", port = 3306, charset = "utf8")
    cursor = db.cursor()
    sql = "select CNAME from C where TNAME = '%s'" % TNAME
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

# 查询选择该课的学生成绩
def find_student(text, CNAME, TNAME):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select S.SNO,S.SNAME,SC.GRADE from S,SC,C where S.SNO = SC.SNO and C.CNO = SC.CNO and C.CNAME = '%s' and C.TNAME = '%s'" % (CNAME, TNAME)
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, col)
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, row)
        text.insert(END, '\n')
    db.close()

# 教师修改成绩
def change_score(SNO, GRADE, CNAME):
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select CNO from C where CNAME = '%s'" % CNAME
    cursor.execute(sql)
    result = cursor.fetchall()
    sql = "replace into SC (SNO, CNO, GRADE) values ('%s', '%s', %d)" % (SNO, result[0][0], int(GRADE))
    cursor.execute(sql)
    db.commit()
    db.close()

# 老师备份数据
def sql_bak():
    cmd = r'mysqldump -uhurry -p123456 course_system > D:\大二复习\数据库\final_work\bak.sql'
    os.system(cmd)

# 老师导入数据
def sql_guide():
    cmd = r'mysql -uhurry -p123456 course_system< D:\大二复习\数据库\final_work\bak.sql'
    os.system(cmd)

# 完整性检查
def integrity_check():
    db = pymysql.connect(host="127.0.0.1", user="hurry", passwd="123456", db="course_system", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = "select @@unique_checks"
    cursor.execute(sql)
    un_result = cursor.fetchall()
    sql = "select @@foreign_key_checks"
    cursor.execute(sql)
    for_result = cursor.fetchall()
    db.commit()
    db.close()
    # print(un_result)
    # print(un_result[0][0] & for_result[0][0])
    return un_result[0][0] & for_result[0][0]

def pre_process(input):
    input = re.sub(r'\',.`!?":;@#$%&*“；，。、]', '', input)         # 去除sql命令中的乱码
    return input