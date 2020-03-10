import tkinter as tk
from tkinter import *
from tkinter import messagebox
#import Adafruit_ADS1x15
#from time import sleep
import time
import RPi.GPIO as GPIO
import smbus
import Adafruit_MCP4725
from w1thermsensor import W1ThermSensor

#adc = Adafruit_ADS1x15.ADS1115()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

sensor = 40 #for counter ir sensor
GPIO.setup(sensor,GPIO.IN)


#from time import*
var=int(0)
j=float(5)
x=int(5)
i=int(1)
var1=float(1)
var2=float(1)
var3=float(1)
tp=int(0)
start=int(0)
t=int(0)
q=float(1)
q1=float(1)
r=float(1)
i
pin=int(11)
u=0
start1=int(0)

countr= 0

startr = 0
endr = 0

highr=int(1)
sensor = W1ThermSensor()
################
dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
value=1
t=int(0)
inv=int(1)
bus=smbus.SMBus(1)
add=0x24
################
def temper():
    global q
    #value = adc.read_adc(0, gain=1)
    temperature=sensor.get_temperature()
    l03.config(text=temperature)
    root.after(500,temper)
    
def rpmi():
    f = open("r.txt", "r")
    #print(f.read())
    x=f.read()
    c=0
    if x!='':
        c=int(x)
    l13.config(text=c)
    root.after(1000,rpmi)         
def on():
    GPIO.output(16,True)
def off():
    
    GPIO.output(16,False)

def code1(value):

    # inform function to use external/global variable
    global pin

    if value == '*':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e1.delete('0', 'end')
        e1.insert('end', pin)

        if pin == "3529":
            print("PIN OK")
        else:
            print("PIN ERROR!", pin)
            # clear `pin`
            pin = ''
            # clear `entry`
            e1.delete('0', 'end')

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e1.insert('end', value)

    print("Current:", pin)

# --- main ---
pin = ''

def keypad1():
    win=tk.Toplevel(root)
    win.attributes("-topmost", True)
    win.title("temp")
    b11.config(state=DISABLED)
    def cc():
        b11.config(state=NORMAL)
        win.destroy()  
    keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['*', '0', '.'],    
    ]
    win.protocol("WM_DELETE_WINDOW",cc)

    
    # create global variable for pin
     # empty string

    
    # place to display pin
    
    
    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            # `lambda` inside `for` has to use `val=key:code(val)` 
            # instead of direct `code(key)`
            b = tk.Button(win, text=key, command=lambda val=key:code1(val))
            b.grid(row=y, column=x, ipadx=10, ipady=10)
def e1_delete():
    e1.delete(first=0,last=100)    

#################
def code2(value):

    # inform function to use external/global variable
    global pin

    if value == '*':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e2.delete('0', 'end')
        e2.insert('end', pin)

        if pin == "3529":
            print("PIN OK")
        else:
            print("PIN ERROR!", pin)
            # clear `pin`
            pin = ''
            # clear `entry`
            e2.delete('0', 'end')

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e2.insert('end', value)

    print("Current:", pin)

# --- main ---
pin = ''

def keypad2():
    win=tk.Toplevel(root)
    win.attributes("-topmost", True)
    win.title("rpm")
    b21.config(state=DISABLED)
    def cc2():
        b21.config(state=NORMAL)
        win.destroy()  
    keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['*', '0', '.'],    
    ]
    win.protocol("WM_DELETE_WINDOW",cc2)
  
    # create global variable for pin
     # empty string
    
    
    # place to display pin
    
    
    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            # `lambda` inside `for` has to use `val=key:code(val)` 
            # instead of direct `code(key)`
            b = tk.Button(win, text=key, command=lambda val=key:code2(val))
            b.grid(row=y, column=x, ipadx=10, ipady=10)
def e1_delete():
    e2.delete(first=0,last=100)    

#####################
def code3(value):

    # inform function to use external/global variable
    global pin

    if value == '*':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e3.delete('0', 'end')
        e3.insert('end', pin)

        if pin == "3529":
            print("PIN OK")
        else:
            print("PIN ERROR!", pin)
            # clear `pin`
            pin = ''
            # clear `entry`
            e3.delete('0', 'end')

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e3.insert('end', value)

    print("Current:", pin)

# --- main ---
pin = ''

def keypad3():
    win=tk.Toplevel(root)
    win.attributes("-topmost", True)
    win.title("clock")
    b31.config(state=DISABLED)
    def cc3():
        b31.config(state=NORMAL)
        win.destroy()  
    keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['*', '0', '.'],    
    ]
    win.protocol("WM_DELETE_WINDOW",cc3)

    # create global variable for pin
     # empty string
    
    
    # place to display pin
    
    
    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            # `lambda` inside `for` has to use `val=key:code(val)` 
            # instead of direct `code(key)`
            b = tk.Button(win, text=key, command=lambda val=key:code3(val))
            b.grid(row=y, column=x, ipadx=10, ipady=10)
def e1_delete():
    e3.delete(first=0,last=100)    

#####################

root = tk.Tk()
root.geometry("1024x600")
root.title("GUI TEST TUBE SPINNING MACHINE")
#root.overrideredirect(1)

def s():
    global start
    global tp
    global i
    i=0
    if(e1.get() and e2.get()!=''):
        start=time.time()
        print("***started***")
    else:
        messagebox.showwarning("Warning","No Target Inputs Given ")
    
def a():
    global i

    result=messagebox.askyesno("QUIT","Do you Want to Abort")
    if(result== True):
        global i
        i=2
    l31.config(text="0 min")
    
    
def e1_delete():
    e1.delete(first=0,last=100)


#frame1
f1 = tk.Frame(root, highlightbackground="DarkGrey", highlightcolor="Black", highlightthickness=1, width=10, height=30, bd= 0)
f1.place(relx=0,rely=0,relwidth=0.5,relheight=0.5)
f1.pack_propagate(False)
photo = PhotoImage(file =r"/home/pi/Desktop/gui/b2")
photoimage = photo.subsample(6,6)
b11=Button(f1,width='5',image = photoimage,command=keypad1)
b11.place(relx=0.4,rely=0.38,relwidth=0.07,relheight=0.1)
b12=Button(f1,text="CLC",width='5',command=e1_delete)
b12.place(relx=0.85,rely=0.38,relwidth=0.07,relheight=0.1)
l0=Label(f1,text="Temperature",fg='black',bd = '15' ,width=20,font=('Grunge 18 bold',25))
l0.pack(side= "top")
l01=Label(f1,text="Target:",fg='black',
                  bd = '15' ,
                   width=6,
          font='Humanist 18 bold',
                    padx=5, pady=5)
l01.place(relx=0.1, rely=0.32)
l02=Label(f1,text="Current:",fg='black',bd = '15',width=6,font='Humanist 18 bold',padx=5, pady=5)
l02.place(relx=0.1, rely=0.65)
e1=Entry(f1,bd=3,bg='white',width='15')
e1.place(relx=0.53,rely=0.4)
l03=Label(f1,text=var1,fg='Black',bg='AliceBlue',width='10',bd = '15',font='Humanist 20 bold',relief="groove",padx=3, pady=5)
l03.place(relx=0.4, rely=0.7)



def temp1():
    global var1
    try:       
        var1=float(e1.get())
        temp1="You have Entered : "+e1.get()+"°C"
        messagebox.showinfo("value",temp1)
    except:
        messagebox.showwarning("Warning","You have not Entered any value")

bs=Button(f1,text="set ",width='8', font='Humanist 10 bold',command=temp1)
bs.place(relx=0.84,rely=0.87)#set button temp

def e1_delete():
    e2.delete(first=0,last=100)

#frame2
f2 = tk.Frame(root, highlightbackground="DarkGrey", highlightcolor="red", highlightthickness=1, width=100, height=100, bd= 0)
f2.place(relx=0.5,rely=0,relwidth=0.5,relheight=0.5)
f1.pack_propagate(False)
photo = PhotoImage(file =r"/home/pi/Desktop/gui/b2")
photoimage1= photo.subsample(6,6)
b21=Button(f2,width='5',image = photoimage1,command=keypad2)
b21.place(relx=0.4,rely=0.38,relwidth=0.07,relheight=0.1)
b22=Button(f2,text="CLC",width='5',command=e1_delete)
b22.place(relx=0.85,rely=0.38,relwidth=0.07,relheight=0.1)
l1=Label(f2,text="R P M  ",fg='black',bd = '15',width=20,font=('Grunge 18 bold',25),padx=5, pady=5)
l1.pack(side="top")
l11=Label(f2,text="Target:",fg='black',bd = '15' ,width=6,font='Humanist 18 bold',padx=5, pady=5)
l11.place(relx=0.1, rely=0.32)
l12=Label(f2,text="Current:",fg='black',bd = '15' ,width=6,font='Humanist 18 bold',padx=5, pady=5)
l12.place(relx=0.1, rely=0.65)
e2=Entry(f2,bd=5,bg='white',width='15')
e2.place(relx=0.53,rely=0.4)
l13=Label(f2,text=var2,fg='Black',bg='AliceBlue',width='10',bd = '15',font='Humanist 20 bold',relief="groove", padx=4, pady=7.5)
l13.place(relx=0.4, rely=0.7)

def temp2():
    global var2
    try:       
        var2=float(e2.get())
        temp2="You have Entered : "+e2.get()+"Rpm"
        messagebox.showinfo("value",temp2)
    except:
        messagebox.showwarning("Warning","You have not selected any value")
bs1=Button(f2,text="set ",width='8',command=temp2,font='Humanist 10 bold')
bs1.place(relx=0.84,rely=0.87)#set button temp

        
def e1_delete():
    e3.delete(first=0,last=100)
#frame3

f3 = tk.Frame(root, highlightbackground="DarkGrey",highlightcolor="Black", highlightthickness=2, width=10, height=30, bd= 0)
f3.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.5)
l3=Label(f3,text="Time",fg="black",bd = '15' ,width=20,font=('Grunge 18 bold',25),padx=5, pady=5)
l3.pack(side="top")


e3=Entry(f3,bd=5,bg='white',width='15')
e3.place(relx=0.53,rely=0.4)

def temp3():
    global tp
    tp=float(e3.get())
    tp=tp*60
    global var3
    try:       
        var3=float(e3.get())
        temp3="You have Entered : "+e3.get()
        messagebox.showinfo("value",temp3)
    except:
        messagebox.showwarning("Warning","You have not Entered any value")

bs2=Button(f3,text="set ",width='8',command=temp3,font='Humanist 10 bold')
bs2.place(relx=0.84,rely=0.87)#set button temp

l31=Label(f3,text="0 min 0 sec",fg='Black',bg='AliceBlue',width='10',bd = '15',
          font='Humanist 20 bold',relief="groove",padx=4, pady=7.5)
l31.place(relx=0.4, rely=0.7)
photo = PhotoImage(file =r"/home/pi/Desktop/gui/b2")
photoimage2= photo.subsample(6,6)
b31=Button(f3,image = photoimage2,width='5',command=keypad3)
b31.place(relx=0.4,rely=0.38,relwidth=0.07,relheight=0.1)
b32=Button(f3,text="CLC",width='5',command=e1_delete)
b32.place(relx=0.85,rely=0.38,relwidth=0.07,relheight=0.1)
def clock():
    ttt=time.strftime('IST- %I:%M:%S %p',time.localtime())
    time.time
    if ttt!='':
        label1.config(text=ttt,font='times 20')
        
    root.after(500,clock)
label1=Label(f3,justify='center')
label1.place(relx=0.53,rely=0.01)
def c():
    global tp
    global var3
    global var31
    global var32
    global start
    global i
    global var1
    global var2
    global q
    global q1
    if(tp>0 and start+tp>time.time()and i==0):
        var3=int(tp+(start-time.time()))
        print("hello");
        print(var3)
        if(q<var1):
            GPIO.output(11,True)
        else:
            GPIO.output(11,False)
        if(q1<var2):
            GPIO.output(13,True)
        else:
            GPIO.output(13,False)
        rout=var2
        #rout=int(rout*0.273)
        rout=int(rout*2.1)
        dac.set_voltage(rout) 
        var31=int(var3/60)
        var32=var3%60
        l31.config(text=str(var31)+" m : "+str(var32)+" s")
        button2.config(state=DISABLED)
    elif(i==0):
        i=1
        print("ended ",(time.time()-start))
        button2.config(state=NORMAL)
        GPIO.output(11,False)
        GPIO.output(13,False)
        dac.set_voltage(0,False)
        f = open("r.txt", "w")
        f.write(str(0))
        f.close()
    
    elif(i==2):
        i=1
        print("ended ",(time.time()-start))
        button2.config(state=NORMAL)
        GPIO.output(11,False)
        GPIO.output(13,False)
        dac.set_voltage(0,False)
        f = open("r.txt", "w")
        f.write(str(0))
        f.close()
    root.after(500,c)#for 0.5 sec
    
temper()
c()
clock()
rpmi()
#frame4
f4 = tk.Frame(root, highlightbackground="DarkGrey",highlightcolor="Black", highlightthickness=1, width=10, height=30, bd= 0)
f4.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.5)
w = Label(f4, text= 'POWER ON\OFF SWITCH',fg="black",bd = '15' ,width=20,font='Grunge 15 bold',padx=5, pady=5,)
w.place(x=180,y=0)
root.configure(background = 'PeachPuff3')

button = tk.Button(f4,text="ABORT",fg="red",bg="BLACK",bd = '15',width=5,padx=5, pady=5,command=a)
button.pack(side=tk.LEFT)
button2 = tk.Button(f4,text="start",bd = '15' , width=5,padx=5, pady=5,command=s)
button2.pack(side=tk.LEFT)

button3 = tk.Button(f4,text="off",fg="blue",bg="RED", bd = '15' ,width=5, padx=5, pady=5,command=off)
button3.pack(side=tk.RIGHT)
button4 = tk.Button(f4,text="on",bd = '15' ,width=5,padx=5, pady=5,command=on)
button4.pack(side=tk.RIGHT)


root.update()
root.mainloop()
