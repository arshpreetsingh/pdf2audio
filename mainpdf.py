from pdfmine.pdfparser import PDFParser 
from pdfmine.pdfdocument import PDFDocument 
from pdfmine.pdfpage import PDFPage 
from pdfmine.pdfpage import PDFTextExtractionNotAllowed 
from pdfmine.pdfinterp import PDFResourceManager 
from pdfmine.pdfinterp import PDFPageInterpreter 
from pdfmine.pdfdevice import PDFDevice 
from pdfmine.converter import TextConverter 
from pdfmine.layout import LAParams 
import unicodedata, codecs 
from cStringIO import StringIO  

def getPDFText(pdfFilenamePath):
    retstr = StringIO()
    parser = PDFParser(open(pdfFilenamePath,'r'))
    try:
        document = PDFDocument(parser)
    except Exception as e:
        print(pdfFilenamePath,'is not a readable pdf')
        return ''
    if document.is_extractable:
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr,retstr, codec='ascii' , laparams = LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        return retstr.getvalue()
    else:
        print(pdfFilenamePath,"Warning: could not extract text from pdf file.")
        return ''



def split_pdf( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]
