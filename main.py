'''
Full Project Link :- https://github.com/ShantonuAcharjee/YouTube-Video-Downloder-Python
Author: Shantonu Acharjee
Email: shantonuacharjee@gmail.com
YouTube :- http://tinyurl.com/yy374bou
FaceBook: http://tinyurl.com/y52rgdd4
'''

from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from threading import *

fileSize = 0
strms = ''
def startDownload():
    global fileSize
    global strms
    global dBtn
    try:
        urlField2.config(text='')
        urlField6.config(text='')
        dBtn.config(text='Start Downloard')
        url = urlField.get() #'https://www.youtube.com/watch?v=e5PIO3a_f6o'
        print("Your Url Is :",url)

        # Change Button TEXT
        dBtn.config(text='Plese Wait..')

        dBtn.config(state = DISABLED)
        path = askdirectory()
        print("Your Path IS :",path)
        if path is None:
            return

        ob=YouTube(url)

        strms =ob.streams.first()
        urlField2.config(text=strms.title)
        q=round(strms.filesize/1048576,2)
        urlField6.config(text=str(q) + 'MB')
        strms.download(path)



        print('Download Done')
        dBtn.config(text='Done.')
        dBtn.config(state=NORMAL)
        urlField.delete(0,END)



    except Exception as e:
        print('Error!:',e)


def startDownloadThread():
    thread=Thread(target=startDownload)
    thread.start()



# strat GUI
main=Tk()
main.geometry('500x400')
main.title('YouTube Video Downloarder')

urlField3 = Label(main,text=('Enter Url Below'),font=('verdana',10))
urlField3.pack(side=TOP,fill=X,pady=10)

urlField = Entry(main,bg='aqua',justify = RIGHT,font=('verdana',20))
urlField.pack(side=TOP,fill=X,padx=40,pady= 5 )

dBtn = Button(main,text = 'Start Downloard',font=('verdana',15),relief='ridge',bg='pink',command = startDownloadThread)
dBtn.pack(side=TOP,fill=X,padx=150,pady=15)

urlField4 = Label(main,text=('Video Name'),font=('verdana',10))
urlField4.pack(side=TOP,fill=X,pady=10)

urlField2 = Label(main,text='',bg='darkgoldenrod',font=('verdana',20))
urlField2.pack(side=TOP,fill=X,padx=40)

urlField5 = Label(main,text=('Video Size'),font=('verdana',10))
urlField5.pack(side=TOP,fill=X,pady=20)

urlField6 = Label(main,text='',bg='Brown',font=('verdana',20))
urlField6.pack(side=TOP,fill=X,padx=40)

main.mainloop()
