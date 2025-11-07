import time, keyboard

time.sleep(1)
while True:
    keyboard.press("e")
    time.sleep(0.4)
    keyboard.release("e")
    keyboard.press("space")
    time.sleep(0.01)
    keyboard.release("space")
    time.sleep(0.05)
