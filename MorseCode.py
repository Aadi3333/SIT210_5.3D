#Name: Aaditya
#Roll No: 2110994838

#Libraries
from tkinter import *
import tkinter.font

#To communicate with the GPIO pins
import RPi.GPIO as GPIO

#time variable
import time

GPIO.setwarnings(False)
#setup the GPIO as a GPIO board
GPIO.setmode(GPIO.BOARD)

#Setup for the pins as a output
GPIO.setup(12,GPIO.OUT)

#For new window or GUI
window = Tk()
#defining the title of the window which will be on the top of window
window.title("Morse Code")

#defining font for the window
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

#function defined for the dots of the morse code 
#output for the pin is setted high and low for some time
def dot():
    GPIO.output(12,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12,GPIO.LOW)
    time.sleep(1)

#function defined for the dash of the morse code 
#output for the pin is setted high and low for some time   
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

#This function is to changing the characters to the morse code
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

#For the user input          
user_input=Entry(window,font=myFont,width=100,bg='grey')
user_input.grid(row=0,column=0)

#A button is added so that after the user input when we click on it characters will be changed into morse code
#And according to the morse code led start to blink
button1=Button(window,text='Change',font=myFont,command=Change_to_MorseCode,bg='blue',height=2,width=10)
button1.grid(row=1,column=0)
