import os
import keyboard
import time
import winsound
from PIL import ImageGrab

# 设置截图保存路径
save_path = r'D:\download\mysnap'

# 创建保存文件夹（如果不存在）
if not os.path.exists(save_path):
    os.makedirs(save_path)

def capture_and_save_screen(e):
    # 获取屏幕截图
    screenshot = ImageGrab.grab()

    # 生成唯一的文件名
    timestamp = int(time.time())
    filename = os.path.join(save_path, f'screenshot_{timestamp}.png')

    # 保存截图
    screenshot.save(filename)
    print(f'Screenshot saved as {filename}')
    # 播放默认的系统提示音
    winsound.Beep(1000, 100) 


# 监听“Print Screen”键
keyboard.on_press_key('Print Screen', capture_and_save_screen)

print('Press the "Print Screen" key to capture and save a screenshot.')
keyboard.wait('esc')  # 持续监听，直到按下Esc键
