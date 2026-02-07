from gtts import gTTS 



import PyPDF2




pdf_file =open('name.pdf','rb')


pdf_reader = PyPDF2.PdfFileReader(pdf_file)
count = pdf_reader.numPages

textList =[]

for i in range(count):
    try:
        page= pdf_reader.getPage(i)
        textList.append(page.extractText())
    except:
        pass
    


textString = " ".join(textList)


print(textString)

language = 'en'


myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")