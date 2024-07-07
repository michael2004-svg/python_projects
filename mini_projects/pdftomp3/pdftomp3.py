import pyttsx3,PyPDF2
reader = PyPDF2.PdfReader(open('Vb.pdf','rb'))
speaker=pyttsx3.init()

for page_num in range(len(reader.pages)):
    print(page_num)
    text = reader.pages[page_num].extract_text
    #clean_text=text.strip().replace('\n',' ')
    print(text)
    print(reader)
#speaker.save_to_file(clean_text,'untetherdsoul.mp3')
#speaker.runAndWait()
#speaker.stop()