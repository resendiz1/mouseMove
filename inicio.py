import pyautogui
import random

print('A donde lo quieres mover en la coordenada X')
a = input()

print('En el eje Y?')
b = input()

pyautogui.moveTo(int(a),int(b))

print('El mouse a sido movido a los ejes y= ',a,' y al eje x= ',b,' ')