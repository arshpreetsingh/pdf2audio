'''
import PyPDF2 as pdflib
pdf = pdflib.PdfFileReader('/home/metal-machine/Desktop/Books & Media/dd.pdf')
print dir(pdf.pages)

for i in pdf.pages():
    print i
'''
'''
import PyPDF2 as pdflib

pdf = pdflib.PdfFileReader('/home/metal-machine/Desktop/Books & Media/dd.pdf')

def hellopy():
	
    yield pdf.pages

for i in hellopy():
	print i.extractText()
	
#for i in pdf.pages:
#	print i#.extractText()
'''
'''	
txt = u'\n'.join(pg.extractText() for pg in pdf.pages)

print txt
'''

from parser.pdf import PdfFileReader  

def read_pdf(pdfFileName):

    pdf = PdfFileReader(pdfFileName) 

    txt = ''.join(pg.extractText() for pg in pdf.pages)
    
    return txt
	
def split_pdf( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

