import pyautogui
import time

# # Tìm biểu tượng chrome
coors = pyautogui.locateOnScreen('img\\chrome.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))

# # Gõ facebook
pyautogui.hotkey('alt', 'd')
pyautogui.write("facebook.com")
pyautogui.press('enter')
time.sleep(5)


# Chọn thanh gõ trên fb
coors_2 = pyautogui.locateOnScreen('img\\search.png', grayscale=True,confidence=0.7 )
coors_center_2 = pyautogui.center(coors_2)
pyautogui.click((coors_center_2.x), (coors_center_2.y))
time.sleep(2)       
pyautogui.write('Xin Chao K63!', interval=0)
time.sleep(2)       
# Nhấn vào nút đăng
coors_3 = pyautogui.locateOnScreen('img\\post.png', grayscale=True,confidence=0.7 )
coors_center_3 = pyautogui.center(coors_3)
pyautogui.click((coors_center_3.x), (coors_center_3.y))