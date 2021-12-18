from PyPDF2 import PdfFileMerger

pdf = 'contrato_transmision.pdf'
merger = PdfFileMerger()

merger.append(pdf, pages=(0,32))
merger.append(pdf, pages=(34,38))

merger.write('CONTRATO_TRANSMISION_LUCERO_MONTEVERDE.pdf')
merger.close()
