from __future__ import print_function

import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def splitPdf(f_file, marker_list):
    inputpdf = PdfFileReader(open(f_file, "rb"))
    startPage = 0
    endPage = inputpdf.numPages-1
    f_name = f_file[:-4] # remove '.pdf'
    saved_path = f_name + "/"

    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    
    print(endPage)
    print(inputpdf)

    for i in range(len(marker_list)):
        output = PdfFileWriter()
        targetPage = marker_list[i]
        while targetPage >= startPage:
            output.addPage(inputpdf.getPage(startPage))
            startPage += 1
            
        saved_file = saved_path + "document-page%s.pdf" % i
        print(saved_file)
        
        with open(saved_file, "wb") as outputStream:
            output.write(outputStream)
            pass
    
def main():

    splitPdf('/Users/ricky/2017/Eutility/Invoice_Spliter/PDFspliter/pdf_erm.pdf', [0,3])

if __name__ == "__main__":
    main()
    

