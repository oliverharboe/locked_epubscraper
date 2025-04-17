import pyautogui
from fpdf import FPDF
import time
import os
# Opret et Word dokument
pdf = FPDF()

# Antal screenshots du vil tage

antal_screenshots = int(input("Hvor mange sider? "))
_ = input("Tryk enter for at starte ")
for i in range(7):
    print(f'starter om {7-i} sekunder')
    time.sleep(1)
for i in range(antal_screenshots):
    # Tag et screenshot og gem midlertidigt
    screenshot_path = f"screenshot_{i}.png"
    screenshot = pyautogui.screenshot(region=(500, 100, 1300,1100 ))
    screenshot.save(screenshot_path)

    # Tilføj screenshot til Word dokumentet
    
    pdf.add_page()
    pdf.image(screenshot_path, x=0, y=7, w=pdf.w, h=pdf.h-100)
    
    # Vent før næste screenshot
    pyautogui.click(2100,645)
    time.sleep(0.1)  # vent 2 sekunder, kan justeres

    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
# Gem dokumentet
pdf.output("screenshot_pdf.pdf")
print("Alle screenshots gemt og dokumentet er klar!")
