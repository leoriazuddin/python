import pyttsx3
import PyPDF2

book = open('<path-to-file-pdf-file>', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = 1
while page < pages:
    speaker.say(pdfReader.getPage(page).extractText())
    page = page + 1

speaker.runAndWait()
