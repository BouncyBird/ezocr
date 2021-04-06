from tkinter import *
from tkinter.ttk import *
import tkinter as tk
u = 1

sload = tk.Tk()
sload.geometry('700x600')
sload.title('Loading...')
sload.iconbitmap('text.ico')

progress = Progressbar(sload, orient = HORIZONTAL, 
              length = 500, mode = 'determinate')
w12 = tk.Label(text="Loading...", fg="black", font=('Calibri', 36, 'bold'))

w12.pack()
progress.pack()

def wu(time):
    global u
    while u <= time:
        u = u + 1
        progress['value'] = u
        sload.update_idletasks()

import pytesseract
wu(10)
from tkinter import *
wu(20)
from tkinter.ttk import *
wu(30)
from PIL import Image
from PIL import ImageGrab
wu(40)
import cv2
wu(50)
import numpy as np
wu(60)

from tkinter.filedialog import askopenfilename
wu(70)
from tkinter.filedialog import asksaveasfilename
wu(80)

import pyperclip
import pyautogui as pag
wu(90)
import os
import sys
wu(100)

sload.destroy()


#pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def upimg():
	global wl, sbu
	sbu.pack_forget()
	def savetext():
		fsel = asksaveasfilename(title = "Select save location and name",filetypes = (("Text Files","*.txt"),("All files","*.*")))
		with open(fsel + '.txt', "w",5 ,"utf-8") as text_file:
			text_file.write(text)
	def home():
		os.execl(sys.executable, sys.executable, *sys.argv)


	filename = askopenfilename()
	file_path= filename

	wl.pack_forget()

	im = Image.open(file_path)
	im.save('oim\\ocr.png', dpi=(300, 300))

	image = cv2.imread('oim\\ocr.png')
	image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
	retval, threshold = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

	text = pytesseract.image_to_string(threshold)
	def copytext():
		pyperclip.copy(text)
	upimgb.pack_forget()
	copyb = tk.Button(root, text="Copy Text", width=10, height=1, fg="black", command = copytext)
	ocrtext = Text(root)
	hb = tk.Button(root, text="Home", width=10, height=1, fg="black", command = home)	
	stb = tk.Button(root, text="Save Text", width=10, height=1, fg="black", command = savetext)
	hb.pack() 
	stb.pack()
	ocrtext.insert(INSERT, text)
	copyb.pack(padx=30, pady=0)
	ocrtext.pack()
	os.remove("oim\\ocr.png")

def simg():
	global wl, upimgb, sbu
	def upimg2():
		sdone.pack_forget()
		def savetext():
			fsel = asksaveasfilename(title = "Select save location and name",filetypes = (("Text Files","*.txt"),("All files","*.*")))
			with open(fsel + '.txt', "w",5 ,"utf-8") as text_file:
				text_file.write(text)
		def home():
			os.execl(sys.executable, sys.executable, *sys.argv)


		wl.pack_forget()

		im = ImageGrab.grabclipboard()
		im.save('oim\\ocr.png', dpi=(300, 300))

		image = cv2.imread('oim\\ocr.png')
		image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
		retval, threshold = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

		text = pytesseract.image_to_string(threshold)
		def copytext():
			pyperclip.copy(text)
		upimgb.pack_forget()
		copyb = tk.Button(root, text="Copy Text", width=10, height=1, fg="black", command = copytext)
		ocrtext = Text(root)
		hb = tk.Button(root, text="Home", width=10, height=1, fg="black", command = home)	
		stb = tk.Button(root, text="Save Text", width=10, height=1, fg="black", command = savetext)
		hb.pack() 
		stb.pack()
		ocrtext.insert(INSERT, text)
		copyb.pack(padx=30, pady=0)
		ocrtext.pack()
		os.remove("oim\\ocr.png")
	pag.hotkey('win', 'shift', 's')
	wl.pack_forget()
	upimgb.pack_forget()
	sbu.pack_forget()
	sdone = tk.Button(root, text="Done", width=10, height=1, fg="black", command = upimg2)
	sdone.pack()


root = tk.Tk()
root.geometry('700x600')
root.title('EZ-OCR')
root.iconbitmap('text.ico')

wl = tk.Label(text="Welcome!\nTo EZ-OCR", fg="black", font=('Calibri', 36, 'bold'))
wl.pack(padx=0, pady=55)

upimgb = tk.Button(root, text="Upload Image", width=20, height=3, fg="black", command = upimg)
upimgb.pack()

sbu = tk.Button(root, text="Take Screenshot", width=20, height=3, fg="black", command = simg)
sbu.pack()


root.mainloop()