from PyPDF2 import PdfFileMerger

#append

def by_appending():
    merger=PdfFileMerger()
    
    f1=open('pdf1.pdf','rb')
    merger.append(f1)
    
    merger.append('pdf2.pdf')
    merger.write('mergedPdf.pdf')
    
#insert

def by_inserting():
    merger=PdfFileMerger()
    merger.append('pdf1.pdf')
    merger.merge(0,'pdf2.pdf')
    merger.write('mergedpdf1.pdf')
    
    
if __name__=='__main__':
    by_appending()
    by_inserting()
