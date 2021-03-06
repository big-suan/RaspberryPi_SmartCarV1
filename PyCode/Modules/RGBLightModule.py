###################################################
#               智能小车1.0 -- RGB七彩灯模块
#
#               @author chenph
#               @date 2018/5/15
###################################################

import RPi.GPIO as GPIO
import time


class RGBLightModule:

    # 初始模块
    def __init__(self, PIN_R, PIN_G, PIN_B):
        print('RGBLight Module In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN_R = PIN_R
        self.PIN_G = PIN_G
        self.PIN_B = PIN_B
        GPIO.setup(self.PIN_R, GPIO.OUT)
        GPIO.setup(self.PIN_G, GPIO.OUT)
        GPIO.setup(self.PIN_B, GPIO.OUT)

        self.pwmR = GPIO.PWM(self.PIN_R, 70)
        self.pwmG = GPIO.PWM(self.PIN_G, 70)
        self.pwmB = GPIO.PWM(self.PIN_B, 70)

        self.pwmR.start(0)
        self.pwmG.start(0)
        self.pwmB.start(0)

    # 开灯
    def turnOn(self):
        self.pwmR.ChangeDutyCycle(0)
        self.pwmG.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(100)

    # 关灯
    def turnOff(self):
        self.pwmR.stop()
        self.pwmG.stop()
        self.pwmB.stop()
