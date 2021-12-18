from PyPDF2 import PdfFileMerger
import sys


pdfs = [sys.argv[1], sys.argv[2]]
merger = PdfFileMerger()

pages = int(sys.argv[3])

for page in range(0,pages):
    merger.append(pdfs[0], pages=(page,page+1))
    merger.append(pdfs[1], pages=(page,page+1))

merger.write(sys.argv[4])
merger.close()
