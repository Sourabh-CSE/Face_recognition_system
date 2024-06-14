from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg= "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"New folder\Developer2.jpg")
        img_top=img_top.resize((1530,740),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=740)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"New folder\Developer.png")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer Info
        dev_label=Label(main_frame,text="Hello, I am Sanskar Gurnani",font=("times new roman",16,"bold"),bg="white",fg="darkblue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Currently Persuing CSE Engg",font=("times new roman",16,"bold"),bg="white",fg="darkblue")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="Contact:- 9753459439",font=("times new roman",16,"bold"),bg="white",fg="darkblue")
        dev_label.place(x=0,y=75)

        img_top2=Image.open(r"New folder\Developer1.png")
        img_top2=img_top2.resize((500,400),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=0,y=210,width=500,height=400)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()