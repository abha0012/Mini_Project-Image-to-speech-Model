from django.shortcuts import render
from .miniproject import main

# Create your views here.
def home(request):
    return render(request, 'mini/home.html')


def about(request):
    return render(request, 'mini/about.html')


def help(request):
    return render(request, 'mini/help.html')


def visual(request):
    return render(request, 'mini/visuals2.html')

def traveller(request):
    return render(request, 'mini/traveller.html')

def helpstudent(request):
    return render(request, 'mini/helpstudent.html')

def main(request):
    import os
    import matplotlib.pyplot as plt
    import cv2  
    import easyocr
    import gtts
    from playsound import playsound
    from pylab import rcParams
    from IPython.display import Image

    # Do something
    rcParams['figure.figsize'] = 8,16
    reader = easyocr.Reader(['en'],gpu=False)
    output = reader.readtext(r'C:\Users\DELL\Downloads\help.png')
    # output
    cord = output[0][0]
    templist = []
    for k in output: 
        templist.append(k[1])
    # templist
    str =  ' '.join(templist)
    print(str)
    my_context = {str}
    # pip install translate
    # from translate import Translator
    # translator= Translator(to_lang="Marathi")
    # translation = translator.translate(str)
    # print (translation)
    tts = gtts.gTTS(str)
    # save the audio file
    tts.save("music.mp3")
    from playsound import playsound
    playsound("music.mp3")

    os.remove(r"C:\Users\DELL\Downloads\help.png")
    # os.remove(r"C:\Users\Dell\django_miniproject\music.mp3")
    return render(request, 'mini/home.html')


def travel(request):
    import matplotlib.pyplot as plt
    import cv2  
    import os
    import easyocr
    import gtts
    from playsound import playsound
    from pylab import rcParams
    from IPython.display import Image

    rcParams['figure.figsize'] = 8,16
    reader = easyocr.Reader(['en'],gpu=False)
    output = reader.readtext(r'C:\Users\DELL\Downloads\traveller.png')
    cord = output[0][0]
    templist = []
    for k in output: 
        templist.append(k[1])
    
    # templist
    str =  ' '.join(templist)
    print(str)

    # pip install translate

    from translate import Translator
    translator= Translator(to_lang="Marathi")
    translation = translator.translate(str)
    print (translation)

    # pip install gTTS pyttsx3 playsound

    # make request to google to get synthesis
    tts = gtts.gTTS(translation)

    # save the audio file
    tts.save("music.mp3")
    #play the sound
    from playsound import playsound
    playsound("music.mp3")
    os.remove(r"C:\Users\DELL\Downloads\traveller.png")
    # os.remove(r"C:\Users\Dell\django_miniproject\music.mp3")
    return render(request, 'mini/home.html')

def student(request):
    import matplotlib.pyplot as plt
    import cv2  
    import os
    import easyocr
    import gtts
    from playsound import playsound
    from pylab import rcParams
    from IPython.display import Image

    rcParams['figure.figsize'] = 8,16
    reader = easyocr.Reader(['en'],gpu=False)
    output = reader.readtext(r'C:\Users\DELL\Downloads\student.png')
    cord = output[0][0]
    templist = []
    for k in output: 
        templist.append(k[1])
    
    # templist
    st =  ' '.join(templist)
    print(st)
    #removing spaces
    #st.replace(" ", "")
    # Python3 code to remove whitespace
    def remove(st):
        return "".join(st.split())  
    # Driver Program
    # print(remove(st))
    result = eval(st)
    # print(result)
    final = st + '=' + str(result)
    print(final)
    
    # pip install translate
    # from translate import Translator
    # translator= Translator(to_lang="Marathi")
    # translation = translator.translate(str)
    # print (translation)
    # pip install gTTS pyttsx3 playsound
    # make request to google to get synthesis

    tts = gtts.gTTS(final)

    # save the audio file
    tts.save("music.mp3")
    #play the sound
    from playsound import playsound
    playsound("music.mp3")
    os.remove(r"C:\Users\DELL\Downloads\student.png")
    # os.remove(r"C:\Users\Dell\django_miniproject\music.mp3")
    return render(request, 'mini/home.html')
