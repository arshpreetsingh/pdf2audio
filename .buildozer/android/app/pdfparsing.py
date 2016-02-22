from plyer import tts
from pdf import PdfFileReader 

def read_pdf(pdfFileName):
	
    pdf = PdfFileReader(pdfFileName) 

    return ''.join(pg.extractText() for pg in pdf.pages)
