from pdf import PdfFileReader 

def read_pdf(pdfFileName):
	
    pdf = PdfFileReader(pdfFileName) 

    yield from (pdf.pages)

for i in read_pdf('book.pdf'):
    print(i)
