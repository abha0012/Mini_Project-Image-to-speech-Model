# -*- coding: utf-8 -*-
# """MiniProject-1.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/11tcjsNmCqcbYthGj-Z0Y3ft-ikFS1DnM
# """

# pip install easyocr

def main():

  import matplotlib.pyplot as plt
  import cv2
  import easyocr
  import gtts
  from playsound import playsound
  from pylab import rcParams
  from IPython.display import Image

  rcParams['figure.figsize'] = 8,16

  # from google.colab import drive
  # drive.mount('/content/drive')

  reader = easyocr.Reader(['en'],gpu=False)

  image = cv2.imread("rock1.png")
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Image("rock1.jpeg")

  output = reader.readtext('rock1.png')

  # output

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
  tts = gtts.gTTS(str)

  # save the audio file
  tts.save("music.mp3")

  # pip install gTTs

  # import gtts

  # pip uninstall playsound

  # pip install playsound

  # import playsound