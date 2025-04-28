import time as time
import matplotlib.pyplot as plt
import numpy as np
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
me = []

starttime = time.time()

def binar(a):
    return [int(i) for i in format(a, '08b')]

def adc():
    for a in range(256):
        GPIO.output(dac, binar(a))
        time.sleep(0.005)
        if GPIO.input(comp) == 1:
           return a
    return 255


try:
    GPIO.output(troyka, 1)
    while adc() < 174:
        V = adc()
        print(V)
        me.append(V)
    
        

    GPIO.output(troyka, 0)
    while adc() > 33:
        V = adc()
        print(V)
        me.append(V)

    endtime = time.time()
    duringtime = endtime - starttime
    md = [str(i) for i in me]
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(md))
    mid = len(me)/duringtime
    step = 3.3/255
    with open('settings.txt', 'w') as f:
        f.write(f'средняя частота дискретизации:{mid}\шаг квантования:{step}\n')
        print(f'средняя частота дискретизации:{mid}\шаг квантования:{step}\время:{duringtime}\период:{1/mid}\n')

except Exception as e:
    print(f'Ошибка: {e}')

finally:
    GPIO.cleanup()


print(me)
plt.plot(me)
plt.show()