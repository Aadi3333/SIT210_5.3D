from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter.font
from gpizero import LED
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

window = Tk()
window.title("Morse Code Blinking Name")
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

def dot():
    GPIO.output(11,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11,GPIO.LOW)
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
    print(" " + word)
    for letter in word:
        for symbol in Morse_Code[letter.upper()]:
            if symbol=='.':
                dot()
            elif symbol=='-':
                dash()
            else:
                time.sleep(0.5)

    for element in word:
        for symbol in Morse_Code[element]:
            if symbol=='.':
                dot()
            elif symbol=='-':
                dash()
            else:
                time.sleep(0.5)

    print("The name you have entered is blinked !")

    GPIO.output(14,GPIO.HIGH)
    time.sleep(1.50)
    GPIO.output(14,GPIO.LOW)
    time.sleep(1.50)
            
user_input=Entry(window,text= 'MorseCode',font=myFont,width=25,bg='white')
user_input.grid(row=0,column=0)

button1=Button(window,text='Change',font=myFont,command=Change_to_MorseCode,bg='black',height=5,width=7)
button1.grid(row=1,column=0)
