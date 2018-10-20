from tkinter import *
from disease import *
from patient import *
from about import *


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
