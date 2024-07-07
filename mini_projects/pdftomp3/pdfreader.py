import PyPDF2,pyttsx3
# open the PDF file
pdfFile = open('Vb.pdf', 'rb')
speaker=pyttsx3.init()

# create PDFFileReader object to read the file
pdfReader = PyPDF2.PdfReader(pdfFile)
print("Printing the document info: " + str(pdfReader.getDocumentInfo))
print("- - - - - - - - - - - - - - - - - - - -")
print("Number of Pages: " + str(len(pdfReader.pages)))

for i in range(0, len(pdfReader.pages)):
       pageObj = pdfReader.pages[i]
       text = pageObj.extract_text()
       clean_text=text.strip().replace('\n',' ')
       print(clean_text)
# close the PDF file object
speaker.save_to_file(clean_text,'vb.mp3')
speaker.runAndWait()
speaker.stop()
pdfFile.close()