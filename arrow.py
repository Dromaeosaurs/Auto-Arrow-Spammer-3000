from time import sleep
import pyautogui
pyautogui.FAILSAFE = False
while 1==1:
    ss = pyautogui.screenshot ()
    on = ss.getpixel ((787,1063))
    print (on)
    if on == (135,102,39):
        pyautogui.mouseDown(0,0,button="right",duration=0.8)
        sleep (0.9)
        pyautogui.click(0,0,button="right")
        sleep (0.3)
        print ("sex")
    else:
        print ("kurwa zjebało sie")
        sleep (1)