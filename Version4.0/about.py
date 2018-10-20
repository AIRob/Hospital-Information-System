from tkinter import *

class gui_about():
    def __init__(self, about_window):
        self.window = about_window

    def set_about_window(self):
        self.window.title("About")

        self.about_Text = Text(self.window, width=100, height=50)
        self.about_Text.grid(row=1, column=15, rowspan=10, columnspan=10)

        self.about_Text.delete(1.0, END)
        self.about_Text.insert(1.0, "@Author: Chen Ziyu\n@version: 3.0\n@Date: 2018/05/29 / 22: 45\n@Blog: https://github.com/yakumorainy\n@License: Copyright © 2018 < copyright holders > \n\n Permission is hereby granted, free of charge, to any person \n obtaining a copy of this software and associated documentation\n files(the “Software”), to deal in the Software without\n restriction, including without limitation the rights to use,\n copy, modify, merge, publish, distribute, sublicense, and/or \nsell copies of the Software, and to permit persons to whom the \n Software is furnished to do so, subject to the following\n conditions:\n\n The above copyright notice and this permission notice shall be\n included in all copies or substantial portions of the\n Software.\n\n THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY\n KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE \nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR \nPURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\n COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR\n OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE \nSOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
