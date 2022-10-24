import pytesseract
import tkinter
import os
import pyperclip
from tkinter import *
from tkinter import filedialog
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\imarcos\AppData\Local\Tesseract-OCR\tesseract.exe'

raiz=Tk()
raiz.title("OCR-Program")
raiz.resizable(False,False)
#raiz.iconbitmap("icono.ico")
raiz.geometry("400x50")
 
miframe=Frame ()
miframe.pack(fill="both", expand="True")
miframe.config(bg="green")
#miframe.config(width="550", height="350")

def createText():
    imagen=tkinter.filedialog.askopenfilename(filetypes =[('PNG', '*.png'),('JPG','*.jpg')])
    text = pytesseract.image_to_string(imagen, config='')
    pathImg=os.path.splitext(imagen)[0]+'_extracto'+".txt"
    tkinter.messagebox.showinfo(title="Se ha generado el siguiente archivo", message="Se ha generado el siguiente archivo\n {pathImg}")
    with open(pathImg, 'w') as f:
        f.write(text)
    
def copyText():
    imagen=tkinter.filedialog.askopenfilename(filetypes =[('PNG', '*.png'),('JPG','*.jpg')])
    text = pytesseract.image_to_string(imagen, config='')
    pyperclip.copy(text)
    tkinter.messagebox.showinfo(title="Texto copiado", message="Se ha copiado el texto")

saveText=Button(miframe,width=50,bg="green",fg="white",text="Extraer texto a txt",font=("Console",10),command=createText)
saveText.grid(row=0, column=1)
copyText=Button(miframe,width=50,bg="green",fg="white",text="Copiar texto a portapapeles",font=("Console",10), command=copyText)
copyText.grid(row=1, column=1)

raiz.mainloop()
