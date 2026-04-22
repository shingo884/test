import subprocess
import time
import pyautogui
import pyperclip
import os

def copy_data(input_path,output_path,day_list,):
    pass

def process_tool(input_path,output_path):
    
    os.makedirs(output_path,exist_ok=True)
    
    exe_path = r"C:\Users\s-hayashi\Documents\Dev\tool\動画変換ツール_全自動\pcap2mp4_frontend.exe"

    subprocess.Popen(exe_path)
    time.sleep(2)
    pyperclip.copy(output_path)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyperclip.copy(input_path)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab', presses=20)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab', presses=6)
    time.sleep(1)
    pyautogui.press('enter')


if __name__ == "__main__":

    # copy_data() 
    input_path = r"T:\S-hayashi\2026\QQ\動画変換ツール\data"
    output_path = r"T:\S-hayashi\2026\QQ\動画変換ツール\result"
    process_tool(input_path,output_path)