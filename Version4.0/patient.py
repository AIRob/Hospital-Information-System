import xlrd
import xlwt
from xlutils.copy import copy
from tkinter import *

global_col = 1

patientsinfo = xlwt.Workbook(encoding='ascii')


patient_info = patientsinfo.add_sheet('patients')
one_patient_info = patientsinfo.add_sheet('the patient')


patient_info.write(0, 0, label='ID')
patient_info.write(0, 1, label='姓名')
patient_info.write(0, 2, label='性别')
patient_info.write(0, 3, label='电话')
patient_info.write(0, 4, label='地址')
patient_info.write(0, 5, label='疾病')
patient_info.write(0, 6, label='疾病ID')

one_patient_info.write(0, 0, label='ID')
one_patient_info.write(0, 1, label='姓名')
one_patient_info.write(0, 2, label='性别')
one_patient_info.write(0, 3, label='电话')
one_patient_info.write(0, 4, label='地址')
one_patient_info.write(0, 5, label='疾病')
one_patient_info.write(0, 6, label='疾病ID')
one_patient_info.write(0, 7, label='传染性')

patientsinfo.save('patients.xls')



class patient():

    def __init__(self):
        print("创建病人类")

    def showinfo(self):
        print("病人信息如下 \n ID：%s \n 姓名：%s ，性别：%s ； \n 电话：%s ， 地址：%s \n 疾病： %s ，疾病ID：%s" % (
            self.id, self.name, self.gender, self.tel, self.address, self.disease_name, self.disease_id))

    def saveinfo(self):
        global global_col

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

        self.patient_id = self.patient_id_Entry.get()

        self.patient_name = self.patient_name_Entry.get()

        self.patient_gender = self.patient_gender_Entry.get()

        self.patient_tel = self.patient_tel_Entry.get()

        self.patient_address = self.patient_address_Entry.get()

        self.disease_name = self.disease_name_Entry.get()

        self.disease_id = self.disease_id_Entry.get()

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
            self.save()


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
