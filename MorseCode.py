from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)


window = Tk()
window.title("Morse Code")
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

def dot():
    GPIO.output(12,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12,GPIO.LOW)
    time.sleep(1)
    
def dash():
    GPIO.output(12,GPIO.HIGH)
    time.sleep(0.75)
    GPIO.output(12,GPIO.LOW)
    time.sleep(0.75)
    
Morse_Code= { 'A':'.-', 'B':'-...','C':'-.-.','D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....','I':'..','J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.','O':'---','P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-','U':'..-','V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..','0': '-----','1':'.----' , '2': '..---', 
            '3': '...--','4': '....-','5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', ' ': ' ',',': '--..--','.': '.-.-.-','?': '..--..',';': '-.-.-.',
            ':' : '---...', "'": '.----.', '-' : '-....-', '/': '-..-.',
            '(': '-.--.-', ')' :'-.--.-','_' :'..--.-'}

def Change_to_MorseCode():
    word =user_input.get()
    print(word)
    for element in word:
        for symbol in Morse_Code[element.upper()]:
            if symbol=='.':
                dot()
            elif symbol=='-':
                dash()
            else:
                time.sleep(0.5)
                
    print("The name you have entered is blinked !")

            
user_input=Entry(window,font=myFont,width=100,bg='grey')
user_input.grid(row=0,column=0)

button1=Button(window,text='Change',font=myFont,command=Change_to_MorseCode,bg='blue',height=2,width=10)
button1.grid(row=1,column=0)

