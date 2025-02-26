import pyttsx3 as tts
import PyPDF2 as PDF
from tkinter.filedialog import *

book = askopenfilename()
reader = PDF.PdfReader(book)
pages = len(reader.pages)

for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    player = tts.init()
    player.say(text)
    player.runAndWait()