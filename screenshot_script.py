import pyautogui
from fpdf import FPDF
import time
import os
pdf = FPDF()


antal_screenshots = int(input("Pages in the ebook: "))
_ = input("Enter to start the 7sec countdown ")
for i in range(7):
    print(f'starting in {7-i} seconds')
    time.sleep(1)
for i in range(antal_screenshots):
    screenshot_path = f"screenshot_{i}.png"
    screenshot = pyautogui.screenshot(region=(500, 100, 1300,1100 ))
    screenshot.save(screenshot_path)

    
    pdf.add_page()
    pdf.image(screenshot_path, x=0, y=7, w=pdf.w, h=pdf.h-100)
    
    pyautogui.click(2100,645)
    time.sleep(0.1)  

    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
# save pdf
pdf.output("screenshot_pdf.pdf")
print("Done")
