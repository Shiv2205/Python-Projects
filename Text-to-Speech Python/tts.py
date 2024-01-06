import pyttsx3
from pypdf import PdfReader
from tkinter.filedialog import askopenfilename
import os

def get_file_path(filename):
    return str(os.path.abspath(filename))

pdf_file_name = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
pdf_reader = PdfReader(get_file_path(pdf_file_name))
num_pages = len(pdf_reader.pages)
print(num_pages)

for page in range(19, 22):
    #Extract text and remove line breaks
    page_text = pdf_reader.pages[page].extract_text().splitlines() #.replace('\n', ' ')
    page_text = ' '.join(page_text)
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)
    engine.save_to_file(page_text, '{0}_Page_{1}.mp3'.format(pdf_file_name, page))
    engine.runAndWait()


#Properties you can modify:
    #rate = engine.getProperty('rate')
    #engine.setProperty('rate', rate+15)
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id) [0] for male voice, [1] for female voice
    #engine.say(page_text)