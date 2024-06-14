from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ''''''''''''''''''''''''''''''''' Variables ''''''''''''''''''''''''''''''''''''''''''''''''''
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        # FIRST IMAGE
        img=Image.open(r"New folder\Attendance1.png")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # SECOND IMAGE
        img1=Image.open(r"New folder\Attendance2.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # BACKGROUND IMAGE
        img3=Image.open(r"New folder\Studen.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg= "darkgreen")
        title_lbl.place(x=-2,y=-2,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        # LEFT LABEL FRAME
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"New folder\Attendance3.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=360)

        # Label and Entry

        # Attendance ID
        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",11,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attend_id,font=("times new roman",11,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # ROLL NO
        roll_no_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",11,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attend_roll,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # STUDENT NAME
        attendanceName_label=Label(left_inside_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="white")
        attendanceName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        attendanceName_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attend_name,font=("times new roman",11,"bold"))
        attendanceName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # DEPARTMENT
        attendance_dep_label=Label(left_inside_frame,text="Department",font=("times new roman",11,"bold"),bg="white")
        attendance_dep_label.grid(row=1,column=2,padx=10)

        attendance_dep_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attend_dep,font=("times new roman",11,"bold"))
        attendance_dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # TIME
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10)

        time_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attend_time,font=("times new roman",11,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DATE
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",11,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10)

        date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attend_date,font=("times new roman",11,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # ATTENDANCE
        atten_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",11,"bold"),bg="white")
        atten_label.grid(row=3,column=0,padx=10,sticky=W)

        atten_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",11,"bold"),state="read",width=22)
        atten_combo["values"]=("Status","Present","Absent")
        atten_combo.current(0)
        atten_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # Buttons Frane
        btn_frame=LabelFrame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        # RIGHT LABEL FRAME 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=580)

        # img_right=Image.open(r"New folder\Attendance4.png")
        # img_right=img_right.resize((720,130),Image.ANTIALIAS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(Right_frame,image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=720,height=130)

        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=710,height=455)

        # ''''''''''''''''''''''''''''' Scroll Bar and Table '''''''''''''''''''''''''''''''''''''''''''''''''''
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # '''''''''''''''''''''''''''''''''''''''''''''''''''' Fetch Data ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

        
    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    # Export CSV 
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,"w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Sucessfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")












if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()

        