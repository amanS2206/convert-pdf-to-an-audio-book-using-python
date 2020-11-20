# import the libraries
import pyttsx3
import pdfplumber
import PyPDF2

# get the file name
file = 'p.pdf'

# create the pdf fie object
pdfFileObj = open(file,'rb')

# create the pdf file reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)