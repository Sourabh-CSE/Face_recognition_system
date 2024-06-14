from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from main import Face_Recognition_System


def main1():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):

        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"New folder\Login4.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1.0,relheight=1.0)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"New folder\Developer.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg= "white")
        get_str.place(x=95,y=100)
        
        # Label
        username_lbl=Label(frame,text="Username",font=("times new roman",18,"bold"),bg="black",fg= "white")
        username_lbl.place(x=80,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="black",fg= "white")
        password_lbl.place(x=80,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)

        # Icon Image
        img2=Image.open(r"New folder\Password1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=328,width=25,height=25)

        img3=Image.open(r"New folder\Password2.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=398,width=25,height=25)

    
        # Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=115,y=305,width=120,height=35)

        # Register Buttton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=360,width=160)

        # Forgot Password Button
        loginbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=180,y=360,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Field Required")
        elif self.txtuser.get()=="Sanskar" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition_system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),               
                                                                                       self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # '''''''''''''''''''''''''''''RESET PASSWORD ''''''''''''''''''''''''''''''''''''''
    def reset_pass(self):
        if self.security_combo.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security_answer.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.security_combo.get(),self.txt_security_answer.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login with new password",parent=self.root2)
                self.root2.destroy()






    # ''''''''''''''''''''''''' FORGOT PASSWORD WINDOW'''''''''''''''''''''''''''''''''''''''''''''
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter Email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognition_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
                l.place(x=0,y=10,relwidth=1)

                # Security
                security=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security.place(x=50,y=80)

                self.security_combo=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="read")
                self.security_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite Book","Your Favourite Teacher")
                self.security_combo.current(0)
                self.security_combo.place(x=50,y=110,width=250)

                
                security_answer=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_answer.place(x=50,y=150)

                self.txt_security_answer=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security_answer.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)





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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
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

    def return_login(self):
        self.root.destroy()

# Main 
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # FIRST IMAGE
        img=Image.open(r"New folder\students.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # SECOND IMAGE
        img1=Image.open(r"New folder\Abc.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        # THIRD IMAGE
        img2=Image.open(r"New folder\GGITS.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # BACKGROUND IMAGE
        img3=Image.open(r"New folder\sky.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg= "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # TIME
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),bg='white',fg='blue')
        lbl.place(x=10,y=0,width=150,height=50)
        time()

        # STUDENT BUTTON
        img4=Image.open(r"New folder\Stu.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=200,y=300,width=220,height=40)


        # DETECT FACE BUTTON
        img5=Image.open(r"New folder\Face.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=500,y=300,width=220,height=40)


        # ATTENDANCE BUTTON
        img6=Image.open(r"New folder\A.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=800,y=300,width=220,height=40)




        # HELP DESK BUTTON
        img7=Image.open(r"New folder\HelpDesk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # TRAIN FACE BUTTON
        img8=Image.open(r"New folder\TrainData.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=200,y=600,width=220,height=40)


        # PHOTOS BUTTON
        img9=Image.open(r"New folder\Photos.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=500,y=600,width=220,height=40)



        # DEVELOPER BUTTON
        img10=Image.open(r"New folder\Developer.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=800,y=600,width=220,height=40)

        # EXIT BUTTON
        img11=Image.open(r"New folder\E.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg= "white")
        b1_1.place(x=1100,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # ''''''''''''''''''''''''''''''''' FUNCTION BUTTONS ''''''''''''''''''''''''''''''''''''''

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)







if __name__ =="__main__":
    main1()
