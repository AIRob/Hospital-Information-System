import xlrd
import xlwt
from xlutils.copy import copy
# from openpyxl import Workbook as wk
# from openpyxl import load_workbook as lw
# from openpyxl.writer.excel import ExcelWriter as ew
from tkinter import *

global_col = 1
global_coll = 1

patientsinfo = xlwt.Workbook(encoding='ascii')

diseasesinfo = xlwt.Workbook(encoding='ascii')


patient_info = patientsinfo.add_sheet('patients')
one_patient_info = patientsinfo.add_sheet('the patient')

disease_info = diseasesinfo.add_sheet('diseases')

patient_info.write(0, 0, label='ID')
patient_info.write(0, 1, label='姓名')
patient_info.write(0, 2, label='性别')
patient_info.write(0, 3, label='电话')
patient_info.write(0, 4, label='地址')
patient_info.write(0, 5, label='疾病')
patient_info.write(0, 6, label='疾病ID')

disease_info.write(0, 0, label='ID')
disease_info.write(0, 1, label='疾病')
# disease_info.write(0,2,label='传染性')

one_patient_info.write(0, 0, label='ID')
one_patient_info.write(0, 1, label='姓名')
one_patient_info.write(0, 2, label='性别')
one_patient_info.write(0, 3, label='电话')
one_patient_info.write(0, 4, label='地址')
one_patient_info.write(0, 5, label='疾病')
one_patient_info.write(0, 6, label='疾病ID')
one_patient_info.write(0, 7, label='传染性')

patientsinfo.save('patients.xls')
diseasesinfo.save('diseases.xls')


class disease():
    def __init__(self):
        print("创建疾病类")

    # def if_infect(self):
    #     if int(self.id)==0:
    #         self.a="无传染性"
    #     elif int(self.id)==1:
    #         self.a = "甲型传染病"
    #     elif int(self.id)==2:
    #         self.a = "乙型传染病"
    #     elif int(self.id)==3:
    #         self.a = "丙型传染病"

    def saveinfo(self):
        global global_coll
        # workbook_=lw('patients.xls')
        # sheetnames=workbook_.get_sheet_names()
        # sheet=workbook_.get_sheet_by_name(sheetnames[0])
        # sheet.cell(row=,column=).value=""

        workbook = xlrd.open_workbook('diseases.xls')
        workbooknew = copy(workbook)
        ws = workbooknew.get_sheet(0)

        ws.write(global_coll, 0, self.id)
        ws.write(global_coll, 1, self.name)

        # if int(table.cell(r, 6).value) == 0:
        #     ws.write(r, 7, '无传染性疾病')
        # elif int(table.cell(r, 6).value) == 1:
        #     ws.write(r, 7, '甲型传染病')
        # elif int(table.cell(r, 6).value) == 2:
        #     ws.write(r, 7, '乙型传染病')
        # elif int(table.cell(r, 6).value) == 3:
        #     ws.write(r, 7, '丙型传染病')

        workbooknew.save('diseases.xls')

        # workbook1=xlrd.open_workbook("diseases.xls")
        # workbook1new=copy(workbook1)
        # table = workbook1.sheet_by_index(0)
        # ws1=workbook1new.get_sheet(0)

        # if int(table.cell(global_coll, 0).value) == 0:
        #     ws.write(global_coll, 2, '无传染性疾病')
        # elif int(table.cell(global_coll, 0).value) == 1:
        #     ws.write(global_coll, 2, '甲型传染病')
        # elif int(table.cell(global_coll, 0).value) == 2:
        #     ws.write(global_coll, 2, '乙型传染病')
        # elif int(table.cell(global_coll, 0).value) == 3:
        #     ws.write(global_coll, 2, '丙型传染病')

        # workbook1new.save('diseases.xls')

        global_coll = global_coll+1


class gui_print_disease():
    #打印窗口初始化
    def __init__(self, new_print_disease):
        self.window = new_print_disease
        #导入excel数据
        self.data = xlrd.open_workbook('diseases.xls')
        self.table = self.data.sheet_by_index(0)

    #设置窗口属性
    def set_new_print_disease(self):
        #测试函数
        print("调用了set_new_print_disease函数")

        #设置标题
        self.window.title("Disease")

        #标签
        self.search_label = Label(self.window, text="输入疾病名")
        self.search_label.grid(row=0, column=0)
        self.result_label = Label(self.window, text='查找结果')
        self.result_label.grid(row=0, column=15)

        #文本框
        self.id_Text = Text(self.window, width=10, height=5)
        self.id_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_Text = Text(self.window, width=30, height=5)
        self.result_Text.grid(row=1, column=15, rowspan=10, columnspan=10)

        #按钮
        self.print_button = Button(
            self.window, text="查找", bg="lightblue", width=10, command=self.info_print)
        self.print_button.grid(row=1, column=11)

    def info_search(self):
        src = self.id_Text.get(1.0, END).strip().replace("\n", "").encode()
        int_src = str(src)

        a = True
        i = 1
        while a:
            if str(self.table.cell(i, 1).value) == int_src:
                self.out = i
                print("找到了%s%s" % (self.out, self.table.cell(self.out, 1).value))
                # self.patient = patient()
                # self.patient.sava_a_info(self.out)
                if int(self.table.cell(self.out, 0).value) == 0:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "疾病名：%s传染性：无" % str(
                        self.table.cell(self.out, 1).value))
                elif int(self.table.cell(self.out, 0).value) == 1:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s传染性：甲型" % str(
                        self.table.cell(self.out, 1).value))
                elif int(self.table.cell(self.out, 0).value) == 2:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s传染性：乙型" % str(
                        self.table.cell(self.out, 1).value))
                elif int(self.table.cell(self.out, 0).value) == 3:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s传染性：丙型" % str(
                        self.table.cell(self.out, 1).value))
                a = False
                break
            elif str(self.table.cell(i, 0).value) != int_src and self.table.cell(i, 0).value != None:
                i = i+1
            elif self.table.cell(i, 0).value == None:
                self.result_Text.delete(1.0, END)
                self.result_Text.insert(1.0, "无此人")
                a = False
                break
            break

        #测试函数
        if src == b'10':
            print("src= %s %s" % (src, int_src))

    def info_print(self):
        self.info_search()


class patient():

    def __init__(self):
        print("创建病人类")

    # def get_name(self):
    #     self.name=input("姓名：")

    # def get_gender(self):
    #     gender=input("性别：")

    # def get_id(self):
    #     pid=input("证件号：")

    # def get_tel(self):
    #     tel=input("联系方式：")

    # def get_address(self):
    #     address=input("家庭住址：")

    def showinfo(self):
        print("病人信息如下 \n ID：%s \n 姓名：%s ，性别：%s ； \n 电话：%s ， 地址：%s \n 疾病： %s ，疾病ID：%s" % (
            self.id, self.name, self.gender, self.tel, self.address, self.disease_name, self.disease_id))

    def saveinfo(self):
        global global_col
        # workbook_=lw('patients.xls')
        # sheetnames=workbook_.get_sheet_names()
        # sheet=workbook_.get_sheet_by_name(sheetnames[0])
        # sheet.cell(row=,column=).value=""

        workbook = xlrd.open_workbook('patients.xls')
        workbooknew = copy(workbook)
        ws = workbooknew.get_sheet(0)

        ws.write(global_col, 0, self.id)
        ws.write(global_col, 1, self.name)
        ws.write(global_col, 2, self.gender)
        ws.write(global_col, 3, self.tel)
        ws.write(global_col, 4, self.address)
        ws.write(global_col, 5, self.disease_name)
        ws.write(global_col, 6, self.disease_id)

        global_col = global_col+1

        workbooknew.save('patients.xls')

    def sava_a_info(self, r):
        raw = r
        workbook = xlrd.open_workbook('patients.xls')
        workbooknew = copy(workbook)
        table = workbook.sheet_by_index(0)
        ws = workbooknew.get_sheet(1)

        ws.write(r, 0, table.cell(r, 0).value)
        ws.write(r, 1, table.cell(r, 1).value)
        ws.write(r, 2, table.cell(r, 2).value)
        ws.write(r, 3, table.cell(r, 3).value)
        ws.write(r, 4, table.cell(r, 4).value)
        ws.write(r, 5, table.cell(r, 5).value)
        ws.write(r, 6, table.cell(r, 6).value)

        if int(table.cell(r, 6).value) == 0:
            ws.write(r, 7, '无传染性疾病')
        elif int(table.cell(r, 6).value) == 1:
            ws.write(r, 7, '甲型传染病')
        elif int(table.cell(r, 6).value) == 2:
            ws.write(r, 7, '乙型传染病')
        elif int(table.cell(r, 6).value) == 3:
            ws.write(r, 7, '丙型传染病')

        workbooknew.save('patients.xls')

# ##传染病警告
# #甲类传染病警告
# class gui_alert1():

#     #警告界面初始化
#     def __init__(self,new_alert_window):
#         self.window=new_alert_window

#     #设置窗口属性
#     def set_new_alert1_window(self):
#         #测试函数
#         print("调用了set_new_alert_window函数")
#         self.window.title("ALERT")

#         #按钮
#         self.str_trans_to_md5_button = Button(self.window, text="警告 \n 此为甲类传染性疾病", fg="white", bg="red", width=10, height=10, command=self.window.quit)
#         self.str_trans_to_md5_button.grid(row=0, column=0)

# #乙类传染病警告
# class gui_alert2():

#     #警告界面初始化
#     def __init__(self, new_alert_window):
#         self.window = new_alert_window

#     #设置窗口属性
#     def set_new_alert2_window(self):
#         #测试函数
#         print("调用了set_new_alert_window函数")
#         self.window.title("ALERT")

#         #按钮
#         self.str_trans_to_md5_button = Button(self.window, text="警告 \n 此为乙类传染性疾病", fg="white", bg="red", width=10, height=10, command=self.window.quit)
#         self.str_trans_to_md5_button.grid(row=0, column=0)

# #丙类传染病警告
# class gui_alert3():

#     #警告界面初始化
#     def __init__(self, new_alert_window):
#         self.window = new_alert_window

#     #设置窗口属性
#     def set_new_alert3_window(self):
#         #测试函数
#         print("调用了set_new_alert_window函数")
#         self.window.title("ALERT")

#         #按钮
#         self.str_trans_to_md5_button = Button(self.window, text="警告 \n 此为丙类传染性疾病", fg="white", bg="red", width=10, height=10, command=self.window.quit)
#         self.str_trans_to_md5_button.grid(row=0, column=0)


class gui_new_disease():
    #疾病窗口初始化
    def __init__(self, new_disease_window):
        self.window = new_disease_window

     #设置窗口属性
    def set_new_disease_window(self):

        #测试函数
        print("调用了set_new_disease_window函数")

        #设置标题
        self.window.title("New Disease")

        #标签
        self.disease_id_lablel = Label(self.window, text="疾病ID")
        self.disease_id_lablel.grid(row=0, column=0)

        self.disease_name_label = Label(self.window, text="疾病")
        self.disease_name_label.grid(row=0, column=15)

        #文本框
        self.disease_id_Text = Text(self.window, width=10, height=5)
        self.disease_id_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.disease_name_Text = Text(self.window, width=10, height=5)
        self.disease_name_Text.grid(
            row=1, column=15, rowspan=10, columnspan=10)

        # #文本框
        # #self.st_id = StringVar()
        # self.disease_id_Entry = Entry(self.window)
        # self.disease_id_Entry.grid(row=0, column=12)

        # #self.st_name = StringVar()
        # self.disease_name_Entry = Entry(self.window)
        # self.disease_name_Entry.grid(row=1, column=12)

        #按钮
        self.str_trans_to_md5_button = Button(
            self.window, text="保存", bg="lightblue", width=10, command=self.save_button)
        self.str_trans_to_md5_button.grid(row=15, column=15)

    def get(self):
        #测试函数
        print("调用了get函数")

        # self.patient_id= self.patient_id_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_name = self.patient_name_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_gender = self.patient_gender_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_tel = self.patient_tel_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_address = self.patient_address_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.disease_name = self.disease_name_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.disease_id = self.disease_id_Text.get(1.0, END).strip().replace("\n", "").encode()

        self.disease_id = int(self.disease_id_Text.get(
            1.0, END).strip().replace("\n", "").encode())

        self.disease_name = str(self.disease_name_Text.get(
            1.0, END).strip().replace("\n", "").encode())

    #数据保存
    def save(self):

        #测试代码
        print("调用了save函数")
        self.get()

        #创建新病人
        self.disease = disease()
        self.disease.id = self.disease_id
        self.disease.name = self.disease_name
        # self.patient.address = self.patient_address
        # self.patient.gender = self.patient_gender
        # self.patient.tel = self.patient_tel
        # self.patient.disease_id = self.disease_id
        # self.patient.disease_name = self.disease_name

        # self.patient.showinfo()
        self.disease.saveinfo()

    def save_button(self):
        # if self.patient.disease_id==b'0':
            self.save()
        # elif self.disease_id=="1":
        #     self.save()
        #     self.alert1()
        # elif self.disease_id=="2":
        #     self.save()
        #     self.alert2()
        # elif self.disease_id=="3":
        #     self.save()
        #     self.alert3()


class gui_new_patient():

    #病人窗口初始化
    def __init__(self, new_patient_window):
        self.window = new_patient_window

    #设置窗口属性
    def set_new_patient_window(self):

        #测试函数
        print("调用了set_new_patient_window函数")

        #设置标题
        self.window.title("New Patient")

        #标签
        self.patient_id_lablel = Label(self.window, text="病人ID")
        self.patient_id_lablel.grid(row=0, column=0)

        self.patient_name_label = Label(self.window, text="姓名")
        self.patient_name_label.grid(row=1, column=0)

        self.patient_gender_label = Label(self.window, text="性别")
        self.patient_gender_label.grid(row=1, column=12)

        self.patient_tel_label = Label(self.window, text="电话")
        self.patient_tel_label.grid(row=2, column=0)

        self.patient_address_label = Label(self.window, text="地址")
        self.patient_address_label.grid(row=2, column=12)

        self.disease_name_label = Label(self.window, text="疾病")
        self.disease_name_label.grid(row=3, column=0)

        self.disease_id_label = Label(self.window, text="疾病ID")
        self.disease_id_label.grid(row=3, column=12)

        # #文本框
        # self.patient_id_Text = Text(self.window, width=10, height=5)
        # self.patient_id_Text.grid(row=0, column=1, rowspan=10, columnspan=10)

        # self.patient_name_Text = Text(self.window, width=10, height=5)
        # self.patient_name_Text.grid(row=1, column=1, rowspan=10, columnspan=10)

        # self.patient_gender_Text = Text(self.window, width=10, height=5)
        # self.patient_gender_Text.grid(row=1, column=13, rowspan=10, columnspan=10)

        # self.patient_tel_Text = Text(self.window, width=10, height=5)
        # self.patient_tel_Text.grid(row=2, column=1, rowspan=10, columnspan=10)

        # self.patient_address_Text = Text(self.window, width=10, height=5)
        # self.patient_address_Text.grid(row=2, column=13, rowspan=10, columnspan=10)

        # self.disease_name_Text = Text(self.window, width=10, height=5)
        # self.disease_name_Text.grid(row=3, column=1, rowspan=10, columnspan=10)

        # self.disease_id_Text = Text(self.window, width=10, height=5)
        # self.disease_id_Text.grid(row=3, column=13, rowspan=10, columnspan=10)

        #文本框
        #self.st_id = StringVar()
        self.patient_id_Entry = Entry(self.window)
        self.patient_id_Entry.grid(row=0, column=1)

        #self.st_name = StringVar()
        self.patient_name_Entry = Entry(self.window)
        self.patient_name_Entry.grid(row=1, column=1)

        #self.st_gender=StringVar()
        self.patient_gender_Entry = Entry(self.window)
        self.patient_gender_Entry.grid(row=1, column=13)

        #self.st_tel=StringVar()
        self.patient_tel_Entry = Entry(self.window)
        self.patient_tel_Entry.grid(row=2, column=1)

        #self.st_address=StringVar()
        self.patient_address_Entry = Entry(self.window)
        self.patient_address_Entry.grid(row=2, column=13)

        #self.st_di_name=StringVar()
        self.disease_name_Entry = Entry(self.window)
        self.disease_name_Entry.grid(row=3, column=1)

        #self.st_di_id=StringVar()
        self.disease_id_Entry = Entry(self.window)
        self.disease_id_Entry.grid(row=3, column=13)

        #按钮
        self.str_trans_to_md5_button = Button(
            self.window, text="保存", bg="lightblue", width=10, command=self.save_button)
        self.str_trans_to_md5_button.grid(row=4, column=13)

    #数据获得
    def get(self):

        #测试函数
        print("调用了get函数")

        # self.patient_id= self.patient_id_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_name = self.patient_name_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_gender = self.patient_gender_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_tel = self.patient_tel_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.patient_address = self.patient_address_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.disease_name = self.disease_name_Text.get(1.0, END).strip().replace("\n", "").encode()

        # self.disease_id = self.disease_id_Text.get(1.0, END).strip().replace("\n", "").encode()

        self.patient_id = self.patient_id_Entry.get()

        self.patient_name = self.patient_name_Entry.get()

        self.patient_gender = self.patient_gender_Entry.get()

        self.patient_tel = self.patient_tel_Entry.get()

        self.patient_address = self.patient_address_Entry.get()

        self.disease_name = self.disease_name_Entry.get()

        self.disease_id = self.disease_id_Entry.get()

    # #甲类传染病警告
    # def alert1(self):
    #     self.alert1_window = Tk()
    #     self.new_alert1_window = gui_alert1(self.alert1_window)
    #     self.new_alert1_window.set_new_alert1_window()
    #     self.alert1_window.mainloop()

    # #乙类传染病警告
    # def alert2(self):
    #     self.alert2_window = Tk()
    #     self.new_alert2_window = gui_alert2(self.alert2_window)
    #     self.new_alert2_window.set_new_alert2_window()
    #     self.alert2_window.mainloop()

    # #丙类传染病警告
    # def alert3(self):
    #     self.alert3_window = Tk()
    #     self.new_alert3_window = gui_alert3(self.alert3_window)
    #     self.new_alert3_window.set_new_alert3_window()
    #     self.alert3_window.mainloop()

    #数据查找

    def search_info(self):
        # self.get()
        # if self.disease_id
        pass

    #数据保存
    def save(self):

        #测试代码
        print("调用了save函数")
        self.get()

        #创建新病人
        self.patient = patient()
        self.patient.id = self.patient_id
        self.patient.name = self.patient_name
        self.patient.address = self.patient_address
        self.patient.gender = self.patient_gender
        self.patient.tel = self.patient_tel
        self.patient.disease_id = self.disease_id
        self.patient.disease_name = self.disease_name

        self.patient.showinfo()
        self.patient.saveinfo()

    def save_button(self):
        # if self.patient.disease_id==b'0':
            self.save()
        # elif self.disease_id=="1":
        #     self.save()
        #     self.alert1()
        # elif self.disease_id=="2":
        #     self.save()
        #     self.alert2()
        # elif self.disease_id=="3":
        #     self.save()
        #     self.alert3()


class gui_print_window():
    #打印窗口初始化
    def __init__(self, new_print_window):
        self.window = new_print_window
        #导入excel数据
        self.data = xlrd.open_workbook('patients.xls')
        self.table = self.data.sheet_by_index(0)

    #设置窗口属性
    def set_new_print_window(self):
        #测试函数
        print("调用了set_new_print_window函数")

        #设置标题
        self.window.title("Patient")

        #标签
        self.search_label = Label(self.window, text="输入病人ID")
        self.search_label.grid(row=0, column=0)
        self.result_label = Label(self.window, text='查找结果')
        self.result_label.grid(row=0, column=15)

        #文本框
        self.id_Text = Text(self.window, width=10, height=5)
        self.id_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_Text = Text(self.window, width=30, height=5)
        self.result_Text.grid(row=1, column=15, rowspan=10, columnspan=10)

        #按钮
        self.print_button = Button(
            self.window, text="打印", bg="lightblue", width=10, command=self.info_print)
        self.print_button.grid(row=1, column=11)

    def info_search(self):
        src = self.id_Text.get(1.0, END).strip().replace("\n", "").encode()
        int_src = int(src)

        a = True
        i = 1
        while a:
            if int(self.table.cell(i, 0).value) == int_src:
                self.out = i
                print("找到了%s%s" % (self.out, self.table.cell(self.out, 0).value))
                self.patient = patient()
                self.patient.sava_a_info(self.out)
                if int(self.table.cell(self.out, 6).value) == 0:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：无" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(
                        self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
                elif int(self.table.cell(self.out, 6).value) == 1:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：甲型" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(
                        self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
                elif int(self.table.cell(self.out, 6).value) == 2:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：乙型" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(
                        self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
                elif int(self.table.cell(self.out, 6).value) == 3:
                    self.result_Text.delete(1.0, END)
                    self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：丙型" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(
                        self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
                a = False
                break
            elif int(self.table.cell(i, 0).value) != int_src and self.table.cell(i, 0).value != None:
                i = i+1
            elif self.table.cell(i, 0).value == None:
                self.result_Text.delete(1.0, END)
                self.result_Text.insert(1.0, "无此人")
                a = False
                break
            break

        #测试函数
        if src == b'10':
            print("src= %s %s" % (src, int_src))

    def info_print(self):
        self.info_search()

        # if int(self.table.cell(self.out,6).value)==0:
        #     self.result_Text.delete(1.0, END)
        #     self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：无" %(str(self.table.cell(self.out, 1).value), str(self.table.cell(self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
        # elif int(self.table.cell(self.out, 6).value) == 1:
        #     self.result_Text.delete(1.0, END)
        #     self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：甲型" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
        # elif int(self.table.cell(self.out, 6).value) == 2:
        #     self.result_Text.delete(1.0, END)
        #     self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：乙型" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))
        # elif int(self.table.cell(self.out, 6).value) == 3:
        #     self.result_Text.delete(1.0, END)
        #     self.result_Text.insert(1.0, "姓名：%s性别：%s联系电话：%s家庭住址：%s疾病：%s传染性：丙型" % (str(self.table.cell(self.out, 1).value), str(self.table.cell(self.out, 2).value), str(self.table.cell(self.out, 3).value), str(self.table.cell(self.out, 4).value), str(self.table.cell(self.out, 5).value)))

        # self.patient=patient()
        # self.patient.sava_a_info(self.out)
        # workbook_=lw('patients.xls')
        # sheetnames=workbook_.get_sheet_names()
        # sheet=workbook_.get_sheet_by_name(sheetnames[0])
        # sheet.cell(row=,column=).value=""

        # workbook = xlrd.open_workbook('patients.xls')
        # workbooknew = copy(workbook)
        # ws = workbooknew.get_sheet(0)
        # #测试bug
        # ws.write(1,0,'ds')
        # workbooknew.save('patients.xls')

        # ws.write(self.out, 0, self.table.cell(self.out, 0))
        # ws.write(self.out, 1, self.table.cell(self.out, 1))
        # ws.write(self.out, 2, self.table.cell(self.out, 2))
        # ws.write(self.out, 3, self.table.cell(self.out, 3))
        # ws.write(self.out, 4, self.table.cell(self.out, 4))
        # ws.write(self.out, 5, self.table.cell(self.out, 5))
        # ws.write(self.out, 6, self.table.cell(self.out, 6))

        # if int(self.table.cell(self.out, 6).value)== 0:
        #     workbook = xlrd.open_workbook('patients.xls')
        #     workbooknew = copy(workbook)
        #     ws = workbooknew.get_sheet(1)
        #     ws.write(self.out, 0, self.table.cell(self.out, 0))
        #     ws.write(self.out, 1, self.table.cell(self.out, 1))
        #     ws.write(self.out, 2, self.table.cell(self.out, 2))
        #     ws.write(self.out, 3, self.table.cell(self.out, 3))
        #     ws.write(self.out, 4, self.table.cell(self.out, 4))
        #     ws.write(self.out, 5, self.table.cell(self.out, 5))
        #     ws.write(self.out, 6, self.table.cell(self.out, 6))
        #     ws.write(self.out, 7, '无传染性')
        #     workbooknew.save('patients.xls')
        # elif int(self.table.cell(self.out, 6).value)== 1:
        #     workbook = xlrd.open_workbook('patients.xls')
        #     workbooknew = copy(workbook)
        #     ws = workbooknew.get_sheet(1)
        #     ws.write(self.out, 0, self.table.cell(self.out, 0))
        #     ws.write(self.out, 1, self.table.cell(self.out, 1))
        #     ws.write(self.out, 2, self.table.cell(self.out, 2))
        #     ws.write(self.out, 3, self.table.cell(self.out, 3))
        #     ws.write(self.out, 4, self.table.cell(self.out, 4))
        #     ws.write(self.out, 5, self.table.cell(self.out, 5))
        #     ws.write(self.out, 6, self.table.cell(self.out, 6))
        #     ws.write(self.out, 7, '甲型传染病')
        #     workbooknew.save('patients.xls')
        # elif int(self.table.cell(self.out, 6).value) == 2:
        #     workbook = xlrd.open_workbook('patients.xls')
        #     workbooknew = copy(workbook)
        #     ws = workbooknew.get_sheet(1)
        #     ws.write(self.out, 0, self.table.cell(self.out, 0))
        #     ws.write(self.out, 1, self.table.cell(self.out, 1))
        #     ws.write(self.out, 2, self.table.cell(self.out, 2))
        #     ws.write(self.out, 3, self.table.cell(self.out, 3))
        #     ws.write(self.out, 4, self.table.cell(self.out, 4))
        #     ws.write(self.out, 5, self.table.cell(self.out, 5))
        #     ws.write(self.out, 6, self.table.cell(self.out, 6))
        #     ws.write(self.out, 7, '乙型传染病')
        #     workbooknew.save('patients.xls')
        # elif int(self.table.cell(self.out, 6).value) == 3:
        #     workbook = xlrd.open_workbook('patients.xls')
        #     workbooknew = copy(workbook)
        #     ws = workbooknew.get_sheet(1)
        #     ws.write(self.out, 0, self.table.cell(self.out, 0))
        #     ws.write(self.out, 1, self.table.cell(self.out, 1))
        #     ws.write(self.out, 2, self.table.cell(self.out, 2))
        #     ws.write(self.out, 3, self.table.cell(self.out, 3))
        #     ws.write(self.out, 4, self.table.cell(self.out, 4))
        #     ws.write(self.out, 5, self.table.cell(self.out, 5))
        #     ws.write(self.out, 6, self.table.cell(self.out, 6))
        #     ws.write(self.out, 7, '丙型传染病')
        #     workbooknew.save('patients.xls')

        # workbooknew.save('patients.xls')


class gui_about():
    def __init__(self, about_window):
        self.window = about_window

    def set_about_window(self):
        self.window.title("About")

        self.about_Text = Text(self.window, width=100, height=50)
        self.about_Text.grid(row=1, column=15, rowspan=10, columnspan=10)

        self.about_Text.delete(1.0, END)
        self.about_Text.insert(1.0, "@Author: Chen Ziyu\n@version: 3.0\n@Date: 2018/05/29 / 22: 45\n@Blog: https://github.com/yakumorainy\n@License: Copyright © 2018 < copyright holders > \n\n Permission is hereby granted, free of charge, to any person \n obtaining a copy of this software and associated documentation\n files(the “Software”), to deal in the Software without\n restriction, including without limitation the rights to use,\n copy, modify, merge, publish, distribute, sublicense, and/or \nsell copies of the Software, and to permit persons to whom the \n Software is furnished to do so, subject to the following\n conditions:\n\n The above copyright notice and this permission notice shall be\n included in all copies or substantial portions of the\n Software.\n\n THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY\n KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE \nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR \nPURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\n COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR\n OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE \nSOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")


class gui_root():
    #初始化
    def __init__(self, ims_window):
        self.window = ims_window

    #设置窗口属性
    def set_ims_window(self):
        #设置窗口名
        self.window.title("Infection Monitoring System")

        self.menubar = Menu(self.window)
        #创建下拉菜单Patients,然后将其加入到顶级的菜单栏中
        self.patientmenu = Menu(self.menubar, tearoff=0)
        #创建新的病人信息窗口
        self.patientmenu.add_command(label="New", command=self.new_window)
        self.patientmenu.add_command(label="Print", command=self.print_window)
        self.patientmenu.add_command(label="Exit", command=self.window.quit)
        self.menubar.add_cascade(label="Patients", menu=self.patientmenu)

        #创建下拉菜单Diseases,然后将其加入到顶级的菜单栏中
        self.diseasemenu = Menu(self.menubar, tearoff=0)
        self.diseasemenu.add_command(label="New", command=self.new_disease)
        self.diseasemenu.add_command(
            label="Search", command=self.search_window)
        self.menubar.add_cascade(label="Disease", menu=self.diseasemenu)

        #创建下拉菜单Help,然后将其加入到顶级的菜单栏中
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        #显示菜单
        self.window.config(menu=self.menubar)

    ##所需函数
    #测试函数

    def hello(self):
        print('hello')

    #版权说明函数
    def about_test(self):
        print("Developer: Chen Ziyu")
        print("MIT Lisence")

    # #创建病人控制台输入
    # def new_patient(self):
    #     self.new_patient=patient()
    #     self.patient_id_lablelself.new_patient.get_id()
    #     self.patient_name_label=self.new_patient.get_name()
    #     self.patient_gender_label=self.new_patient.get_gender()
    #     self.patient_address=self.new_patient.get_address()
    #     self.patient_telphone=self.new_patient.get_tel()

    #创建新病人窗口

    def new_window(self):
        self.new_window = Tk()
        self.new_patient_window = gui_new_patient(self.new_window)
        self.new_patient_window.set_new_patient_window()
        self.new_window.mainloop()

    #创建新疾病窗口
    def new_disease(self):
        self.new_disease = Tk()
        self.new_disease_window = gui_new_disease(self.new_disease)
        self.new_disease_window.set_new_disease_window()
        self.new_disease.mainloop()

    #创建打印窗口
    def print_window(self):
        self.print_window = Tk()
        self.new_print_window = gui_print_window(self.print_window)
        self.new_print_window.set_new_print_window()
        self.print_window.mainloop()

    #创建疾病查找窗口
    def search_window(self):
        self.search_window = Tk()
        self.new_search_window = gui_print_disease(self.search_window)
        self.new_search_window.set_new_print_disease()
        self.search_window.mainloop()

    #创建About窗口
    def about(self):
        self.about_window = Tk()
        self.new_about_window = gui_about(self.about_window)
        self.new_about_window.set_about_window()
        self.about_window.mainloop()


def gui_start():
    #实例化一个窗口
    ims_window = Tk()
    ims = gui_root(ims_window)
    #设置根窗口默认属性
    ims.set_ims_window()
    #父窗口进入事件循环
    ims_window.mainloop()


gui_start()
