from gui_root import *
from tkinter import *

def gui_start():
    #实例化一个窗口
    ims_window = Tk()
    ims = gui_root(ims_window)
    #设置根窗口默认属性
    ims.set_ims_window()
    #父窗口进入事件循环
    ims_window.mainloop()


gui_start()
