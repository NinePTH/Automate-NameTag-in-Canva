import pyautogui
import time
import pyperclip

time.sleep(1)

f = open("รายชื่อ.txt", encoding="utf-8-sig")

print(pyautogui.position())

for word in f:
    time.sleep(1)
    pyautogui.click(x=1156, y=271) #Duplicate ป้ายชื่อ
    time.sleep(1)

    pyautogui.doubleClick(x=996, y=736) #คลิกแก้ชื่อ
    time.sleep(1)
    pyperclip.copy(word)
    pyautogui.typewrite("P'")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('backspace')
