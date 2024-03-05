import time
import keyboard
from PIL import ImageGrab

def screenshot():
    current_time = time.strftime("_%Y%m%d_%h%m%s")
    img = ImageGrab.grab()
    img.save("image{}.png".format((current_time)))

keyboard.add_hotkey("F9",screenshot)

keyboard.wait("esc") # 사용자가 esc를 누를때까지 프로그램 수행


time.sleep(5)

for i in range(1,11):
    img = ImageGrab.grab() # 현재 스크린의 이미지를 가져옴.
    img.save("Image{}.png".format(i)) # 파일 저장
    time. sleep(2)
