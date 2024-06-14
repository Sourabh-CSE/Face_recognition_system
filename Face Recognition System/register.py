from atexit import register
from tkinter import*
from tkinter import ttk
from tokenize import Imagnumber
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #  Background Image
        self.bg=ImageTk.PhotoImage(file=r"D:\Face Recognition System\New folder\Login4.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #  Left Image
        self.bg1=ImageTk.PhotoImage(file=r"D:\Face Recognition System\New folder\Studen.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # Main Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=850,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg= "green")
        register_lbl.place(x=20,y=20)

        # Label and Entry

        # ''''''''' ROW 1''''''''
        fname=Label(frame,text="First Name",font=("times new roman",18,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",18,"bold"))
        self.txt_fname_entry.place(x=50,y=140,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",18,"bold"),bg="white")
        l_name.place(x=400,y=100)

        self.txt_l_name_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",18,"bold"))
        self.txt_l_name_entry.place(x=400,y=140,width=250)

        # ''''''''''' ROW 2''''''''''
        contact=Label(frame,text="Contact",font=("times new roman",18,"bold"),bg="white")
        contact.place(x=50,y=180)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",18,"bold"))
        self.txt_contact.place(x=50,y=220,width=250)

        email=Label(frame,text="Email",font=("times new roman",18,"bold"),bg="white")
        email.place(x=400,y=180)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",18,"bold"))
        self.txt_email.place(x=400,y=220,width=250)

        # ''''''''''' ROW 3''''''''''''
        security=Label(frame,text="Select Security Question",font=("times new roman",18,"bold"),bg="white")
        security.place(x=50,y=260)

        security_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",18,"bold"),state="read")
        security_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite Book","Your Favourite Teacher")
        security_combo.current(0)
        security_combo.place(x=50,y=300)

        
        security_answer=Label(frame,text="Security Answer",font=("times new roman",18,"bold"),bg="white")
        security_answer.place(x=400,y=260)

        self.txt_security_answer=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",18,"bold"))
        self.txt_security_answer.place(x=400,y=300,width=250)

        # ''''''''''ROW 4'''''''''''
        pswd=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="white")
        pswd.place(x=50,y=340)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",18,"bold"))
        self.txt_pswd.place(x=50,y=380,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",18,"bold"),bg="white")
        confirm_pswd.place(x=400,y=340)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",18,"bold"))
        self.txt_confirm_pswd.place(x=400,y=380,width=250)

        # ''''''''''''Check Button ''''''''
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=420)

        # '''''''''''''' Buttons ''''''''''
        img=Image.open(r"D:\Face Recognition System\New folder\Register.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=480,width=300)


        img1=Image.open(r"D:\Face Recognition System\New folder\Login2.jpg")
        img1=img1.resize((220,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=370,y=480,width=300)


    # Function Declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Invalid","Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists, Please Enter another Email")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")





        






if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
