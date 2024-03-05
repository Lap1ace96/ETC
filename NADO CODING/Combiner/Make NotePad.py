from tkinter import *
from tkinter.filedialog import *
import tkinter.ttk as ttk
import time
import tkinter.messagebox as msgbox
import sys


root = Tk()
root.title("제목 없음 - Windwos 메모장")
root.geometry("500x500") # 가로 * 세로
root.resizable(True,True)

menu = Menu(root)
root.config(menu=menu)

def create_new_file():
    file = askopenfile(mode='r',defaultextension='.txt')
    print(file)
    line = file.readline()
    txt.delete('1.0',END)
    txt.insert(INSERT,line + "\n")
    file.close()
def save_file():
    file = asksaveasfile(mode='w',defaultextension='.txt',filetypes=[('TXT (*.txt)','.txt')])
    text_data = str(txt.get(1.0,END))
    file.write(text_data)
    file.close()

def quit_file():
    quit()

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command=create_new_file)
menu_file.add_separator()
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=quit_file)
menu_file.add_separator()
menu.add_cascade(label="파일",menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")
txt = Text(root,yscrollcommand=scrollbar.set)
txt.pack(fill=BOTH,expand=True) #부모(root, 창)와 자신의 크기를 동일하게 가져간다.
scrollbar.config(command=txt.yview)




root.mainloop()
