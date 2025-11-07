import time, keyboard

time.sleep(1)
while True:
    keyboard.press("e")
    time.sleep(0.4)
    keyboard.release("e")
    keyboard.press("w")
    time.sleep(0.1)
    keyboard.release("w")
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")
    time.sleep(0.05)
