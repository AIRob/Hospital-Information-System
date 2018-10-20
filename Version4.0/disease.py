import xlrd
import xlwt
from xlutils.copy import copy
from tkinter import *

global_coll = 1


diseasesinfo = xlwt.Workbook(encoding='ascii')

disease_info = diseasesinfo.add_sheet('diseases')

disease_info.write(0, 0, label='ID')
disease_info.write(0, 1, label='疾病')
# disease_info.write(0,2,label='传染性')

diseasesinfo.save('diseases.xls')



class disease():
    def __init__(self):
        print("创建疾病类")

    def saveinfo(self):
        global global_coll

        workbook = xlrd.open_workbook('diseases.xls')
        workbooknew = copy(workbook)
        ws = workbooknew.get_sheet(0)

        ws.write(global_coll, 0, self.id)
        ws.write(global_coll, 1, self.name)

        workbooknew.save('diseases.xls')

        global_coll = global_coll+1


class gui_print_disease():

    def __init__(self, new_print_disease):
        self.window = new_print_disease

        self.data = xlrd.open_workbook('diseases.xls')
        self.table = self.data.sheet_by_index(0)

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

        #按钮
        self.str_trans_to_md5_button = Button(
            self.window, text="保存", bg="lightblue", width=10, command=self.save_button)
        self.str_trans_to_md5_button.grid(row=15, column=15)

    def get(self):
        #测试函数
        print("调用了get函数")

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

        self.disease.saveinfo()

    def save_button(self):
            self.save()
