import os.path
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("Imager Combiner")

# 파일 추가 def
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일은 선택하세요.", \
                                        filetypes=(("PNG 파일", "*.png"),("모든파일","*.*"),), \
                                        initialdir=r"C:\Users\Sim\Documents\Github\CodingTest_Study\NADO CODING",\
                                        ) # 최초 경로를 보여줌.
    #print(files, type(files))
    # 사용자가 선택한 파일 목록을 출력.
    print(files)
    print('--------------------------------------------------------------------------------------')

    for file in files:
        list_file.insert(END, file) # END, 부터 하면 순서대로 , 0부터 하면 역순으로

def del_file():
    print(list_file.curselection())
    #지우는건 역으로 인덱스를 지운다.
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로(폴더) 선택
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "": #폴더를 선택 안한다면
        return
    print(folder_selected)
    txt_dest_path.delete(0,END) #우선은 초기화 하는 느낌으로.
    txt_dest_path.insert(0,folder_selected)
    pass

def start():
    # print("가로넓이 : ",cmb_width.get())
    # print("간격넓이 : ", cmb_space.get())
    # print("포맷 : ", cmb_foramt.get())

    # 파일 목록 확인
    if list_file.size() ==0:
        msgbox.showwarning("경고","이미지 파일이 없어요.")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장경로를 선택하세요.")
        return

    merge_image()

#이미지 통합
def merge_image():
    # print("가로넓이 : ",cmb_width.get())
    # print("간격넓이 : ", cmb_space.get())
    # print("포맷 : ", cmb_foramt.get())

    # 가로 넓이 옵션
    img_width = cmb_width.get() #여기는 문자형 1024, 240 이런거임
    if img_width == "원본유지":
        img_width = -1 # -1일때는 원본 기준으로 이미지를 통합
    else:
        img_width = int(img_width) #숫자로 바꿔야함.

    # 간격 넓이 옵션
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 60
    elif img_space == "넓게":
        img_space = 90
    else:
        img_space = 0

    # 포맷
    img_format = cmb_foramt.get().lower() # PNG, JPG, BMP 값을 가져와서 소문자로 변경

    #########################################################################################################

    #print(list_file.get(0,END)) # 모든 파일 목록을 가져온다.
    images = [Image.open(x) for x in list_file.get(0,END)] # 이 IMAGE 에는 SIZE 정보가 포함

    # 이미지 사이즈 리스트에 넣어서 하나씩 처리
    image_sizes = [] # [(width1, height1), (width2, height2) ~ ]
    if img_width > -1:
        image_sizes = [(int(img_width),int(img_width * x.size[1]/x.size[0])) for x in images]
        pass # width 값 변경
    else:
        # 원본사이즈 사용
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    # 100*60 이미지가 있음을, width를 80으로 줄인다면 height?

    # 각 파일 중 가장 가로 사이즈가 큰 친구를 기준으로
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]

    # [(10, 10), (20, 20), (30, 30)]
    # widths, heights = zip(*(x.size for x in images)) #(x.size ~ unzip)
    widths, heights = zip(*(image_sizes))
    # 각 파일의 인덱스는 0은 가로, 1은 세로라서
    # print(widths)
    # print(heights)
    max_width, total_height = max(widths),sum(heights)
    print(max_width)
    print(total_height)

    if img_space >0:
        total_height += (img_space * (len(images)-1))

    result_img = Image.new("RGB",(max_width,total_height),(255,255,255))
    y_offset = 0 # y 위치 정보
    # for img in images:
    #     result_img.paste(img,(0,y_offset))
    #     y_offset=img.size[1] + y_offset
    for idx, img in enumerate(images):
        # width가 원본이 아니라면, 크기 조정이 필요하다.
        if img_width > -1:
            img = img.resize(image_sizes[idx])

        result_img.paste(img,(0,y_offset))
        y_offset = (y_offset+img.size[1] + img_space) # height + 사용자 지정 간격

        progress = (idx +1) / len(images) * 100 # 실제 퍼센트 정보 계산
        p_var.set(progress)
        progress_bar.update()

    file_name = "nado_photo." + img_format
    dest_path = os.path.join(txt_dest_path.get(), file_name)
    result_img.save(dest_path)
    msgbox.showinfo("알림","작업 완료")

#파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5, pady=5) #간격 뛰우기


btn_add_file = Button(file_frame,padx=5,pady=5, width=12,text="파일 추가",command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5,pady=5, width=12,text="파일 삭제",command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both",expand=True)
scrollbar.config(command=list_file.yview)


#저장경로 Frame
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x",padx=5, pady=5,ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",expand = True,ipady=4,padx=5, pady=5) # ipad 높이 조금 조정

btn_dest_path = Button(path_frame,text="찾아보기",width=10,padx=5, pady=5,command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5,ipady=5)

# 가로 넓이 옵션
width_label = Label(option_frame,text="가로 넓이", width=8)
width_label.pack(side="left")

option_width = ["원본유지", "1024","800","640"]
cmb_width = ttk.Combobox(option_frame,state="readonly",values=option_width)
cmb_width.current(0)
cmb_width.pack(side="left")

# 간격 옵션
space_label = Label(option_frame,text="간격",width=8)
space_label.pack(side="left",padx=5, pady=5)

option_space = ["좁게","중간","넓게"]
cmb_space = ttk.Combobox(option_frame,state="readonly",values=option_space)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5, pady=5)


# 파일 포맷 옵션
format_label = Label(option_frame,text="옵션",width=8)
format_label.pack(side="left",padx=5, pady=5)

option_foramt = ["PNG","JPG","BMP"]
cmb_foramt = ttk.Combobox(option_frame,state="readonly",values=option_foramt)
cmb_foramt.current(0)
cmb_foramt.pack(side="left",padx=5, pady=5)

# 진행 상황 Progress Bar
progress_frame = LabelFrame(root, text="진행사항")
progress_frame.pack(fill= "x",padx=5, pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame,maximum=100,variable=p_var)
progress_bar.pack(fill="x",padx=5, pady=5)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x",padx=5, pady=5)

btn_close = Button(run_frame,padx=5,pady=5,text="닫기",width=12,command=root.quit())
btn_close.pack(side="right",padx=5, pady=5)

btn_start = Button(run_frame,padx=5, pady=5, text="시작", width =12,command=start)
btn_start.pack(side="right",padx=5, pady=5)


root.resizable(1, 1)
root.mainloop()
