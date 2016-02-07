from plyer import tts
from pdf import PdfFileReader 

def read_pdf(pdfFileName):

    pdf = PdfFileReader(pdfFileName) 

    txt = (pg.extractText() for pg in pdf.pages)
    
    return  txt
	
def split_pdf( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]
