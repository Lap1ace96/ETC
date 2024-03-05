import tkinter.ttk as ttk
import time
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("NADO GUI")
root.geometry("500x500") # 가로 * 세로

# #root.resizeable(False, False) # 창 크기 변경 불가 시
# btn = Button(root, text = "버튼 1")
# btn.pack()
#
# btn2 =Button(root,padx=5, pady=10, text="버튼2")
# btn2.pack()
# #버튼 내용이 많아지면, 길이도 커진다
# btn3 =Button(root,padx=15, pady=10, text="버튼3")
# btn3.pack()
#
# btn4 = Button(root, width=10, height=3, text="버튼4")
# btn4.pack()
#
# btn5= Button(root, fg ="red",bg="yellow",text="버튼5")
# btn5.pack()
#
# photo = PhotoImage(file="img.png")
# btn6 = Button(root, image=photo)
# btn6.pack()
#
# def btncmd():
#     print("버튼이 클릭되엇어요")
#
# btn7 = Button(root, text="동작하는 버튼",command=btncmd)
# btn7.pack()

#4 -----------------------------------------------------------------------------------
# label1 = Label(root, text="안녕하세요")
# label1.pack()
#
# photo = PhotoImage(file="img.png")
# label2 = Label(root,image=photo)
# label2.pack()
#
# photo2 = PhotoImage(file="img2.png")
# def change():
#     label2.config(image=photo2)
#
# btn1 = Button(root,text="클릭",command=change)
# btn1.pack()

#5 -----------------------------------------------------------------------------------

# txt = Text(root, width=30, height=5)
# txt.pack()
#
# txt.insert(END, "글자를 입력하세요.")
#
# e = Entry(root, width="30") #한 줄로만 할 때, 여러줄에 거쳐서 데이터를 받지 않음.
# e.pack()
# e.insert(0,"한 줄만 입력하세요")
#
# def btncmd():
#     print(txt.get("1.0",END)) #1은 첫번째 행, 0은 0번째 열 위치
#     print(e.get())
#
#     txt.delete("1.0",END)
#     e.delete(0,END)
#
# btn = Button(root,text="클릭",command = btncmd)
# btn.pack()
# 6 --------------------------------------------------------------------------
#
#
#
# listbox = Listbox(root,selectmode="extended", height=3) #Height는 인덱스 갯수 출력(0은 모든 인덱스 다)
# listbox.insert(0,"사과")
# listbox.insert(1,"딸기")
# listbox.insert(2,"바나나")
# listbox.insert(END,"포도")
# listbox.pack()
#
#
# def btncmd():
#     # listbox.delete(0) #맨위에 삭제
#     # print("리스트에는",listbox.size()) #갯수 출력
#     #
#     # print("1번째 부터 3번째 까지의 항목 : ", listbox.get(0,2))
#     print("선택된 항목 : ", listbox.curselection()) #인덱스 위치로 반환함.
#
# btn = Button(root,text="클릭",command=btncmd)
# btn.pack()
# 7 ------------------------------------------------------------------------
# chkvar = IntVar()
# chkvar2 = IntVar()
#
# chkbox = Checkbutton(root, text="오늘 하루 보지 않기",variable=chkvar)
# chkbox.deselect()
# chkbox.pack()
#
# chkbox2 = Checkbutton(root, text="일주일동안 안 보기",variable=chkvar2)
# chkbox2.select()
# chkbox2.pack()
#
#
# def btncmd():
#     print(chkvar.get())# 0은 체크해제, 1은 체크
#     print(chkvar2.get())
# btn = Button(root,width=10,height=10,command=btncmd)
# btn.pack()
# 8 ---------------------------------------------------------------------------------

# label1= Label(root,text="메뉴를 선택하세요").pack()
#
# burger_var = IntVar()
# btn_burger1 = Radiobutton(root, text="햄버거", value=1,variable=burger_var)
# btn_burger2 = Radiobutton(root, text="피자", value=2,variable=burger_var)
# btn_burger3 = Radiobutton(root, text="치킨", value=3,variable=burger_var)
#
# btn_burger1.select()
#
# btn_burger1.pack()
# btn_burger2.pack()
# btn_burger3.pack()
#
#
# Label(root,text="음료를 선택하세요").pack()
# drink_var = StringVar()
# btn_drink1 = Radiobutton(root,text="콜라",value="콜라", variable=drink_var)
# btn_drink1.select()
# btn_drink2 = Radiobutton(root,text="사이다",value="사이다", variable=drink_var)
# btn_drink3 = Radiobutton(root,text="환타",value="환타", variable=drink_var)
#
# btn_drink1.pack()
# btn_drink2.pack()
# btn_drink3.pack()
# 9  ------------------------------------------------------------------------------------

# combobox는 ttk
#
# values = [str(i) + "일" for i in range(1,32)]
#
# combobox = ttk.Combobox(root, height=5, values=values)
# combobox.pack()
# combobox.set("카드 결제일")
# combobox_Readonly = ttk.Combobox(root, height=10, values=values,state="readonly") # state는 변경 불가.
# combobox_Readonly.current(0) # 0번째 인덱스 값 선택
# combobox_Readonly.pack()
#
# 10  ------------------------------------------------------------------------------------

# p_var2 = DoubleVar() # %가 정수값으로 가는게 아니라서, Double로 함.
# #progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 언제 끝날지 모를때 진행 중인걸 확인시키려면.
# progressbar2 = ttk.Progressbar(root, maximum=100,length=150, variable=p_var2)
# progressbar2.pack()
# #progressbar.start(10)
# #progressbar.pack()
#
# def btncmd():
#     progressbar2.stop()
#     pass
#
# def btncmd2():
#     for i in range(1,101):
#         time.sleep(0.01) # 0.01s 대기
#         p_var2.set(i)
#         progressbar2.update()
#         print(p_var2.get())
# btn = Button(root,text="선택",width=10,height=10,command=btncmd)
# btn.pack()
#
# btn2 = Button(root,text="시작",width=10,height=10,command=btncmd2)
# btn2.pack()
# 11---------------------------------------------------------------------------

# menu = Menu(root)
# root.config(menu=menu)
#
# def create_new_file():
#     print("새 파일을 만듭니다.")
#
# menu_file = Menu(menu,tearoff=0)
# menu_file.add_command(label="New File",command=create_new_file)
# menu_file.add_command(label="New Window")
# menu_file.add_separator()
# menu_file.add_command(label="Open File...")
# menu.add_cascade(label="File",menu=menu_file)
# menu_file.add_separator()
# menu_file.add_command(label="Save all", state="disable")
# menu_file.add_separator()
# menu_file.add_command(label="Exit", command=root.quit)
#
# # Edit mENU
#
# menu.add_cascade(label="Edit")
#
# # Language 메뉴 추가 radio 버튼을 통해서 택 1
# menu.add_cascade(label="language")
#
# menu_lang = Menu(menu,tearoff=0)
# menu_lang.add_radiobutton(label="python")
# menu_lang.add_radiobutton(label="C++")
#
# menu.add_cascade(label="language",menu=menu_lang)
#
# menu_view = Menu(menu,tearoff=0)
# menu_view.add_checkbutton(label="Show Minimap")
# menu.add_cascade(label="View",menu=menu_view)
# 12------------------------------------------------------------------------------------

# def info():
#     msgbox.showinfo("알림","정상적으로 예매 완료 되었습니다.")
# def warn():
#     msgbox.showwarning("경고","해당 좌석은 매진 되었습니다.")
# def err():
#     msgbox.showerror("에러","결제 불가")
# def okcancel():
#     msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석이다.")
# def retrycancel():
#     msgbox.askretrycancel("재시도 / 취소","핸드폰 통신 상태 확인해봐라")
# def yesno():
#     msgbox.askyesno("예  / 아니오","기가 안기가?")
# def yesnocancel():
#     response= msgbox.askyesnocancel(title=None, message="진짜로 종료할끼라?")
#     print(response)
#
#
# Button(root,command=info,text="알림").pack()
# Button(root,command=warn,text="알림").pack()
# Button(root,command=err,text="경고").pack()
# Button(root,command=okcancel,text="확인").pack()
# Button(root,command=retrycancel,text="확인").pack()
# Button(root,command=yesno,text="확인").pack()
# Button(root,command=yesnocancel,text="확인").pack()
# 12------------------------------------------------------------------------------------

# Label(root,text="메뉴를 선택해주세요").pack(side="top")
# Button(root,text="주문하기").pack(side="bottom")
# frame_burger = Frame(root,relief="solid",bd=1)
# frame_burger.pack(side="left",fill="both",expand=True)
#
# Button(frame_burger, text="햄버거").pack()
# Button(frame_burger, text="치키").pack()
# Button(frame_burger, text="치즈").pack()
#
# frame_drink = LabelFrame(root,text="음로")
# Button(frame_drink, text="콜라").pack()
# Button(frame_drink, text="사이다").pack()
# frame_drink.pack(side="right",fill="both",expand=True)

# 12--------------------------------------------------------------------------------------
#
# frame = Frame(root)
# frame.pack()
#
# scrollbar = Scrollbar(frame)
# scrollbar.pack(side="right",fill="y")
# # set이 없으면 스크롤을 내려도 다시 올라옴..
# listbox = Listbox(frame, selectmode="extended",height=10,yscrollcommand=scrollbar.set)
#
# for i in range(1,32):
#     listbox.insert(END,str(i)+ "일")
# listbox.pack()
# scrollbar.config(command=listbox.yview) # y 상하에 대한 처리가 가능함. # 매핑.

# 12----------------------------------------------------------------------------------

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)


# 13----------------------------------------------------------------

# # 맨 윗줄
# btn_F16 = Button(root,text="F16", width=5, height=2)
# btn_F17 = Button(root,text="F17",width=5, height=2)
# btn_F18 = Button(root,text="F18",width=5, height=2)
# btn_F19 = Button(root,text="F19",width=5, height=2)
#
# btn_F16.grid(row=0, column=0,sticky=N+E+W+S, padx=3, pady=3)
# btn_F17.grid(row=0, column=1,sticky=N+E+W+S, padx=3, pady=3)
# btn_F18.grid(row=0, column=2,sticky=N+E+W+S, padx=3, pady=3)
# btn_F19.grid(row=0, column=3,sticky=N+E+W+S, padx=3, pady=3)
# # Clear 줄
# btn_clear = Button(root,text="Clear",width=5, height=2)
# btn_equal = Button(root,text="=",width=5, height=2)
# btn_div = Button(root,text="/",width=5, height=2)
# btn_mul = Button(root,text="*",width=5, height=2)
#
# btn_clear.grid(row=1, column=0,sticky=N+E+W+S, padx=3, pady=3)
# btn_equal.grid(row=1, column=1,sticky=N+E+W+S, padx=3, pady=3)
# btn_div.grid(row=1, column=2,sticky=N+E+W+S, padx=3, pady=3)
# btn_mul.grid(row=1, column=3,sticky=N+E+W+S, padx=3, pady=3)
#
# btn_7 = Button(root,text="7",width=5, height=2)
# btn_8 = Button(root,text="8",width=5, height=2)
# btn_9 = Button(root,text="9",width=5, height=2)
# btn_sub = Button(root,text="-",width=5, height=2)
#
# btn_7.grid(row=2, column=0,sticky=N+E+W+S, padx=3, pady=3)
# btn_8.grid(row=2, column=1,sticky=N+E+W+S, padx=3, pady=3)
# btn_9.grid(row=2, column=2,sticky=N+E+W+S, padx=3, pady=3)
# btn_sub.grid(row=2, column=3,sticky=N+E+W+S, padx=3, pady=3)
#
# btn_4 = Button(root,text="4",width=5, height=2)
# btn_5 = Button(root,text="5",width=5, height=2)
# btn_6 = Button(root,text="6",width=5, height=2)
# btn_add = Button(root,text="+",width=5, height=2)
#
# btn_4.grid(row=3, column=0,sticky=N+E+W+S, padx=3, pady=3)
# btn_5.grid(row=3, column=1,sticky=N+E+W+S, padx=3, pady=3)
# btn_6.grid(row=3, column=2,sticky=N+E+W+S, padx=3, pady=3)
# btn_add.grid(row=3, column=3,sticky=N+E+W+S, padx=3, pady=3)
#
# btn_1 = Button(root,text="1",width=5, height=2)
# btn_2 = Button(root,text="2",width=5, height=2)
# btn_3 = Button(root,text="3",width=5, height=2)
# btn_enter = Button(root,text="enter",width=5, height=2)
#
# btn_1.grid(row=4, column=0,sticky=N+E+W+S, padx=3, pady=3)
# btn_2.grid(row=4, column=1,sticky=N+E+W+S, padx=3, pady=3)
# btn_3.grid(row=4, column=2,sticky=N+E+W+S, padx=3, pady=3)
# btn_enter.grid(row=4, column=3, rowspan=2,sticky=N+E+W+S, padx=3, pady=3) #현재 위치로 부터 아래쪽으로 1칸을 더함
#
# btn_0 = Button(root,text="0",width=5, height=2)
# btn_point = Button(root,text=".",width=5, height=2)
#
# btn_0.grid(row=5, column=0, columnspan=2,sticky=N+E+W+S, padx=3, pady=3)
# btn_point.grid(row=5, column=2,sticky=N+E+W+S, padx=3, pady=3)
#

root.mainloop()
