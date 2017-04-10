from __future__ import print_function

import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def splitPdf(f_file, marker_list):
    inputpdf = PdfFileReader(open(f_file, "rb"))
    startPage = 0
    endPage = inputpdf.numPages
    f_name = f_file[:-4] # remove '.pdf'
    saved_path = f_name + "/"
    selected_pdf = f_name.split('/')[-1]

    # check if page is out of range
    if marker_list[-1] > endPage:
        return 'Final number is larger than the page number'

    # add the last page to make sure all page gone through
    if marker_list[-1] != endPage:
        marker_list.append(endPage)

    # create folder if not exist
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    

    for i in range(len(marker_list)):
        output = PdfFileWriter()
        targetPage = marker_list[i] - 1 # off set page by one

        while targetPage >= startPage:
            output.addPage(inputpdf.getPage(startPage))
            startPage += 1
            
        saved_file = saved_path + "%s-page%s.pdf" % (selected_pdf, marker_list[i])
        
        with open(saved_file, "wb") as outputStream:
            output.write(outputStream)

    return True
    
def main():

    splitPdf('/Users/ricky/2017/Eutility/Invoice_Spliter/PDFspliter/pdf_erm.pdf', [1,3])

if __name__ == "__main__":
    main()
    

