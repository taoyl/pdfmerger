#!/bin/env python3
####################################################################################################
## File Name     :  pdfmerger.py
## Author        :  Nero Tao (nerotao@foxmail.com)
## Created At    :  7/15/2022 9:45:54 AM
## Last Modified :  7/15/2022 10:06:04 AM
##
####################################################################################################
## Description   :  Merge multiple pdfs into a single one.
##                  Put all your pdfs with ordered filenames (e.g. 001.pdf, 002.pdf, etc) 
##                  into pdfs directory, and run:
##                  > python3 pdfmerger.py
##
####################################################################################################
## Change History:  R0.1 2022-07-15 | Initial creation.
##
####################################################################################################

import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

all_pdf_files = sorted(glob.glob("pdfs/*.pdf"))
print(f'Input pdfs: {all_pdf_files}')
# The pdf reader IO should not be closed before pdf writer writes all streams into the output file
# so we should not use with...as context handling
opened_pdfs = [open(pdf_file, 'rb') for pdf_file in sorted(all_pdf_files)]
rd_pdfs = [PdfFileReader(pdf) for pdf in opened_pdfs]
wr_pdf = PdfFileWriter()
_ = [wr_pdf.addPage(rpdf.getPage(x)) for rpdf in rd_pdfs for x in range(rpdf.numPages)]
# close all input files after write the output file
print('Saving merged pdf into merged.pdf ...')
with open('megered.pdf', 'wb') as pdf:
    wr_pdf.write(pdf)
_ = [pdf.close() for pdf in opened_pdfs]
