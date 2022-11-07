import pyautogui
import time
time.sleep(3)

text= open("songs.txt",encoding="utf8")

for each_line in text:
    pyautogui.write(each_line)




