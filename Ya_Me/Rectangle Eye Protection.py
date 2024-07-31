# 1. 먼저 투명한 창을 만들고, 시간 마다 빨간색으로 테두리를 변경하고 가운데에 그림이 나타나게 한다.
# 2. 눈이랑 이런 깜빡이를 조금 둬서, 추가로 거시기 하게 한다.
# 3.
import time as Time
import tkinter
import pyautogui
import tkinter as tk
import cv2
import threading

xml = 'C:/Users/Sim/Documents/GitHub/ETC/Ya_Me/HaarCascade_Xml/haarcascade_frontalface_alt.xml'
face_Cascade = cv2.CascadeClassifier(xml)


#-------------------------------------------OpenCV 부문
def Camera_Function():
    capture = cv2.VideoCapture(1)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    capture.set(cv2.CAP_PROP_FPS,15)

    while 1:
        ret, frame = capture.read()
        frame = cv2.flip(frame,1) # 좌우 대칭 하고 싶음.
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face = face_Cascade.detectMultiScale(gray,1.05,5)

        if len(face):
            for (x,y,w,h) in face:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if ret:
            cv2.imshow("VideoFrame",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): # 굳이 창 업데이트 및 키보드가 필요 없음.
                 break

    capture.release()
    cv2.destroyAllWindows()

#-------------------------------------------OpenCV 부문

# Monitor Size Return
Monitor_Size = pyautogui.size()
Monitor_Height = Monitor_Size[1] # int형
Monitor_Width = Monitor_Size[0] # int 형


root = tk.Tk()
# root.geometry(f"+{Monitor_Width}+{Monitor_Height}") # f문자열 포맷팅
root.geometry("1920x1080")
root.attributes('-topmost',True)# 제일 상단
#root.attributes('-fullscreen',True) # Full Screen
root.attributes('-alpha',1)

#1번 Frame Border 테두리 용
Border_Color = "red"
Border_Width = 5
Border_frame = tk.Frame(root, bg=Border_Color,width=Monitor_Width,height=Monitor_Height)
Border_frame.pack_propagate(False) # Frame의 크기를 고정
Border_frame.pack(padx=Border_Width,pady=Border_Width)

Border_Frame2 = tk.Frame(Border_frame, bg="white",width=Monitor_Width-10,height=Monitor_Height-10)
Border_Frame2.pack_propagate(False) # Frame의 크기를 고정
Border_Frame2.pack(padx=Border_Width,pady=Border_Width)

#이미지 처리 및 출력 관련 부분
Image = tk.PhotoImage(file="C:/Users/Sim/Documents/GitHub/ETC/Ya_Me/Cho Rong.png")
Image_Width = Image.width()
Image_Height = Image.height()
Image_Frame = tk.Frame(Border_Frame2, bg="white",width=Monitor_Width-10,height=Monitor_Height-10)
Image_Frame.pack()
label = tk.Label(Image_Frame,image=Image)
label.place(x=(Monitor_Width-10 - Image_Width)//2,y=(Monitor_Height-10-Image_Height)//2)
# label.pack()  Label.Place와 pack은 충돌 메서드임. 하나만 사용하자.


# Event Handelr, 매 시간 마다
def delayed_function():
    root.attributes('-topmost', True)
    root.focus_force() # Focus 오류는 regedit 및 서비스를 통해서 수정이 가능함.
    root.focus_set() # set 오류는 regedit 및 서비스를 통해서 수정이 가능함.
    root.after(5000,delayed_function)

root.after(5000,delayed_function)

Camera_Function_Value = threading.Thread(target=Camera_Function)
Camera_Function_Value.start()

root.mainloop()