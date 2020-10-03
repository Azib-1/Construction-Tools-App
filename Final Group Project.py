
#This is the Python Code for the Information System called Shared Power which is created by the Knight Coders


#For each code that is adapted from the Internet, it has been refrenced right below the code

#This code is divided into three sections named as Tradesman,Hirer and Administrator
#It uses Tkinter which is Graphical User Interface
#Package and we used global variable.





#..........................................................Code starts from here..............................................#


#Importing the pacakages

from tkinter import *
import os
import random
import time
import datetime
from tkinter import filedialog
from tkinter import messagebox



def Shared_Power_Window():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Shared Power")
    Label(text="Shared Power", bg="lightblue", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login as Tradesman", height="2", width="30",
           command=New_or_Existing_user_As_Tradesman).pack()
    Label(text="").pack()
    Button(text="Login as Hirer", height="2", width="30",
           command=New_or_Existing_user_As_Hirer).pack()
    Label(text="").pack()
    Button(text="Login as Administrator", height="2",
           width="30", command=Login_As_Administrator).pack()
    Label(text="").pack()

    screen.mainloop()




###########################################################################............Tradesman Section..........###########################################################################################################

def New_or_Existing_user_As_Tradesman():
    global screen8
    screen8 = Tk()
    screen8.geometry("350x300")
    screen8.title("New or Existing User as Tradesman")
    Button(screen8, text="New User", width="30", height="2",
           command=Register_As_Tradesman, font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(screen8, text="Existing User", width="30", height="2"
           , command=Login_As_Tradesman, font=("Calibri", 13)).pack()
    Label(text="").pack()

def Register_As_Tradesman():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x400")

    global username
    global password
    global name
    global address
    global email
    global telephone
    global username_entry
    global password_entry
    global name_entry
    global address_entry
    global email_entry
    global telephone_entry
    username = StringVar()
    password = StringVar()
    name = StringVar()
    address = StringVar()
    email = StringVar()
    telephone = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="Age").pack()
    name_entry = Entry(screen1, textvariable=name)
    name_entry.pack()
    Label(screen1, text="Address *").pack()
    address_entry = Entry(screen1, textvariable=address)
    address_entry.pack()
    Label(screen1, text="Email *").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Telephone *").pack()
    telephone_entry = Entry(screen1, textvariable=telephone)
    telephone_entry.pack()
    Button(screen1, text="Register", width=10, height=1,
           command=Register_User_Tradesman).pack()

    
def Register_User_Tradesman():
    ("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()
    


def Login_As_Tradesman():
    global screen42
    screen42 = Toplevel(screen)
    screen42.title("login")
    screen42.geometry("400x300")
    Label(screen42, text="Please enter details below to login").pack()
    Label(screen42, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen42, text="Username * ").pack()
    username_entry1 = Entry(screen42, textvariable=username_verify)
    username_entry1.pack()
    Label(screen42, text="password * ").pack()
    password_entry1 = Entry(screen42, textvariable=password_verify)
    password_entry1.pack()
    Label(screen42, text="").pack()
    Button(screen42, text="Login", width=10, height=1,
           command=login_verify_tradesman).pack()




def login_verify_tradesman():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            multiple_function_Tradesman()

    else:
            user_not_found()            
                
                            
def multiple_function_Tradesman():
    Welcome_Tradesman()
    delete_screens_tradesman()

def delete_screens_tradesman():
    screen42.destroy()
    screen8.destroy()



def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()

def delete4():
    screen5.destroy()
    return

    
#We adapted the Login System code from:
#https://www.youtube.com/watch?v=Xt6SqWuMSA8
#https://www.youtube.com/watch?v=Z-deSpgtIG0
#https://www.youtube.com/watch?v=OqfcGng4oKs&feature=youtu.be


def Welcome_Tradesman():
    global screen69
    screen69 = Tk()
    screen69.title("Welcome Tradesman")
    screen69.geometry("400x300")
    Label(screen69, text="Welcome Tradesman", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen69, text="Add Tools",command=addtools,height="2", width="30").pack()
    Label(text="").pack()
    Button(screen69, text="Edit Profile", command=openeditprofilewindowtradesman, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen69, text="Give Reviews", command=givereviews, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen69, text="Verify Tool Condition", command=verifytoolcondition, height="2", width="30").pack()
    Label(text="").pack()
    
    Button(screen69, text="Logout", command=Logout_Tradesman, height="2", width="30").pack()
    Label(text="").pack()


def addtools():
    global screen79
    screen79=Tk()
    screen79.title("Add tools")
    screen79.geometry("600x700")
    Label(screen79,text="Add tools",bg = "lightblue",
    width = "300", height = "2",font = ("Calibri", 13)).pack()

    global toolsspecification
    global price
    global addpicture
    global toolsspecification_entry
    global price_entry
    global addpicture_entry
    
    toolsspecification = StringVar()
    price = StringVar()
    addpicture = StringVar()

    Label(screen79, text = "Tools specification",height="2",width="20").pack()
    text=Text(screen79,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen79, text = "Special Notes about Tool",height="2",width="20").pack()
    text=Text(screen79,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen79, text = "Half day price * ").pack()
    price_entry = Entry(screen79, textvariable = price)
    e2=Entry(screen79)
    e2.pack()
    Label(screen79, text = "Full day price * ").pack()
    price_entry = Entry(screen79, textvariable = price)
    e2=Entry(screen79)
    e2.pack()

    def Upload_Picture():
        filename=filedialog.askopenfilename(initialdir="/",title="Select a File",filetype=(("jpeg","*.jpg"),("All files","*.*"))) 
        print(filename)
    
    Button(screen79, text = "Upload picture ", command=Upload_Picture,width = "15", height = "2").pack()
    Label(screen79, text = "").pack()
    Button(screen79, text = "Rent Tool",command=delete99, width = "10", height = "2").pack()
    Label(screen79, text = "").pack()
   

#Opening a file from desktop code has been adapted from:
#https://www.youtube.com/watch?v=BayLrEJytjI



def delete99():
    screen79.destroy()
    







def openeditprofilewindowtradesman():
    global screen122
    screen122 = Tk()
    screen122.geometry("500x450")
    screen122.title("Edit Profile")

   
    global firstname
    global lastname
    global age
    global address
    global phone
    global emailaddress
    global username
    global password
    global firstname_entry
    global lastname_entry
    global age_entry
    global address_entry
    global phone_entry
    global emailaddress_entry
    global username_entry
    global password_entry

    firstname = StringVar()
    lastname = StringVar()
    age = IntVar()
    phone = IntVar()
    address = StringVar()
    phone = StringVar()
    emailaddress = StringVar()

    Label(screen122, text="Edit Profile", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen122, text="Firstname * ").pack()
    firstname_entry = Entry(screen122, textvariable=firstname)
    e1 = Entry(screen122)
    e1.insert(10, "Knight")
    e1.pack()
    Label(screen122, text="Lastname * ").pack()
    lastname_entry = Entry(screen122, textvariable=lastname)
    e2 = Entry(screen122)
    e2.insert(10, "Coders")
    e2.pack()
    Label(screen122, text="Age * ").pack()
    age_entry = Entry(screen122, textvariable=age)
    e3 = Entry(screen122)
    e3.insert(10, "18 to 40")
    e3.pack()
    Label(screen122, text="Address * ").pack()
    address_entry = Entry(screen122, textvariable=address)
    e4 = Entry(screen122)
    e4.insert(10, "UK")
    e4.pack()
    Label(screen122, text="Phone * ").pack()
    phone_entry = Entry(screen122, textvariable=phone)
    e5 = Entry(screen122)
    e5.insert(10, "079576766")
    e5.pack()
    Label(screen122, text="Emailaddress * ").pack()
    emailaddress_entry = Entry(screen122, textvariable=emailaddress)
    e6 = Entry(screen122)
    e6.insert(10, "knightcoders@gmail")
    e6.pack()
    Label(screen122, text="UserName * ").pack()
    emailaddress_entry = Entry(screen122, textvariable=emailaddress)
    e6 = Entry(screen122)
    e6.insert(10, "Knight_Coders")
    e6.pack()
    Label(screen122, text="Password * ").pack()
    emailaddress_entry = Entry(screen122, textvariable=emailaddress)
    e6 = Entry(screen122)
    e6.insert(10, "1Knight.Coders1")
    e6.pack()
    Label(screen122, text="").pack()
    Button(screen122, text="Save", width="10", height="2").pack(side=RIGHT)
    Label(screen122, text="").pack()
    Button(screen122, text="Back", width="10", height="2").pack(side=LEFT)
    Label(screen122, text="").pack()


def givereviews():
    global screen133
    screen133 = Tk()
    screen133.geometry("400x400")
    Label(screen133, text="Give Reviews of Hirer", height="2", width="20").pack()
    text = Text(screen133, width=20, height=10, wrap=WORD, padx=10)
    text.pack()
    Button(screen133, text="Save",
           height="2", width="30").pack()



def verifytoolcondition():
    global screen321
    screen321=Tk()
    screen321.title("Verify Tool Condition")
    screen321.geometry("400x300")
    Label(screen321, text="Verify Tool Condition", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen321, text="Open my Tool Picture",command=opentoolpicture, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen321, text="Report to Administrator",command=Reporttoadministrator, height="2", width="30").pack()
    Label(text="").pack()


def opentoolpicture():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetype=(("jpeg", "*.jpg"), ("All files", "*.*")))
    print(filename)


#Opening a file from desktop code has been adapted from:
#https://www.youtube.com/watch?v=BayLrEJytjI






def Reporttoadministrator():
    global screen321
    screen321=Tk()
    screen321.title("Report to Administrator")
    screen321.geometry("300x300")
    Label(screen321, text="Report to Administrator", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen321, text="Write Complaint", height="2", width="20").pack()
    text = Text(screen321, width=20, height=10, wrap=WORD, padx=10)
    text.pack()
    Button(screen321, text = "Send Message", width = "10", height = "2").pack(side=BOTTOM)
    Label(screen321, text = "").pack()

  

def Logout_Tradesman():
    qExit = messagebox.askyesno("Tradesman", "Do you want to exit the system")
    if qExit > 0:
        screen69.destroy()
        return

#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/





###########################################################################............Hirer Section..........###########################################################################################################


def New_or_Existing_user_As_Hirer():
    global screen99
    screen99 = Tk()
    screen99.geometry("300x250")
    Button(screen99, text="New User", width="30", height="2",
           command=Register_As_Hirer, font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(screen99, text="Existing User", width="30", height="2"
           , command=Login_As_Hirer, font=("Calibri", 13)).pack()
    Label(text="").pack()


def Register_As_Hirer():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x400")

    global username
    global password
    global name
    global address
    global email
    global telephone
    global username_entry
    global password_entry
    global name_entry
    global address_entry
    global email_entry
    global telephone_entry
    username = StringVar()
    password = StringVar()
    name = StringVar()
    address = StringVar()
    email = StringVar()
    telephone = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="Age").pack()
    name_entry = Entry(screen1, textvariable=name)
    name_entry.pack()
    Label(screen1, text="Address *").pack()
    address_entry = Entry(screen1, textvariable=address)
    address_entry.pack()
    Label(screen1, text="Email *").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Telephone *").pack()
    telephone_entry = Entry(screen1, textvariable=telephone)
    telephone_entry.pack()
    Button(screen1, text="Register", width=10, height=1,
           command=Register_User_Hirer).pack()



def Register_User_Hirer():
    ("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()






def Login_As_Hirer():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("login")
    screen2.geometry("400x300")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1,
           command=login_verify_Hirer).pack()


def login_verify_Hirer():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            multiple_functions_hirer()

    else:
        user_not_found()

def multiple_functions_hirer():
    Welcome_Hirer()
    delete_screens_hirer()

def delete_screens_hirer():
    screen99.destroy()
    screen2.destroy()
    

#We adapted the Login System code from:
#https://www.youtube.com/watch?v=Xt6SqWuMSA8
#https://www.youtube.com/watch?v=Z-deSpgtIG0
#https://www.youtube.com/watch?v=OqfcGng4oKs&feature=youtu.be





def Welcome_Hirer():
    global screen66
    screen66 = Tk()
    screen66.title("Welcome Hirer")
    screen66.geometry("400x300")
    Label(screen66, text="Welcome Hirer", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen66, text="Select Tools", command=SelectTools,height="2", width="30").pack()
    Label(text="").pack()
    Button(screen66, text="Return Tools", command=Return_Tools, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen66, text="Give Reviews", command= Givereviews_to_Tradesman, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen66, text="Edit Profile", command=openeditprofilewindowhirer, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen66, text="Logout", command=Logout_Hirer, height="2", width="30").pack()
    Label(text="").pack()


def SelectTools():
    global screen177
    screen177 = Tk()
    screen177.title("Select Tools")
    screen177.geometry("600x600")
    Label(screen177, text="Select Tools", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen177, text="Cement Mixer",command=Cement_Mixer,height="2", width="30").pack()
    Label(text="").pack()
    Button(screen177, text="Hammer Drill Bosh",command=Hammer_Dril_Bosh,height="2", width="30").pack()
    Label(text="").pack()
    Button(screen177, text="Bosh Breaker",command=Bosh_Breaker,height="2", width="30").pack()
    Label(text="").pack()
    Button(screen177, text="Excavator",command=Excavator,height="2", width="30").pack()
    Label(text="").pack()
    Button(screen177, text="ForkLlift",command=Fork_Lift,height="2", width="30").pack()
    Label(text="").pack()

    

def Cement_Mixer():
    global screen1243
    screen1243 = Tk()
    screen1243.title("Cement Mixer")
    screen1243.geometry("800x800")
    Label(screen1243, text="Cement Mixer", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()

    can=Canvas(master=screen1243,width=300,height=250)
    can.pack(side="top")
    photo=PhotoImage(file="Cement Mixer.gif", master=can)
    can.create_image(150,220,anchor="s", image=photo)

#Adding Picture on Python Window code has been adapted from:
#https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item


    Label(screen1243, text="Tool Description", height="1", bd="1", font=("Calibri", 12),width="20",anchor="n").pack(side="top")
   
    Label(screen1243, text= """For mixing in bulk on the toughest of sites, heavy-duty site mixers are essential.
                                    Compact and portable for easy transportation.
                            Complete with barrow height swivel and stand.Fitted with Honda GX120
                                    EngineExtra thick drum with quick mix paddles.""", bd="1", font=("Calibri", 11),width="70", height="6", anchor="center").pack(side="top")
    
    Label(screen1243, text="Full Day Price and Half Day Price",height="2" ,bd="4",font=("Calibri", 12),width="25").pack()
    Entry(screen1243)
    e1 = Entry(screen1243)
    e1.insert(10, "£35.0/ £17.5")
    e1.pack()
   

    
    Label(screen1243, text="Choose Quantity", height="2", bd="4", font=("Calibri", 12),width="20").pack(side="top")
    var = StringVar(screen1243)
    var.set("") 
    
    w = Spinbox(master=screen1243, from_=0, to=100)
    w.pack()
    v=IntVar()

#Spinbox Code Adapted from 
#:https://effbot.org/tkinterbook/spinbox.html
#:https://www.tutorialspoint.com/python/tk_spinbox.htm
    
    
    Label(screen1243, text="Choose Distribution Method", height="2", bd="4", font=("Calibri", 12),width="30").pack(side="top")
    Radiobutton(screen1243, text="Pickup", font=("Calibri", 11), variable=v, value=1).pack(anchor="n")
    Radiobutton(screen1243, text="Delivery",font=("Calibri", 11), variable=v, value=2).pack(anchor="s")
    Button(screen1243, text="Choose Date", font=("Calibri", 11), command=PurchaseDate_CementMixer, height="2", width="20").pack(anchor="center")
    Label(text="").pack()
    mainloop()   

#Radio button Code Adapted from 
#:http://effbot.org/tkinterbook/radiobutton.htm





def PurchaseDate_CementMixer():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Purchase Date")
    
    Label(screen, text="Purchase Date", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    var = StringVar(screen)
    var.set("Year") 

    option = OptionMenu(screen, var,"2019")
    option.pack()

    var = StringVar(screen)
    var.set("month")

    option = OptionMenu(screen, var, "January","Feburary","March","April","May","June","July","August","September","October","November","December")
    option.pack()

    var = StringVar(screen)
    var.set("date")

    option = OptionMenu(screen, var, "1","2","3","4","5","6","7","8","9","10","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")              
    option.pack()

    
    Button(screen, text = "Next", command=Delivery_Adress_CementMixer,width = "10", height = "2").pack(side=RIGHT)
    Label(screen, text = "").pack()
    Button(screen, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen, text = "").pack()
    

def Delivery_Adress_CementMixer():
    global screen1
    screen1=Tk()
    screen1.title("Delivery Address")
    screen1.geometry("500x500")
    
    Label(screen1, text="Your Delivery Address and Notes from Tradesman", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()


    global deliveryaddress
    global deliveryaddress_entry

    deliveryaddress = StringVar()

    Label(screen1,text="Write Delivery Adress if required*",height="1",width="30",font=("Calibri", 12)).pack()
    text=Text(screen1,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen1, text="Notes from Tradesman", height="1", bd="1", font=("Calibri", 12),width="20",anchor="center").pack()
    
    Label(screen1, text= """The tool is in good condition, no scratches, it has been used for only 6 weeks.""", bd="1",
          font=("Calibri", 11),width="70", height="2", anchor="center").pack()
   

    Button(screen1, text = "Confirm Order", command=ConfirmOrder_CementMixer,width = "10", height = "2").pack(side=RIGHT)
    Label(screen1, text = "").pack()
    Button(screen1, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen1, text = "").pack()
    screen.mainloop()

def ConfirmOrder_CementMixer():
    Confirmorder=messagebox.askyesno("Hirer","You have to return the tool within 3 days of purchase date.Press Yes to Confirm Order")
    if Confirmorder>0:
        screen1.destroy()
        screen.destroy()
        screen1243.destroy()
        screen177.destroy()
        
    return

#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/



def Hammer_Dril_Bosh():
    global screen1264
    screen1264 = Tk()
    screen1264.title("Cement Mixer")
    screen1264.geometry("800x800")
    Label(screen1264, text="Hammer Drill Bosh", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()

    can=Canvas(master=screen1264,width=300,height=250)
    can.pack(side="top")
    photo=PhotoImage(file="HammerDrillBosh.gif", master=can)
    can.create_image(150,220,anchor="s", image=photo)

#Adding Picture on Python Window code has been adapted from:
#https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item

    
    Label(screen1264, text="Tool Description", height="1", bd="1", font=("Calibri", 12),width="20",anchor="n").pack(side="top")
   
    Label(screen1264, text= """A powerful corded hammer drill, perfect for drill in masonry, metal and wood.
                            High drilling rate and 30% higher chiselling performance than other rotary hammers in the entry-level class
                            Lightweight and compact, ideal for working overhead""", bd="1", font=("Calibri", 11),width="70", height="6", anchor="center").pack(side="top")

    Label(screen1264, text="Full Day Price and Half Day Price",height="2" ,bd="4",font=("Calibri", 12),width="25").pack()
    Entry(screen1264)
    e1 = Entry(screen1264)
    e1.insert(10, "£50.0/ £25.0")
    e1.pack()
   
       

    
    Label(screen1264, text="Choose Quantity", height="2", bd="4", font=("Calibri", 12),width="20").pack(side="top")
    var = StringVar(screen1264)
    var.set("") 
    
    w = Spinbox(master=screen1264, from_=0, to=100)
    w.pack()
    v=IntVar()

#Spinbox Code Adapted from 
#:https://effbot.org/tkinterbook/spinbox.html
#:https://www.tutorialspoint.com/python/tk_spinbox.htm
    
    Label(screen1264, text="Choose Distribution Method", height="2", bd="4", font=("Calibri", 12),width="30").pack(side="top")
    Radiobutton(screen1264, text="Pickup", font=("Calibri", 11), variable=v, value=1).pack(anchor="n")
    Radiobutton(screen1264, text="Delivery",font=("Calibri", 11), variable=v, value=2).pack(anchor="s")
    Button(screen1264, text="Choose Date", font=("Calibri", 11), command=PurchaseDate_HammerDrillBosh, height="2", width="20").pack(anchor="center")
    Label(text="").pack()
    mainloop()



#Radio Button Code Adapted from 
#:http://effbot.org/tkinterbook/radiobutton.htm


def PurchaseDate_HammerDrillBosh():
    global screen22
    screen22 = Tk()
    screen22.geometry("300x250")
    screen22.title("Purchase Date")
    
    Label(screen22, text="Purchase Date", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    var = StringVar(screen22)
    var.set("Year") # initial value

    option = OptionMenu(screen22, var,"2019")
    option.pack()

    var = StringVar(screen22)
    var.set("month") # initial value

    option = OptionMenu(screen22, var, "January","Feburary","March","April","May","June","July","August","September","October","November","December")
    option.pack()

    var = StringVar(screen22)
    var.set("date") # initial value

    option = OptionMenu(screen22, var, "1","2","3","4","5","6","7","8","9","10","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")              
    option.pack()

    
    Button(screen22, text = "Next", command=DeliveryAdress_HammerDrillBosh,width = "10", height = "2").pack(side=RIGHT)
    Label(screen22, text = "").pack()
    Button(screen22, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen22, text = "").pack()

def DeliveryAdress_HammerDrillBosh():
    global screen19
    screen19=Tk()
    screen19.title("Delivery Address")
    screen19.geometry("500x500")
    
    Label(screen19, text="Your Delivery Address and Notes from Tradesman", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()


    global deliveryaddress
    global deliveryaddress_entry

    deliveryaddress = StringVar()

    Label(screen19,text="Write Delivery Adress if required*",height="1",width="30",font=("Calibri", 12)).pack()
    text=Text(screen19,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen19, text="Notes from Tradesman", height="1", bd="1", font=("Calibri", 12),width="20",anchor="center").pack()
    
    Label(screen19, text= """The tool is in Ok condition, no damages, it has only been used for 9 months.""", bd="1",
          font=("Calibri", 11),width="70", height="2", anchor="center").pack()
   

    Button(screen19, text = "Confirm Order", command=ConfirmOrder_HammerDrillBosh,width = "10", height = "2").pack(side=RIGHT)
    Label(screen19, text = "").pack()
    Button(screen19, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen19, text = "").pack()
    screen.mainloop()    



def ConfirmOrder_HammerDrillBosh():
    Confirmorder=messagebox.askyesno("Hirer","You have to return the tool within 3 days of purchase date.Press Yes to Confirm Order")
    if Confirmorder>0:
        screen22.destroy()
        screen19.destroy()
        screen1264.destroy()
        screen177.destroy()
        
    return


#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/

def Bosh_Breaker():
    global screen1964
    screen1964 = Tk()
    screen1964.title("Bosh Breaker")
    screen1964.geometry("800x800")
    Label(screen1964, text="Bosh Breaker", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()

    can=Canvas(master=screen1964,width=300,height=250)
    can.pack(side="top")
    photo=PhotoImage(file="BoshBreaker.gif", master=can)
    can.create_image(150,220,anchor="s", image=photo)


#Adding Picture on Python Window code has been adapted from:
#https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item

    Label(screen1964, text="Tool Description", height="1", bd="1", font=("Calibri", 12),width="20",anchor="n").pack(side="top")
   
    Label(screen1964, text= """The most powerful electric breaker from Bosch.
                            Very low vibration (only 8.5 m/s²) thanks to the decoupled handle.
                            The vibration-reduced hammer mechanism – for a longer trigger time per day..""", bd="1",
          font=("Calibri", 11),width="70", height="6", anchor="center").pack(side="top")


    Label(screen1964, text="Full Day Price and Half Day Price",height="2" ,bd="4",font=("Calibri", 12),width="25").pack()
    Entry(screen1964)
    e1 = Entry(screen1964)
    e1.insert(10, "£35.0/ £17.5")
    e1.pack()
   
    
      

    
    Label(screen1964, text="Choose Quantity", height="2", bd="4", font=("Calibri", 12),width="20").pack(side="top")
    var = StringVar(screen1964)
    var.set("")
    
    w = Spinbox(master=screen1964, from_=0, to=100)
    w.pack()
    v=IntVar()

#SpinBox Code Adapted from 
#:https://effbot.org/tkinterbook/spinbox.html
#:https://www.tutorialspoint.com/python/tk_spinbox.htm



    Label(screen1964, text="Choose Distribution Method", height="2", bd="4", font=("Calibri", 12),width="30").pack(side="top")
    Radiobutton(screen1964, text="Pickup", font=("Calibri", 11), variable=v, value=1).pack(anchor="n")
    Radiobutton(screen1964, text="Delivery",font=("Calibri", 11), variable=v, value=2).pack(anchor="s")
    Button(screen1964, text="Confirm order", font=("Calibri", 11), command=PurchaseDate_BoshBbreaker, height="2", width="20").pack(anchor="center")
    Label(text="").pack()
    mainloop()   

def PurchaseDate_BoshBbreaker():
    global screen01
    screen01 = Tk()
    screen01.geometry("300x250")
    screen01.title("Purchase Date")
    
    Label(screen01, text="Purchase Date", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    var = StringVar(screen01)
    var.set("Year") 

    option = OptionMenu(screen01, var,"2019")
    option.pack()

    var = StringVar(screen01)
    var.set("month") 

    option = OptionMenu(screen01, var, "January","Feburary","March","April","May","June","July","August","September","October","November","December")
    option.pack()

    var = StringVar(screen01)
    var.set("date")

    option = OptionMenu(screen01, var, "1","2","3","4","5","6","7","8","9","10","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")              
    option.pack()

    
    Button(screen01, text = "Next", command=Delivery_Adress_BoshBreaker,width = "10", height = "2").pack(side=RIGHT)
    Label(screen01, text = "").pack()
    Button(screen01, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen01, text = "").pack()


def Delivery_Adress_BoshBreaker():
    global screen02
    screen02=Tk()
    screen02.title("Return Date and Delivery Address")
    screen02.geometry("500x500")
    
    Label(screen02, text="Return Date and Delivery Address", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    global deliveryaddress
    global deliveryaddress_entry

    deliveryaddress = StringVar()

    Label(screen02,text="Delivery Adress",height="1",width="15").pack()
    text=Text(screen02,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen02, text="Notes from Tradesman", height="1", bd="1", font=("Calibri", 12),width="20",anchor="center").pack()
    
    Label(screen02, text= """The tool is in Excellent condition,it has never been used""", bd="1",
          font=("Calibri", 11),width="70", height="2", anchor="center").pack()
   

    Button(screen02, text = "Confirm Order", command=ConfirmOrder_BoshBreaker,width = "10", height = "2").pack(side=RIGHT)
    Label(screen02, text = "").pack()
    Button(screen02, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen02, text = "").pack()
    screen.mainloop()


#Radio Button Code Adapted from 
#:http://effbot.org/tkinterbook/radiobutton.htm

def ConfirmOrder_BoshBreaker():
    Confirmorder=messagebox.askyesno("Hirer","Bosh Breaker is currently unavilable because its handle is damaged and it is being investigated by insurance company.We apologize for any inconveience.Press Yes and choose different tool")
    if Confirmorder>0:
        screen01.destroy()
        screen02.destroy()
        screen1964.destroy()
        screen177.destroy()
    return

#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/


def Excavator():
    global screen1994
    screen1994 = Tk()
    screen1994.title("Excavator")
    screen1994.geometry("800x800")
    Label(screen1994, text="Excavator", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()

    can=Canvas(master=screen1994,width=300,height=250)
    can.pack(side="top")
    photo=PhotoImage(file="Excavator.gif", master=can)
    can.create_image(150,220,anchor="s", image=photo)


#Adding Picture on Python Window code has been adapted from:
#https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item


    Label(screen1994, text="Tool Description", height="1", bd="1", font=("Calibri", 12),width="20",anchor="n").pack(side="top")
   
    Label(screen1994, text= """Range of tracked excavators available for moving large quantities
                            of earth and materials on building sites.
                            Well-protected hoses to minimise damage and downtime
                            Leading edge O-ring face sealing technology
                            Powerful, engine.""", bd="1", font=("Calibri", 11),width="70", height="6", anchor="center").pack(side="top")

    Label(screen1994, text="Full Day Price and Half Day Price",height="2" ,bd="4",font=("Calibri", 12),width="25").pack()
    Entry(screen1994)
    e1 = Entry(screen1994)
    e1.insert(10, "£350.0/ £175.0")
    e1.pack()
       
    Label(screen1994, text="Choose Quantity", height="2", bd="4", font=("Calibri", 12),width="20").pack(side="top")
    var = StringVar(screen1994)
    var.set("") 
    
    w = Spinbox(master=screen1994, from_=0, to=100)
    w.pack()
    v=IntVar()

#SpinBox Code Adapted from 
#:https://effbot.org/tkinterbook/spinbox.html
#:https://www.tutorialspoint.com/python/tk_spinbox.htm


    
    Label(screen1994, text="Choose Distribution Method", height="2", bd="4", font=("Calibri", 12),width="30").pack(side="top")
    Radiobutton(screen1994, text="Pickup", font=("Calibri", 11), variable=v, value=1).pack(anchor="n")
    Radiobutton(screen1994, text="Delivery",font=("Calibri", 11), variable=v, value=2).pack(anchor="s")
    Button(screen1994, text="Choose Date", font=("Calibri", 11), command=PurchaseDate_Excavator, height="2", width="20").pack(anchor="center")
    Label(text="").pack()
    mainloop()   
    


def PurchaseDate_Excavator():
    global screen71
    screen71 = Tk()
    screen71.geometry("300x250")
    screen71.title("Purchase Date")
    
    Label(screen71, text="Purchase Date", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    var = StringVar(screen71)
    var.set("Year") 

    option = OptionMenu(screen71, var,"2019")
    option.pack()

    var = StringVar(screen71)
    var.set("month") 

    option = OptionMenu(screen71, var, "January","Feburary","March","April","May","June","July","August","September","October","November","December")
    option.pack()

    var = StringVar(screen71)
    var.set("date") 

    option = OptionMenu(screen71, var, "1","2","3","4","5","6","7","8","9","10","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")              
    option.pack()

    
    Button(screen71, text = "Next", command=Delivery_Adress_Excavator,width = "10", height = "2").pack(side=RIGHT)
    Label(screen71, text = "").pack()
    Button(screen71, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen71, text = "").pack()


def Delivery_Adress_Excavator():
    global screen91
    screen91=Tk()
    screen91.title("Delivery Address")
    screen91.geometry("500x500")
    
    Label(screen91, text="Your Delivery Address and Notes from Tradesman", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()


    global deliveryaddress
    global deliveryaddress_entry

    deliveryaddress = StringVar()

    Label(screen91,text="Write Delivery Adress if required*",height="1",width="30",font=("Calibri", 12)).pack()
    text=Text(screen91,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen91, text="Notes from Tradesman", height="1", bd="1", font=("Calibri", 12),width="20",anchor="center").pack()
    
    Label(screen91, text= """Excavator is in working condition, it has been used for only 1 year.""", bd="1",
          font=("Calibri", 11),width="70", height="2", anchor="center").pack()
   

    Button(screen91, text = "Confirm Order", command=ConfirmOrder_Excavator,width = "10", height = "2").pack(side=RIGHT)
    Label(screen91, text = "").pack()
    Button(screen91, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen91, text = "").pack()
    screen.mainloop()    


#Radio Button Code Adapted from 
#:http://effbot.org/tkinterbook/radiobutton.htm


def ConfirmOrder_Excavator():
    Confirmorder=messagebox.askyesno("Hirer","You have to return the tool within 3 days of purchase date.Press Yes to Confirm Order")
    if Confirmorder>0:
        screen91.destroy()
        screen71.destroy()
        screen1994.destroy()
        screen177.destroy()
        
    return


#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/


def Fork_Lift():
    global screen1965
    screen1965 = Tk()
    screen1965.title("Fork Lift")
    screen1965.geometry("800x800")
    Label(screen1965, text="Fork Lift", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()

    can=Canvas(master=screen1965,width=300,height=250)
    can.pack(side="top")
    photo=PhotoImage(file="ForkLift.gif", master=can)
    can.create_image(150,220,anchor="s", image=photo)

#Adding Picture on Python Window code has been adapted from:
#https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item
    
    Label(screen1965, text="Tool Description", height="1", bd="1", font=("Calibri", 12),width="20",anchor="n").pack(side="top")
   
    Label(screen1965, text=  """Powered industrial truck which can be use to lift and move heavy pallets
                                  can lift pallets upto maximum height of 15 feets.
                                  Powerfull engine with automatic gears... """, bd="1", font=("Calibri", 11),width="70", height="6", anchor="center").pack(side="top")
    
    Label(screen1965, text="Full Day Price and Half Day Price",height="2" ,bd="4",font=("Calibri", 12),width="25").pack()
    Entry(screen1965)
    e1 = Entry(screen1965)
    e1.insert(10, "£80.0/ £40.0")
    e1.pack()
   
    
    Label(screen1965, text="Choose Quantity", height="2", bd="4", font=("Calibri", 12),width="20").pack(side="top")
    var = StringVar(screen1965)
    var.set("") 
    
    w = Spinbox(master=screen1965, from_=0, to=100)
    w.pack()
    v=IntVar()

#SpinBox Code Adapted from 
#:https://effbot.org/tkinterbook/spinbox.html
#:https://www.tutorialspoint.com/python/tk_spinbox.htm

    
    Label(screen1965, text="Choose Distribution Method", height="2", bd="4", font=("Calibri", 12),width="30").pack(side="top")
    Radiobutton(screen1965, text="Pickup", font=("Calibri", 11), variable=v, value=1).pack(anchor="n")
    Radiobutton(screen1965, text="Delivery",font=("Calibri", 11), variable=v, value=2).pack(anchor="s")
    Button(screen1965, text="Choose Date", font=("Calibri", 11), command=PurchaseDate_ForkLift, height="2", width="20").pack(anchor="center")
    Label(text="").pack()
    mainloop()   
   


def PurchaseDate_ForkLift():
    global screen08
    screen08 = Tk()
    screen08.geometry("300x250")
    screen08.title("Purchase Date")
    
    Label(screen08, text="Purchase Date", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    var = StringVar(screen08)
    var.set("Year") 

    option = OptionMenu(screen08, var,"2019")
    option.pack()

    var = StringVar(screen08)
    var.set("month")

    option = OptionMenu(screen08, var, "January","Feburary","March","April","May","June","July","August","September","October","November","December")
    option.pack()

    var = StringVar(screen08)
    var.set("date")

    option = OptionMenu(screen08, var, "1","2","3","4","5","6","7","8","9","10","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")              
    option.pack()

    
    Button(screen08, text = "Next", command=Delivery_Adress_ForkLift,width = "10", height = "2").pack(side=RIGHT)
    Label(screen08, text = "").pack()
    Button(screen08, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen08, text = "").pack()



def Delivery_Adress_ForkLift():
    global screen06
    screen06=Tk()
    screen06.title("Return Date and Delivery Address")
    screen06.geometry("600x600")
    
    Label(screen06, text="Return Date and Delivery Address", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    
    global deliveryaddress
    global deliveryaddress_entry

    deliveryaddress = StringVar()

    Label(screen06,text="Delivery Adress",height="1",width="15").pack()
    text=Text(screen06,width=20,height=10,wrap=WORD,padx=10)
    text.pack()
    Label(screen06, text="Notes from Tradesman", height="1", bd="1", font=("Calibri", 12),width="20",anchor="center").pack()
    
    Label(screen06, text= """Fork-Lift good condition, no mechanical issues and it has been used for only 2 weeks""", bd="1",
          font=("Calibri", 11),width="70", height="2", anchor="center").pack()
   

    Button(screen06, text = "Confirm Order", command=ConfirmOrder_ForkLift,width = "10", height = "2").pack(side=RIGHT)
    Label(screen06, text = "").pack()
    Button(screen06, text = "Back", width = "10", height = "2").pack(side=LEFT)
    Label(screen06, text = "").pack()
    screen.mainloop()

#Radio Button Code Adapted from 
#:http://effbot.org/tkinterbook/radiobutton.htm




def ConfirmOrder_ForkLift():
    Confirmorder=messagebox.askyesno("Hirer","You have to return the tool within 3 days of purchase date.Press Yes to Confirm Order")
    if Confirmorder>0:
        screen08.destroy()
        screen06.destroy()
        screen1965.destroy()
        screen177.destroy()
        
    return


#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/

def Givereviews_to_Tradesman():
    global screen139
    screen139 = Tk()
    screen139.geometry("400x400")
    Label(screen139, text="Give Reviews of Tradesman", height="2", width="20").pack()
    text = Text(screen139, width=20, height=10, wrap=WORD, padx=10)
    text.pack()
    Button(screen139, text="Save",
           height="2", width="30").pack()



def Return_Tools():
    global screen54
    screen54 = Tk()
    screen54.title("Return Tools")
    screen54.geometry("500x700")
    Label(screen54, text="Return Tools", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen54, text="Upload Picture", command=Upload_Picture,
           height="2", width="30").pack()
    Label(screen54, text="Write Notes", height="2", width="20").pack()
    text = Text(screen54, width=20, height=10, wrap=WORD, padx=10)
    text.pack()
   
    Button(screen54,text="Return",command=delete22,height="2",width="30").pack()

def delete22():
    screen54.destroy()


def Upload_Picture():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetype=(("jpeg", "*.jpg"), ("All files", "*.*")))
    print(filename)

#Uploading the file from desktop code has been adapted from:
#https://www.youtube.com/watch?v=BayLrEJytjI




def openeditprofilewindowhirer():
    global screen12
    screen12 = Tk()
    screen12.geometry("600x500")
    screen12.title("Edit Profile")

    global firstname
    global lastname
    global age
    global address
    global phone
    global emailaddress
    global firstname_entry
    global lastname_entry
    global age_entry
    global address_entry
    global phone_entry
    global emailaddress_entry

    firstname = StringVar()
    lastname = StringVar()
    age = IntVar()
    phone = IntVar()
    address = StringVar()
    phone = StringVar()
    emailaddress = StringVar()

    Label(screen12, text="Edit Profile", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen12, text="Firstname * ").pack()
    firstname_entry = Entry(screen12, textvariable=firstname)
    e1 = Entry(screen12)
    e1.insert(10, "Knight ")
    e1.pack()
    Label(screen12, text="Lastname * ").pack()
    lastname_entry = Entry(screen12, textvariable=lastname)
    e2 = Entry(screen12)
    e2.insert(10, "Coders")
    e2.pack()
    Label(screen12, text="Age * ").pack()
    age_entry = Entry(screen12, textvariable=age)
    e3 = Entry(screen12)
    e3.insert(10,"18 to 40")
    e3.pack()
    Label(screen12, text="Address * ").pack()
    address_entry = Entry(screen12, textvariable=address)
    e4 = Entry(screen12)
    e4.insert(10, "UK")
    e4.pack()
    Label(screen12, text="Phone * ").pack()
    phone_entry = Entry(screen12, textvariable=phone)
    e5 = Entry(screen12)
    e5.insert(10, "079576766")
    e5.pack()
    Label(screen12, text="Emailaddress * ").pack()
    emailaddress_entry = Entry(screen12, textvariable=emailaddress)
    e6 = Entry(screen12)
    e6.insert(10, "knightcoders@gmail")
    e6.pack()
    Label(screen12, text="").pack()
    Label(screen12, text="UserName * ").pack()
    emailaddress_entry = Entry(screen12, textvariable=emailaddress)
    e7 = Entry(screen12)
    e7.insert(10, "Knight Coders")
    e7.pack()
    Label(screen12, text="").pack()
    Label(screen12, text="Password * ").pack()
    emailaddress_entry = Entry(screen12, textvariable=emailaddress)
    e8 = Entry(screen12)
    e8.insert(10, "1knight_coders1")
    e8.pack()
    Label(screen12, text="").pack()
    Button(screen12, text="Save", width="10", height="2").pack(side=RIGHT)
    Label(screen12, text="").pack()
    Button(screen12, text="Back", width="10", height="2").pack(side=LEFT)
    Label(screen12, text="").pack()


def Logout_Hirer():
    qExit = messagebox.askyesno("Hirer", "Do you want to exit the system")
    if qExit > 0:
        screen66.destroy()
        return


#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/

###########################################################################............Administrator Section..........###########################################################################################################



def Login_As_Administrator():
    global screen42
    screen42 = Toplevel(screen)
    screen42.title("login")
    screen42.geometry("400x300")
    Label(screen42, text="Please enter details below to login").pack()
    Label(screen42, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen42, text="Username * ").pack()
    username_entry1 = Entry(screen42, textvariable=username_verify)
    username_entry1.pack()
    Label(screen42, text="password * ").pack()
    password_entry1 = Entry(screen42, textvariable=password_verify)
    password_entry1.pack()
    Label(screen42, text="").pack()
    Button(screen42, text="Login", width=10, height=1,
           command=login_verify_Administrator).pack()


def login_verify_Administrator():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
           multiple_screen_administrator()       
    else:
        user_not_found()

def multiple_screen_administrator():
    Welcome_Administrator()
    delete_screens_administrator()

def delete_screens_administrator():
    screen42.destroy()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()



def delete4():
    screen5.destroy()
    return
    

#We adapted the Login System code from:
#https://www.youtube.com/watch?v=Xt6SqWuMSA8
#https://www.youtube.com/watch?v=Z-deSpgtIG0
#https://www.youtube.com/watch?v=OqfcGng4oKs&feature=youtu.be






def Welcome_Administrator():
    global screen79
    screen79 = Tk()
    screen79.title("Welcome Administrator")
    screen79.geometry("400x300")
    Label(screen79, text="Welcome Administrator", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen79, text="Generate Monthly Invoice", command=Generate_Monthly_Invoice, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen79, text="Complaint From Tradesman", command=Complaintfromtradesman, height="2", width="30").pack()
    Label(text="").pack()
    Button(screen79, text="Logout", command=Logout_Administrator, height="2", width="30").pack()
    Label(text="").pack()
    




def Generate_Monthly_Invoice():
    global screen100
    screen100 = Tk()
    screen100.geometry("1450x1000")
    screen100.title("Welcome Administrator")

    global Tops
    global f1
    global f2
    global f2a

    Tops = Frame(screen100, width=600, height=80, bd=8, relief="raise")
    Tops.pack(side=TOP)

    f1 = Frame(screen100, width=600, height=650, bd=4, relief="raise")
    f1.pack(side=LEFT)
    f2 = Frame(screen100, width=400, height=650, bd=8, relief="raise")
    f2.pack(side=RIGHT)

    f1a = Frame(f1, width=450, height=330, bd=8, relief="raise")
    f1a.pack(side=TOP)
    f2a = Frame(f1, width=300, height=320, bd=8, relief="raise")
    f2a.pack(side=BOTTOM)

    global f1aa
    f1aa = Frame(f1a, width=450, height=430, bd=8, relief="raise")
    f1aa.pack(side=LEFT)

    global f1ab
    f1ab = Frame(f1a, width=450, height=430, bd=8, relief="raise")
    f1ab.pack(side=RIGHT)

    global f2aa
    f2aa = Frame(f2a, width=450, height=330, bd=8, relief="raise")
    f2aa.pack(side=LEFT)
    global f2ab
    f2ab = Frame(f2a, width=450, height=330, bd=8, relief="raise")
    f2ab.pack(side=LEFT)
    lblInfo = Label(Tops, font=('arial', 60, 'bold'), text="       Welcome Administrator           ", bd=10, anchor='w')
    lblInfo.grid(row=0, column=0)
    lblInvoiceDS = Label(f2, font=('arial', 12, 'bold'), text="Invoice Display", bd=2, anchor='w')
    lblInvoiceDS.grid(row=0, column=0, sticky=W)
    global txtInvoiceDS
    txtInvoiceDS = Text(f2, width=35, height=25, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtInvoiceDS.grid(row=1, column=0)

    # =============================== Calculator ==================

    global text_Input
    global PaymentRef
    global CementMixer
    global HammerDrillBosh
    global BoshBreaker
    global ForkLift
    global PaidTax
    global SubTotal
    global Insurance
    global Excavator
    global TotalCost
    global CostofCementMixer
    global CostofHammerDrillBosh
    global CostofBoshBreaker
    global CostofExcavator
    global CostofForkLift
    global CostofExcavator
    global DateofOrder
    global Delivery
    global LateFee

    text_Input = StringVar()
    operator = ""
    PaymentRef = StringVar()
    CementMixer = StringVar()
    HammerDrillBosh = StringVar()
    BoshBreaker = StringVar()
    Excavator = StringVar()
    ForkLift = StringVar()
    PaidTax = StringVar()
    SubTotal = StringVar()
    Insurance = StringVar()
    TotalCost = StringVar()
    CostofCementMixer = StringVar()
    CostofHammerDrillBosh = StringVar()
    CostofBoshBreaker = StringVar()
    CostofExcavator = StringVar()
    CostofForkLift = StringVar()
    DateofOrder = StringVar()

    CementMixer.set(0)
    HammerDrillBosh.set(0)
    BoshBreaker.set(0)
    Excavator.set(0)
    ForkLift.set(0)
    Insurance.set(1)
    Delivery = StringVar()
    Delivery.set(0)
    LateFee=StringVar()
    LateFee.set(0)

    global btnTotalCost
    btnTotalCost = Button(f2ab, padx=10, pady=10, bd=5, fg="black", font=('arial', 16, 'bold'), width=11,
                          text="Total Cost", command=CostofOrder).grid(row=0, column=0)
    global btnReference
    btnReference = Button(f2ab, padx=10, pady=10, bd=5, fg="black", font=('arial', 16, 'bold'), width=11,
                          text="Invoice Number", command=PayReference).grid(row=0, column=1)

    global btnDisplayInvoice
    global btnReset
    global btnExit
    global btnHomeCharge
    global btnChargeMinus
    global btnLateFee



#---------------------------------------------------- Other Information Button ---------------------------
    btnTotalCost=Button(f2ab, padx=10,pady=10,bd=5, fg="black", font=('arial', 16, 'bold'), width = 11,
                text="Total Cost", command=CostofOrder).grid(row=0, column=0)

    btnReference=Button(f2ab, padx=10,pady=10,bd=5, fg="black", font=('arial', 16, 'bold'), width = 12 ,
                text="Invoice Number ", command=PayReference).grid(row=0, column=1)

    btnDisplayInvoice=Button(f2, padx=8, pady=2, bd=6, fg="black", font=('arial',16,'bold'), width= 18,
                text="Display Invoice", command=InvoiceDS).grid(row=2, column=0,sticky=W )


    btnReset=Button(f2ab, padx=10,pady=10,bd=5, fg="black", font=('arial', 16, 'bold'), width = 11,
                text="Reset", command=Reset).grid(row=1, column=0,sticky=W+E)

    btnExit=Button(f2ab, padx=10,pady=10,bd=5, bg="light gray", fg="black", font=('arial', 16, 'bold'), width = 12,
                text="Exit", command=iExit).grid(row=1, column=1,sticky=W+E)



    btnHomeCharge=Button(f2ab, padx=10, pady=10, bd=5, fg="black", font=('arial',16,'bold'), width= 11,
                text="Delivery +",command=lambda: DeliveryCharge(False)).grid(row=0, column=2,sticky=W+E)
                                    

    btnHomeChargeMinus=Button(f2ab, padx=10, pady=10, bd=5, fg="black", font=('arial',16,'bold'), width= 11,
                text="Delivery -",command=lambda: DeliveryCharge(True)).grid(row=1, column=2,sticky=W+E)
                                    
    btnLateFeeP = Button(f2ab, padx=10, pady=10, bd=5, fg="black", font=('arial', 16, 'bold'), width = 11,
                           text="Late Fee +", command=lambda: LateFeeCharge(False)).grid(row=0, column=3, sticky=W + E)

    btnLateFeeM = Button(f2ab, padx=10, pady=10, bd=5, fg="black", font=('arial', 16, 'bold'), width = 11,
                               text="Late Fee -",command=lambda: LateFeeCharge(True)).grid(row=1, column=3)




    Reset()


# ============================================================ def CostofOrder ====================

def CostofOrder():
    global txtCementMixer
    global txtHammerDrillBosh
    global txtBoshBreaker
    global txtExcavator
    global txtForkLift
    global Insurance
    global txtPaidTax
    print(txtCementMixer.get())
    CementMixerPrice = float(0 if txtCementMixer.get() == "" else txtCementMixer.get())
    print(txtHammerDrillBosh.get())
    HammerDrillBoshPrice = float(0 if txtHammerDrillBosh.get() == "" else txtHammerDrillBosh.get())
    print(txtBoshBreaker.get())
    BoshBreakerPrice = float(0 if txtBoshBreaker.get() == "" else txtBoshBreaker.get())
    print(txtExcavator.get())
    ExcavatorPrice = float(0 if txtExcavator.get() == "" else txtExcavator.get())
    print(txtForkLift.get())
    ForkLiftPrice = float(0 if txtForkLift.get() == "" else txtForkLift.get())
    InsurancePrice = float(Insurance.get())


    print('called')
    DeliveryService = (Delivery.get())
    print(DeliveryService)

    print('called')
    LateFeeService = float(LateFee.get())
    print(LateFeeService)

    global CementMixerCost
    _cost_cement_mixer = (CementMixerPrice * 35.00)
    CementMixerCost = "£", str('%.2f' % (_cost_cement_mixer))
    global txtCostofCementMixer
    txtCostofCementMixer.delete(0, END)
    txtCostofCementMixer.insert(0, str(_cost_cement_mixer))
    
    global HammerDrillBoshCost
    _cost_Hammer_Drill_Bosh=(HammerDrillBoshPrice*50.00)
    HammerDrillBoshCost = "£", str('%.2f' % (_cost_Hammer_Drill_Bosh))
    global txtCostofHammerDrillBosh
    txtCostofHammerDrillBosh.delete(0, END)
    txtCostofHammerDrillBosh.insert(0, str(_cost_Hammer_Drill_Bosh))
    
    global BoshBreakerCost
    _cost_Bosh_Breaker = (BoshBreakerPrice* 35.00)
    BoshBreakerCost = "£", str('%.2f' % (_cost_Bosh_Breaker))
    global txtCostofBoshBreaker
    txtCostofBoshBreaker.delete(0, END)
    txtCostofBoshBreaker.insert(0, str(_cost_Bosh_Breaker))
   
    global ExcavatorCost
    _cost_Excavator = (ExcavatorPrice * 350.00)
    ExcavatorCost = "£", str('%.2f' % (_cost_Excavator))
    global txtCostofExcavator
    txtCostofExcavator.delete(0, END)
    txtCostofExcavator.insert(0, str(_cost_Excavator))
    
    global ForkLiftCost
    _cost_Fork_Lift = (ForkLiftPrice * 80.00)
    ForkLiftCost = "£", str('%.2f' % (_cost_Fork_Lift))
    global txtCostofForkLift
    txtCostofForkLift.delete(0, END)
    txtCostofForkLift.insert(0, str(_cost_Fork_Lift))
 

    _sub_total =  (CementMixerPrice * 35.00) + (HammerDrillBoshPrice * 50.00) + (BoshBreakerPrice * 35.00) + (
                    ExcavatorPrice * 350.00) + (ForkLiftPrice * 80.00)
    ToC = "£", str('%.2f' % (_sub_total))
    SubTotal.set(ToC)
    global txtSubTotal
    txtSubTotal.delete(0, END)
    txtSubTotal.insert(0, str(_sub_total))

    Tax = "£", str('%.2f' % (((CementMixerPrice * 35.00) + (HammerDrillBoshPrice * 50.00) + (
                BoshBreakerPrice * 35.00) + (ExcavatorPrice * 350.00) + (ForkLiftPrice * 80.00)) * 0.2))

    PaidTax.set(Tax)

    TaxPay = (((CementMixerPrice * 35.00) + (HammerDrillBoshPrice * 50.00) + (BoshBreakerPrice * 35.00) + (
                ExcavatorPrice * 350.00) + (ForkLiftPrice * 80.00)) * 0.2)
    txtPaidTax.delete(0, END)
    txtPaidTax.insert(0, str(TaxPay))

    Cost = ((CementMixerPrice * 35.00) + (HammerDrillBoshPrice * 50.00) + (BoshBreakerPrice * 35.00) + (
                ExcavatorPrice * 350.00) + (ForkLiftPrice * 80.00))
    Service = ((InsurancePrice * 5.00))
    
    print(DeliveryService)
    DeliveryC = (float(DeliveryService) * 8.00)

    print(LateFeeService)
    LateFeeP = (float(LateFeeService) * 660.00)

    _total = (TaxPay + Cost + Service + DeliveryC + LateFeeP)
    CostofItems = "£", str('%.2f' % _total)
    print(txtTotalCost.get())
    txtTotalCost.delete(0, END)
    txtTotalCost.insert(0,  str(_total))

    x = random.randint(10034, 699812)
    randomRef = str(x)
    global PaymentRef
    PaymentRef.set(" " + randomRef)


global PayReference


def PayReference():
    x = random.randint(10034, 699812)
    randomRef = str(x)
    global txtInvoicenumber
    print(txtInvoicenumber.get())
    txtInvoicenumber.delete(0, END)
    txtInvoicenumber.insert(0, " " + randomRef)


def iExit():
    qExit = messagebox.askyesno("Administrator", "Do you want to exit the system")
    if qExit > 0:
        screen100.destroy()
        return


#MessageBox Code has been adapted from:
#https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-10-messagebox/

def Reset():
    global PaymentRef
    global CementMixer
    global HammerDrillBosh
    global BoshBreaker
    global Excavator
    global Delivery
    global ForkLift
    global PaidTax
    global SubTotal
    global TotalCost
    global CostofCementMixer
    global CostofHammerDrillBosh
    global CostofBoshBreaker
    global CostofExcavator
    global CostofForkLift
    global LateFee

    # ----------------------------------------------(frame f1aa)-------------------------
    global f1aa
    lblInvoicenumber = Label(f1aa, font=('arial', 16, 'bold'), text="Invoice number", bd=16, justify='left')
    lblInvoicenumber.grid(row=0, column=0)
    global txtInvoicenumber
    txtInvoicenumber = Entry(f1aa, font=('arial', 16, 'bold'), text="", bd=10, insertwidth=2, justify='left')
    txtInvoicenumber.grid(row=0, column=1)

    lblCementMixer = Label(f1aa, font=('arial', 16, 'bold'), text="Cement Mixer", bd=16, justify='left')
    lblCementMixer.grid(row=1, column=0)
    global txtCementMixer
    txtCementMixer = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=CementMixer, bd=10, insertwidth=2,justify='left')
    txtCementMixer.grid(row=1, column=1)
    txtCementMixer.delete(0, END)
    txtCementMixer.insert(0, "0")

    lblHammerDrillBosh = Label(f1aa, font=('arial', 16, 'bold'), text="Hammer Drill Bosh", bd=16, justify='left')
    lblHammerDrillBosh.grid(row=2, column=0)
    global txtHammerDrillBosh
    txtHammerDrillBosh = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=HammerDrillBosh, bd=10, insertwidth=2,justify='left')
    txtHammerDrillBosh.grid(row=2, column=1)
    txtHammerDrillBosh.delete(0, END)
    txtHammerDrillBosh.insert(0, "0")


    lblBoshBreaker = Label(f1aa, font=('arial', 16, 'bold'), text="Bosh Breaker", bd=16, justify='left')
    lblBoshBreaker.grid(row=3, column=0)
    global txtBoshBreaker
    txtBoshBreaker = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=BoshBreaker, bd=10, insertwidth=2,justify='left')
    txtBoshBreaker.grid(row=3, column=1)
    txtBoshBreaker.delete(0, END)
    txtBoshBreaker.insert(0, "0")


    lblExcavator = Label(f1aa, font=('arial', 16, 'bold'), text="Excavator", bd=16, justify='left')
    lblExcavator.grid(row=4, column=0)
    global txtExcavator
    txtExcavator = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Excavator, bd=10, insertwidth=2, justify='left')
    txtExcavator.grid(row=4, column=1)
    txtExcavator.delete(0, END)
    txtExcavator.insert(0, "0")

    lblForkLift = Label(f1aa, font=('arial', 16, 'bold'), text="Fork-Lift", bd=16, justify='left')
    lblForkLift.grid(row=5, column=0)
    global txtForkLift
    txtForkLift = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=ForkLift, bd=10, insertwidth=2, justify='left')
    txtForkLift.grid(row=5, column=1)
    txtForkLift.delete(0, END)
    txtForkLift.insert(0, "0")



    # ----------------------------------------------(Tools in frame f2aa)--------------------------
    global f1ab
    lblDateofOrder = Label(f1ab, font=('arial', 16, 'bold'), text="Date of Order", bd=16, justify='left')
    lblDateofOrder.grid(row=0, column=0)
    global txtDateofOrder
    txtDateofOrder = Entry(f1ab, font=('arial', 16, 'bold'),bd=10, insertwidth=2,
                           justify='left')

    txtDateofOrder.delete(0, END)
    txtDateofOrder.insert(0, time.strftime("%d/%m/%Y"))

    txtDateofOrder.grid(row=0, column=1)
    lblCostofCementMixer = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Cement Mixer", bd=16, justify='left')
    lblCostofCementMixer.grid(row=1, column=0)
    global txtCostofCementMixer
    txtCostofCementMixer = Entry(f1ab, font=('arial', 16, 'bold'), bd=10, insertwidth=2,
                                 justify='left')
    txtCostofCementMixer.grid(row=1, column=1)
    lblCostofHammerDrillBosh = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Hammer Drill Bosh", bd=16,
                                     justify='left')
    lblCostofHammerDrillBosh.grid(row=2, column=0)
    global txtCostofHammerDrillBosh
    txtCostofHammerDrillBosh = Entry(f1ab, font=('arial', 16, 'bold'),bd=10,
                                     insertwidth=2, justify='left')
    txtCostofHammerDrillBosh.grid(row=2, column=1)
    lblCostofBoshBreaker = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Bosh Breaker", bd=16, justify='left')
    lblCostofBoshBreaker.grid(row=3, column=0)
    global txtCostofBoshBreaker
    txtCostofBoshBreaker = Entry(f1ab, font=('arial', 16, 'bold'), bd=10, insertwidth=2,
                                 justify='left')
    txtCostofBoshBreaker.grid(row=3, column=1)
    lblCostofExcavator = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Excavator", bd=16, justify='left')
    lblCostofExcavator.grid(row=4, column=0)
    global txtCostofExcavator
    txtCostofExcavator = Entry(f1ab, font=('arial', 16, 'bold'),bd=10, insertwidth=2,
                               justify='left')
    txtCostofExcavator.grid(row=4, column=1)
    lblCostofForkLift = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Fork-Lift", bd=16, justify='left')
    lblCostofForkLift.grid(row=5, column=0)
    global txtCostofForkLift
    txtCostofForkLift = Entry(f1ab, font=('arial', 16, 'bold'), bd=10, insertwidth=2,
                              justify='left')
    txtCostofForkLift.grid(row=5, column=1)
    # ------------------------------------------------------------ f2aa   ---------------------------------------------------
    global f2aa
    lblPaidTax = Label(f2aa, font=('arial', 16, 'bold'), text="Paid Vat", bd=8, width=12,anchor='w')
    lblPaidTax.grid(row=2, column=0)
    global txtPaidTax
    txtPaidTax = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=2,width=12, justify='left')
    txtPaidTax.grid(row=2, column=1)

    lblSubTotal = Label(f2aa, font=('arial', 16, 'bold'), text="Sub Total", width=12,bd=8, anchor='w')
    lblSubTotal.grid(row=3, column=0)
    global txtSubTotal
    txtSubTotal = Entry(f2aa, font=('arial', 16, 'bold'),bd=8, insertwidth=2, width=12,justify='left')
    txtSubTotal.grid(row=3, column=1)

    lblTotalCost = Label(f2aa, font=('arial', 16, 'bold'), text="Total Cost",width=12, bd=8, anchor='w')
    lblTotalCost.grid(row=4, column=0)
    global txtTotalCost
    txtTotalCost = Entry(f2aa, font=('arial', 16, 'bold'),bd=8, insertwidth=2, width=12,justify='left')
    txtTotalCost.grid(row=4, column=1)



# ----Invoice Display -----------------------------------------------------------------------------------

def DeliveryCharge(is_minus):
    current_delivery_cost = float(Delivery.get())
    if is_minus:
        if current_delivery_cost > 0:
            current_delivery_cost -= 1
    else:
        current_delivery_cost += 1
    Delivery.set(current_delivery_cost)

def LateFeeCharge(is_minus):
    current_LateFee_cost = float(LateFee.get())
    if is_minus:
        if current_LateFee_cost > 0:
            current_LateFee_cost -= 1
    else:
        current_LateFee_cost += 1
    LateFee.set(current_LateFee_cost)


global InvoiceDS

#Delivery Charge code has been adapted from StackOverFlow



def InvoiceDS():
    global txtInvoiceDS
    global txtInvoicenumber
    global txtDateofOrder
    global PaymentRef
    global SubTotalCost
    txtInvoiceDS.delete("1.0", END)
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set(" " + randomRef)
    txtInvoiceDS.insert(END, 'Invoice No.\t' + txtInvoicenumber.get() + "\n")
    txtInvoiceDS.insert(END, 'Date:\t' + txtDateofOrder.get() + "\n")
    txtInvoiceDS.insert(END, 'Items\t' + " Total Cost of Items \n\n")
    txtInvoiceDS.insert(END, 'Cement Mixer:\t\t' + txtCostofCementMixer.get() + "\n")
    txtInvoiceDS.insert(END, 'Hammer D/Bosh:\t\t'  + txtCostofHammerDrillBosh.get() + "\n")
    txtInvoiceDS.insert(END, 'Bosh Braker:\t\t'  + txtCostofBoshBreaker.get() + "\n")
    txtInvoiceDS.insert(END, 'Excavator:\t\t' + txtCostofExcavator.get() + "\n")
    txtInvoiceDS.insert(END, 'Fork Lift:\t\t' +txtCostofForkLift.get() + "\n\n")
    txtInvoiceDS.insert(END, 'VAT:\t\t' + txtPaidTax.get() + "\n")
    txtInvoiceDS.insert(END, 'Sub Total:\t\t' + txtSubTotal.get() + "\n")                                            
    DeliveryCost = "£" + str('%.2f' % ((float(Delivery.get()) * 8.00)))
    txtInvoiceDS.insert(END, 'Delivery Cost:\t\t(' + str(int(float(Delivery.get()))) + ')' + DeliveryCost + "\n\n")
    InsuranceCost = "£" + str('%.2f' % ((float(Insurance.get()) * 5.00)))
    txtInvoiceDS.insert(END, 'Insurance:\t\t' + InsuranceCost + "\n\n")
    LateFeeCost ="£"+ str('%.2f'%((float(LateFee.get()) * 660.00)))
    txtInvoiceDS.insert(END,'Late Fee(days):\t\t('+str(int(float(LateFee.get())))+')' + LateFeeCost + "\n\n")
    txtInvoiceDS.insert(END, 'Total Cost:\t\t' + txtTotalCost.get() + "\n\n")

  

    content = txtInvoiceDS.get('1.0', END)
    with open('invoices/' + PaymentRef.get() + '.txt', 'w') as f:
        f.write(content)


#Generate Monthly Invoice Code has been adapted from:
#https://www.youtube.com/watch?v=sHa827pDvnw
#https://www.youtube.com/watch?v=wTg7rOq8-2Y


def Complaintfromtradesman():
    global screen799
    screen799 = Tk()
    screen799.title("Complaint From Tradesman")
    screen799.geometry("400x400")
    Label(screen799, text="Complaint From Tradesman", bg="lightblue",
          width="300", height="2", font=("Calibri", 13)).pack()
    Button(screen799, text="Open Complaint File", command=opencomplaintfile, height="2", width="30").pack()
    Label(text="").pack()
    Label(screen799, text="Message Insurance Company", height="2", width="30").pack()
    text = Text(screen799, width=20, height=10, wrap=WORD, padx=10)
    text.pack()
    Button(screen799, text="Send Message",height="2", width="30").pack()
    Label(text="").pack()
    



def opencomplaintfile():
    file="Complaint File.txt"
    f=open(file,"r+")
    text=f.read()
    print(text)
    f.close()
    


#Opening complaint file code is adapted from:
#https://www.pythonforbeginners.com/cheatsheet/python-file-handling


def Logout_Administrator():
    qExit = messagebox.askyesno("Administrator", "Do you want to exit the system")
    if qExit > 0:
        screen79.destroy()
        return



Shared_Power_Window()





#..................................................................Code ends here..........................................................#










