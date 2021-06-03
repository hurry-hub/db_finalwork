//创建新用户
CREATE USER 'hurry'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'hurry'@'localhost';
//创建数据库
create database course_system;
use course_system;
//建表
create table S(SNO char(4) not NULL UNIQUE,SNAME char(8),SEX char(2),AGE char(2),SDEPT char(10),LOGN char(20),hash char(32), primary key(SNO)) default charset utf8;
create table C(CNO char(4) not NULL UNIQUE,CNAME char(20),CREDI int(11),CDEPT char(10),TNAME char(8), primary key(CNO)) default charset utf8;
create table SC(SNO char(4) not NULL,CNO char(4) not NULL,GRADE int(11), primary key(SNO, CNO), foreign key(CNO)references C(CNO), foreign key(SNO)references S(SNO)) default charset utf8;
create table T(TNO char(4) not NULL UNIQUE,TNAME char(20),LOGN char(20),hash char(32), primary key(TNO)) default charset utf8;

insert into S values('S1','孔维翰','男','20','网络空间安全','S1',md5('student1'));
insert into S values('S2','姚南华','男','19','经济与管理','S2',md5('student2'));
insert into S values('S3','姜斛','男','21','计算机科学','S3',md5('student3'));
insert into S values('S4','陈双','女','20','计算机科学','S4',md5('student4'));
insert into S values('S5','吴雨晗','女','19','网络空间安全','S5',md5('student5'));
insert into S values('S6','宋珪','女','20','经济与管理','S6',md5('student6'));
insert into S values('S7','魏羡','男','21','计算机科学','S7',md5('student7'));
insert into S values('S8','顾粲','男','19','网络空间安全','S8',md5('student8'));
insert into S values('S9','高适','男','20','计算机科学','S9',md5('student9'));
insert into S values('S10','宁姚','女','18','网络空间安全','S10',md5('student10'));
insert into S values('S11','黄庭','女','20','经济与管理','S11',md5('student11'));
insert into S values('S12','陈清都','男','22','网络空间安全','S12',md5('student12'));

insert into C values('C1', '机器学习', 3, '网络空间安全', '李晨亮');
insert into C values('C2', '数据库系统', 2, '计算机科学', '余发江');
insert into C values('C3', '专业英语', 2, '网络空间安全', '李晨亮');
insert into C values('C4', '操作系统', 3, '网络空间安全', '严飞');
insert into C values('C5', '法学原理', 3, '网络空间安全', '丁鹏');
insert into C values('C6', '数据结构', 4, '计算机科学', '陈刚');
insert into C values('C7', '微观经济学', 3, '经济与管理', '丁严');
insert into C values('C8', 'R语言', 3, '经济与管理', '文庆森');
insert into C values('C9', '计算机网络', 4, '计算机科学', '陈刚');

insert into SC values('S1', 'C4', 90);
insert into SC values('S1', 'C3', 90);
insert into SC values('S2', 'C7', 86);
insert into SC values('S2', 'C3', 88);
insert into SC values('S3', 'C2', 87);
insert into SC values('S3', 'C6', 90);
insert into SC values('S4', 'C1', 91);
insert into SC values('S5', 'C5', 94);
insert into SC values('S6', 'C8', 95);
insert into SC values('S7', 'C6', 96);
insert into SC values('S8', 'C1', 85);
insert into SC values('S9', 'C9', 84);
insert into SC values('S10', 'C6', 97);
insert into SC values('S11', 'C8', 89);
insert into SC values('S12', 'C7', 87);

insert into T values('T1', '李晨亮', 'T1', md5('teacher1'));
insert into T values('T2', '余发江', 'T2', md5('teacher2'));
insert into T values('T3', '严飞', 'T3', md5('teacher3'));
insert into T values('T4', '丁鹏', 'T4', md5('teacher4'));
insert into T values('T5', '陈刚', 'T5', md5('teacher5'));
insert into T values('T6', '丁严', 'T6', md5('teacher6'));
insert into T values('T7', '文庆森', 'T7', md5('teacher7'));