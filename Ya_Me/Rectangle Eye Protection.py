import time
import time as Time
import tkinter
import pyautogui
import tkinter as tk
import cv2
import threading

#---EAR Algorithm--------
import dlib
import imutils
import argparse
import numpy as np
from imutils import face_utils
from scipy.spatial import distance as dist

# Not To Use VideoStream ▶VideoCaputer
# from imutils.video import videostream
# from imutils.video import FileVideoStream

#카메라 설정 ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
def Camera_Function():
    capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    capture.set(cv2.CAP_PROP_FPS,15)

    while 1:
        ret, frame = capture.read()
        if not ret:
            break

        frame = cv2.flip(frame,1) # 좌우 대칭 하고 싶음.
        frame = imutils.resize(frame, width=320)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        rects=detector(gray,0)
        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            global COUNTER, TOTAL
            if ear < EYE_AR_THRESH: # ear 값을 만족하지 못하면, Counter를 높인다 → 노이즈 방지 대책
                COUNTER += 1
            else: # 만족 못한 프레임이 3개 이상이면, Blink 갯수인 TOTAL을 높인다. → 노이즈 방지 대책
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    TOTAL += 1
                    COUNTER = 0 # 이후 프레임 COUNTER를 초기화 한다.
            # 해당 구문이 없으면, 1Frame 당 Blink가 엄청 많아 지기 때문에 3Frame을 Thresold Counter로 했다.

            cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("VideoFrame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): # 굳이 창 업데이트 및 키보드가 필요 없음.
            break

    capture.release()
    cv2.destroyAllWindows()


# Event Handelr, 매 시간 마다
def delayed_function():
    root.attributes('-topmost', True)
    root.focus_force() # Focus 오류는 regedit 및 서비스를 통해서 수정이 가능함.
    root.focus_set() # set 오류는 regedit 및 서비스를 통해서 수정이 가능함.
    root.after(5000,delayed_function)

# EAR Definition ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1],eye[5])
    B = dist.euclidean(eye[2],eye[4])
    C= dist.euclidean(eye[0],eye[3])
    ear = (A+B) / (2.0 * C)
    return ear


EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 5 # 5프레임 동안 Thresold 조건을 확인하기 위함. ← 노이즈 방지 가능.
global COUNTER, TOTAL
COUNTER = 0
TOTAL = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


# Time Definition ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
def Time_Function(Start_Count = 0, MaxCalls = 2440):
    time.sleep(10) # 60초에 한 번씩 실행
    global TOTAL
    if TOTAL <= 5:
        print("눈을 깜빡이세요 용사님!")
        Window_Function()
    TOTAL = 0
    if Start_Count +1 >= MaxCalls:
        return
    Time_Function(Start_Count +1, MaxCalls)



# Tkinter ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

# Monitor Size Return

def Window_Function():
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
    # root.after(5000,delayed_function)
    root.mainloop()


Camera_Function_Value = threading.Thread(target=Camera_Function)
Camera_Function_Value.start()
Time_Function_Value = threading.Thread(target=Time_Function)
Time_Function_Value.start()
Window_Function_Value = threading.Thread(target=Window_Function)
Window_Function_Value.start()

