#!/usr/bin/env python
# coding: utf-8

# In[11]:


import traitlets
from ipywidgets import widgets
from IPython.display import display
from tkinter import Tk, filedialog
from googletrans import*
import speech_recognition as sr
import pandas as pd
translator = Translator()


# In[12]:


choice=int(input("Enter your choice: \n1.Enter text manually \n2.Speaklive\n3.AudioFile\n Enter a index number above options :  "))
l=[1,2,3]


# In[23]:


if choice == 1:
    recognized_text=str(input("Enter a text to convert into Your Favourite language\n"))#text manually
elif choice == 2:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
        recognized_text=text
elif choice not in l:
    print("Sorry you Chossen invalid option Try again Hope This Time Works")


# In[24]:


with open('langlist.txt') as f1:
    csv_reader =f1.readlines()
d={}
for i in range(len(csv_reader)):
    l,c=csv_reader[i].split(",")
    c=c[:len(c)-1]
    c=c.strip()
    l=l.strip()
    d[l]=c


# In[28]:


print(pd.read_csv('langlist.txt'))
print("enter language you want to translate")
target=str(input("enter a target language  :   ")).capitalize()
if (target not in d):
    print("invalid language please check your spelling that matches target language You entered: ",target)
else:
    result = translator.translate(recognized_text, dest=d[target])
    print("Your Target language is :",result.text)


# In[29]:


choice=3
if (choice == 3):
    class SelectFilesButton(widgets.Button):
        def __init__(self):
            super(SelectFilesButton, self).__init__()
            # Add the selected_files trait
            self.add_traits(files=traitlets.traitlets.List())
            # Create the button.
            self.description = "Select Files"
            self.icon = "square-o"
            self.style.button_color = "orange"
            # Set on click behavior.
            self.on_click(self.select_files)

        @staticmethod
        def select_files(b):
            """Generate instance of tkinter.filedialog.

            Parameters
            ----------
            b : obj:
                An instance of ipywidgets.widgets.Button 
            """
            # Create Tk root
            root = Tk()
            # Hide the main window
            root.withdraw()
            # Raise the root to the top of all windows.
            root.call('wm', 'attributes', '.', '-topmost', True)
            # List of selected fileswill be set to b.value
            b.files = filedialog.askopenfilename(multiple=True)
    
            b.description = "Files Selected"
            b.icon = "check-square-o"
            b.style.button_color = "lightgreen"
    my_button = SelectFilesButton()


# In[30]:


my_button


# In[31]:


path=my_button.files
pathl=str(path)
pathl
pa=pathl.split("/")
pa
f=pa[-1]
f=f[:len(f)-2]
f


# In[32]:


import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile(f) as source:              
    audio = r.record(source)
try:
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
except:
    print("Sorry could not recognize what you said")
recognized_text=text


# In[ ]:


with open('langlist.txt') as f1:
    csv_reader =f1.readlines()
d={}
for i in range(len(csv_reader)):
    l,c=csv_reader[i].split(",")
    c=c[:len(c)-1]
    c=c.strip()
    l=l.strip()
    d[l]=c


# In[33]:


print(pd.read_csv('langlist.txt'))
print("enter language you want to translate")
target=str(input("enter a target language  :   ")).capitalize()
if (target not in d):
    print("invalid language please check your spelling that matches target language You entered: ",target)
else:
    result = translator.translate(recognized_text, dest=d[target])
    print("Your Target language is :",result.text)


# In[ ]:




