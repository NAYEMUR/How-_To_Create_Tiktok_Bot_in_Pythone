#How to creat a Tiktok bot using python
import pyautogui
import time
pyautogui.FAILSAFE = False
pyautogui.moveTo(63,758,2)#go to search ber
pyautogui.click()

pyautogui.typewrite('google chrome',.25) # type and search google chrome
pyautogui.press('enter')
time.sleep(4)

pyautogui.typewrite(' https://www.tiktok.com',.25) #enter web link in search bar
pyautogui.press('enter')
time.sleep(2)

pyautogui.moveTo(736, 342, 2) #Bot will go to watch now
pyautogui.click()

pyautogui.moveTo(107,250, 2)#Bot will go to following
pyautogui.click()

pyautogui.moveTo(561,395, 4) #Bot will go to video
pyautogui.click()

for x in range(0,5): #how many video i want to see.suppose i want to see 5 video.you can adjust increase or decrease the range
    time.sleep(10) #watch video for 10 sec .you can change as you want
    pyautogui.moveTo(561, 395,1 )  # like video
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(761,395,1) #play next video
    pyautogui.click()

pyautogui.moveTo(1358,3, 2) #Bot will close browser
pyautogui.click()