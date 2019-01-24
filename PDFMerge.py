import PyPDF2
from PyPDF2 import PdfFileMerger

#Specify the path of the doc
path = "PATH"

#Create a PdfFileMerger Object
merger = PdfFileMerger()

#Open all docs which will be merged together and put them in one list
in1 = open(path + "\\1.pdf", "rb")
in2 = open(path + "\\2.pdf", "rb")
in3 = open(path + "\\3.pdf", "rb")
in4 = open(path + "\\4.pdf", "rb")
in5 = open(path + "\\5.pdf", "rb")
in6 = open(path + "\\6.pdf", "rb")
in7 = open(path + "\\7.pdf", "rb")
in8 = open(path + "\\8.pdf", "rb")
in9 = open(path + "\\9.pdf", "rb")
in10 = open(path + "\\10.pdf", "rb")
in11 = open(path + "\\11.pdf", "rb")
in12 = open(path + "\\12.pdf", "rb")
in13 = open(path + "\\13.pdf", "rb")
in14 = open(path + "\\14.pdf", "rb")
in15 = open(path + "\\15.pdf", "rb")
in16 = open(path + "\\16.pdf", "rb")

docs = [in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,in16]


#Merge them together. One doc had a blank page.
for doc in docs:
    if doc == in6:
        merger.append(doc, pages = (0,2))

    else:
        merger.append(doc)

#Specfiy the output and write the merged files in it
output = open(path + "\\FILE.pdf", "wb")
merger.write(output)
