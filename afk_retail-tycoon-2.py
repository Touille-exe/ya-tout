import time, keyboard

time.sleep(1)
while True:
    keyboard.press("e")
    time.sleep(0.5)
    keyboard.release("e")
    keyboard.press("z")
    time.sleep(0.05)
    keyboard.release("z")
    keyboard.press("s")
    time.sleep(0.05)
    keyboard.release("s")
    time.sleep(0.05)
