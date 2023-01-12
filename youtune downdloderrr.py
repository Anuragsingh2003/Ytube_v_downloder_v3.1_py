from tkinter import *
import time


try:
    strt=int(input("Please write secret code to launch our downloder program : "))
    print("welcome to your yt lite downloder..")
    user=input("Enter your good name : ")
    print("welcome to digital next genration mini py YT 2.01 videos downloder<>, ",user)
except ValueError:
    time.sleep(3)
    print("may be some mistake in your input , Please recheck Cearfully,.. secret code, hint:= {sum of first 2 digts of latitude & longitude of in which city your are in.. }")
    userdata=input("enter again > ")
    print("congrats!")

def ytube():
    from pytube import YouTube
    link=(str(hd.get()))
    yt=YouTube(link)
    stm=yt.streams.first()
    stm.download()
    print("downloder done vro")
    print("enjoy your video!")
    time.sleep(3)
    print("If any thing you want to say about this program or py so, Pease write here , and we definatily work on this and make more effective for you : ")
    feed=input("Write here your : ")
    print("please wait we are uploading your risponse.. ...  ....")
    time.sleep(3)
    print("we are work on your valuable feed thankyou for using..",user)

asr=Tk()
asr.title("Youtube DOWNLODER 2.0")
asr.geometry("600x400")
filebg=PhotoImage(file='pikrepo.png')
l_fr_bg=Label(asr,image=filebg)
l_fr_bg.place(x=0,y=0)
label=Label(text="Hey Buddy, Welcome,, Insert your link below",fg="purple",font="200x300",bg='steel blue').pack()
lbel2=Label(text="hey user there is some changes in your program you can'nt paste youtube link by mouse or touch, but you can paste link by 'CLTRL + V ' keys",fg="yellow",bg='purple' ).pack()
button1=Button(text="download",font="150x160",bg="green",fg="yellow",command=ytube).pack()
hd=StringVar()
valid=Entry(textvariable=hd,bd=4,bg='powder blue').pack()


