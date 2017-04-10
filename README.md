# Invoice_Spliter

### Issue the tool try to solve:
Consolidated invoice from different retailers have combined multiple pages of bills into one, e.g. 2 page or 3 page each. Split tool like PDFSam can only split by even/odd, n page or after n page.

### Function of the tool
The tool is built to customise the split page number. For example, a pdf file that contains 10 pages needs to be split into 1-2, 3, 4-5, 6-9, 10. Simply run the tool and entry end page, e.g. 2, 3, 5 for selected file, will do the work.

All split files will be generated into a sub directory and stored in the same directory as the original pdf file.

the tool is only working for pdf.

### Installation
1. download or clone the folder
2. open terminal or cmd and run: python setup.py build
3. a build directory will be generated

### Update
1. in order to build the file, make sure the your computer has PyPDF2 installed
2. it works for python 2.7
