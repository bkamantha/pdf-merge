 # "pip install PyPDF2"
 
#import dependancy
import os
from os import listdir
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader




# file folder location
input_dir = "C:/Users/Brainx/Documents/electronics/"






#add all file dir to singal list
merge_list = []
for x in listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    merge_list.append(input_dir + x)

merge_list.sort()

#add modeule
merger = PdfFileMerger()

page_no = 0

#merge pdfs into single
for pdf in merge_list:
    
    #get file name
    document_name = os.path.basename(pdf)
    
    #add bookmark as file name
    merger.addBookmark(document_name, page_no, parent=None)
    
    #read pdf and check number of pages for add next bookmark
    pdf = PdfFileReader(open(pdf,'rb'))
    number = pdf.getNumPages()
    page_no = page_no + number
    
    #merge all PDFs
    merger.append(pdf)
    
    
#output merge file    
merger.write("C:/Users/Brainx/Documents/electronics/All in one.pdf") #your output directory
merger.close()

print("Done.. check your output directory")