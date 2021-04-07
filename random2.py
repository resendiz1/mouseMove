import random
import pyautogui

for contador  in range(1,100):

    a = random.randrange(10, 900)
    b = random.randrange(10,900)

    pyautogui.moveTo(int(a),int(b))

    print('El mouse a sido movido a los ejes y= ',a,' y al eje x= ',b,' ')