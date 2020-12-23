# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:49:44 2020

@author: akanksha_pandey
"""

from tkinter import *
from tkinter.ttk import *
import sqlite3
import tkinter as tk
import pandas as pd
con=sqlite3.connect('database.db')
print("Opened database successfully")

def BookTickets():
    box.destroy()
    box1 = Tk(className='Trip')
    box1.geometry("500x500")

    def Oneway():
        box1 = Tk(className='Book Ticket')
        box1.geometry("800x500")
    
        Label(box1, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=1)
        Label(box1, text='Enter Name: ', font = ('Times New Roman', 10, 'bold',)).grid(row=1) 
        name1 = Entry(box1)
        name1.grid(row=1,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
        Label(box1, text='Enter Last 4 digits of Adhar Card number: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
        adhar1 = Entry(box1)
        adhar1.grid(row=3,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
        n = StringVar() 
        Label(box1, text='From: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5) 
        Source1 = Combobox(box1,height=5,textvariable=n, font = ('Times New Roman', 10, 'bold',))
        Source1['values'] = ('Ahemdabad',  
                            'Bangalore', 
                            'Chennai', 
                            'Dehradun', 
                            'Hyedrabad', 
                            'New Delhi',  
                            'Surat' 
                            )
        Source1.grid(row=5,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
        n1 = StringVar() 
        Label(box1, text='To: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7) 
        Destination1 = Combobox(box1,height=5,textvariable=n1, font = ('Times New Roman', 10, 'bold',))
        Destination1['values'] = ('Ahemdabad',  
                            'Bangalore', 
                            'Chennai', 
                            'Dehradun', 
                            'Hyedrabad', 
                            'New Delhi',  
                            'Surat' 
                            )
        Destination1.grid(row=7,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=9)
        n2 = StringVar() 
        Label(box1, text='Date: ', font = ('Times New Roman', 10, 'bold',)).grid(row=9)
        Date1 = Combobox(box1,height=5,textvariable=n2, font = ('Times New Roman', 10, 'bold',))
        Date1['values'] = ('11-October-2020',  
                            '12-October-2020', 
                            '13-October-2020', 
                            '14-October-2020',  
                            '15-October-2020' 
                            )
        Date1.grid(row=9,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=11)
        n3 = StringVar() 
        Label(box1, text='Time: ', font = ('Times New Roman', 10, 'bold',)).grid(row=11) 
        Time1 = Combobox(box1,height=5,textvariable=n3, font = ('Times New Roman', 10, 'bold',))
        Time1['values'] = ('10:00 am',  
                            '12:20 pm', 
                            '4:30 pm', 
                            '9:00 pm', 
                            '2:30 am' 
                            )
        Time1.grid(row=11,column=4)

        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=13)
        n5 = StringVar() 
        Label(box1, text='Class: ', font = ('Times New Roman', 10, 'bold',)).grid(row=13)
        Class1 = Combobox(box1,height=5,textvariable=n5, font = ('Times New Roman', 10, 'bold',))
        Class1['values'] = ('Economy',  
                            'Business',
                            'First-Class'
                            )
        Class1.grid(row=13,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=15)
        Label(box1, text='Enter Luggage weight: ', font = ('Times New Roman', 10, 'bold',)).grid(row=15) 
        weight1 = Entry(box1)
        weight1.grid(row=15,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=17)
        Label(box1, text='Money for extra weight: ', font = ('Times New Roman', 10, 'bold',)).grid(row=17) 
        
        def calcmon():
            weight = weight1.get()
            money = 0
            if int(weight)>20:
                money = 2 *int(weight)
                messagebox.showinfo("Money in Rupees",money)
            else:
                messagebox.showinfo("Money in Rupees","No extra money")
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=19)
        calmon = Button(box1, text ="Calculate money",command=calcmon).grid(row=19,column=4)

        def payment():
            
            name = name1.get()
            adhar = adhar1.get()
            Source = Source1.get()
            Destination = Destination1.get()
            Date = Date1.get()
            Time = Time1.get()
            Class = Class1.get()
            x = (adhar,name,Source,Destination,Date,Time)
            insert = con.cursor()
            if name=='' or adhar=='' or Source=='' or Destination == '' or Date == ''or Time == '' or Class =='':
                messagebox.showerror("Error","Please fill all the information!")
            else:
                box2 = Tk(className='Payment')
                box2.geometry("800x500")

                Label(box2, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=1)
                n10 = StringVar() 
                Label(box2, text='Payment Method: ', font = ('Times New Roman', 10, 'bold',)).grid(row=1) 
                Payment = Combobox(box2,height=5,textvariable=n10, font = ('Times New Roman', 10, 'bold',))
                Payment['values'] = ('Credit Card',  
                                    'Debit Card' 
                                    )
                Payment.grid(row=1,column=4)
            
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
                Label(box2, text='Enter Card number: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
                card1 = Entry(box2)
                card1.grid(row=3,column=4)
                
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
                Label(box2, text='CVV: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5) 
                cvv = Entry(box2)
                cvv.grid(row=5,column=4)
                
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
                Label(box2, text='OTP: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7) 
                cvv = Entry(box2)
                cvv.grid(row=7,column=4)

                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=10)
                Book2 = Button(box2, text ="Complete Payment",command=confirm).grid(row=10,column=4)
    


        def confirm():
            name = name1.get()
            adhar = adhar1.get()
            Source = Source1.get()
            Destination = Destination1.get()
            Date = Date1.get()
            Time = Time1.get()
            Class = Class1.get()
            x = (adhar,name,Source,Destination,Date,Time)
            insert = con.cursor()
            if name=='' or adhar=='' or Source=='' or Destination == '' or Date == ''or Time == '' or Class =='':
                messagebox.showerror("Error","Please fill all the information!")
            else:
                if Source == Destination:
                    messagebox.showerror("Error","Source can not be same as the destination!")
                else:
                    if Class == 'Economy':
                        insert.execute("insert into ECONOMY values(?,?,?,?,?,?)",x)
                        messagebox.showinfo("Payment Successful","Your Seat is Confirmed!")
                        con.commit()
                        box1.destroy()
                    if Class == 'Business':
                        insert.execute("insert into BUSINESS values(?,?,?,?,?,?)",x)
                        messagebox.showinfo("Payment Successful","Your Seat is Confirmed!")
                        con.commit()
                        box1.destroy()
                    if Class == 'First-Class':
                        insert.execute("insert into FIRST values(?,?,?,?,?,?)",x)
                        messagebox.showinfo("Payment Successful","Your Seat is Confirmed!")
                        con.commit()
                        box1.destroy()
        Label(box1, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=22)
        Book1 = Button(box1, text ="Pay",command=payment).grid(row=22,column=4)
        box1.mainloop()

    def Roundtrip():
        box1 = Tk(className='Book Ticket')
        box1.geometry("800x500")
        
        Label(box1, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=1)
        Label(box1, text='Enter Name: ', font = ('Times New Roman', 10, 'bold',)).grid(row=1) 
        name1 = Entry(box1)
        name1.grid(row=1,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
        Label(box1, text='Enter Adhar Card number: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
        adhar1 = Entry(box1)
        adhar1.grid(row=3,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
        n = StringVar() 
        Label(box1, text='From: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5) 
        Source1 = Combobox(box1,height=5,textvariable=n, font = ('Times New Roman', 10, 'bold',))
        Source1['values'] = ('Ahemdabad',  
                            'Bangalore', 
                            'Chennai', 
                            'Dehradun', 
                            'Hyedrabad', 
                            'New Delhi',  
                            'Surat' 
                            )
        Source1.grid(row=5,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
        n1 = StringVar() 
        Label(box1, text='To: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7) 
        Destination1 = Combobox(box1,height=5,textvariable=n1, font = ('Times New Roman', 10, 'bold',))
        Destination1['values'] = ('Ahemdabad',  
                            'Bangalore', 
                            'Chennai', 
                            'Dehradun', 
                            'Hyedrabad', 
                            'New Delhi',  
                            'Surat' 
                            )
        Destination1.grid(row=7,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=9)
        n2 = StringVar() 
        Label(box1, text='Date: ', font = ('Times New Roman', 10, 'bold',)).grid(row=9)
        Date1 = Combobox(box1,height=5,textvariable=n2, font = ('Times New Roman', 10, 'bold',))
        Date1['values'] = ('11-October-2020',  
                            '12-October-2020', 
                            '13-October-2020', 
                            '14-October-2020',  
                            '15-October-2020' 
                            )
        Date1.grid(row=9,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=11)
        n3 = StringVar() 
        Label(box1, text='Time: ', font = ('Times New Roman', 10, 'bold',)).grid(row=11) 
        Time1 = Combobox(box1,height=5,textvariable=n3, font = ('Times New Roman', 10, 'bold',))
        Time1['values'] = ('10:00 am',  
                            '12:20 pm', 
                            '4:30 pm', 
                            '9:00 pm', 
                            '2:30 am' 
                            )
        Time1.grid(row=11,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=13)
        n11 = StringVar() 
        Label(box1, text='ReturnDate: ', font = ('Times New Roman', 10, 'bold',)).grid(row=13)
        Date2 = Combobox(box1,height=5,textvariable=n11, font = ('Times New Roman', 10, 'bold',))
        Date2['values'] = ('11-October-2020',  
                            '12-October-2020', 
                            '13-October-2020', 
                            '14-October-2020',  
                            '15-October-2020' 
                            )
        Date2.grid(row=13,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=15)
        n12 = StringVar() 
        Label(box1, text='ReturnTime: ', font = ('Times New Roman', 10, 'bold',)).grid(row=15) 
        Time2 = Combobox(box1,height=5,textvariable=n12, font = ('Times New Roman', 10, 'bold',))
        Time2['values'] = ('10:00 am',  
                            '12:20 pm', 
                            '4:30 pm', 
                            '9:00 pm', 
                            '2:30 am' 
                            )
        Time2.grid(row=15,column=4)
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=17)
        n5 = StringVar() 
        Label(box1, text='Class: ', font = ('Times New Roman', 10, 'bold',)).grid(row=17)
        Class1 = Combobox(box1,height=5,textvariable=n5, font = ('Times New Roman', 10, 'bold',))
        Class1['values'] = ('Economy',  
                            'Business',
                            'First-Class'
                            )
        Class1.grid(row=17,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=19)
        Label(box1, text='Enter Luggage weight: ', font = ('Times New Roman', 10, 'bold',)).grid(row=19) 
        weight1 = Entry(box1)
        weight1.grid(row=19,column=4)
        
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=21)
        Label(box1, text='Money for extra weight: ', font = ('Times New Roman', 10, 'bold',)).grid(row=21) 
        
        def calcmon():
            weight = weight1.get()
            money = 0
            if int(weight)>20:
                money = 2 *int(weight)
                messagebox.showinfo("Money in Rupees",money)
            else:
                messagebox.showinfo("Money","No extra money!")
        Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=23)
        Book1 = Button(box1, text ="Calculate money",command=calcmon).grid(row=23,column=4)

        def payment():
            
            name = name1.get()
            adhar = adhar1.get()
            Source = Source1.get()
            Destination = Destination1.get()
            Date = Date1.get()
            Time = Time1.get()
            ReturnDate = Date2.get()
            ReturnTime = Time2.get()
            Class = Class1.get()
            x = (adhar,name,Source,Destination,Date,Time,ReturnDate,ReturnTime)
            insert = con.cursor()
            if name=='' or adhar=='' or Source=='' or Destination == '' or Date == ''or Time == '' or ReturnDate == '' or ReturnTime == '' or Class =='':
                 messagebox.showerror("Error","Please fill all the information!")
            else:
                box2 = Tk(className='Payment')
                box2.geometry("800x500")

                Label(box2, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=1)
                n10 = StringVar() 
                Label(box2, text='Payment Method: ', font = ('Times New Roman', 10, 'bold',)).grid(row=1) 
                Payment = Combobox(box2,height=5,textvariable=n10, font = ('Times New Roman', 10, 'bold',))
                Payment['values'] = ('Credit Card',  
                                    'Debit Card' 
                                    )
                Payment.grid(row=1,column=4)
            
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
                Label(box2, text='Enter Card number: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
                card1 = Entry(box2)
                card1.grid(row=3,column=4)
                
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
                Label(box2, text='CVV: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5) 
                cvv = Entry(box2)
                cvv.grid(row=5,column=4)
                
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
                Label(box2, text='OTP: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7) 
                cvv = Entry(box2)
                cvv.grid(row=7,column=4)
            
                Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=10)
                Book2 = Button(box2, text ="Complete Payment",command=confirm).grid(row=10,column=4)
    


        def confirm():
            name = name1.get()
            adhar = adhar1.get()
            Source = Source1.get()
            Destination = Destination1.get()
            Date = Date1.get()
            Time = Time1.get()
            ReturnDate = Date2.get()
            ReturnTime = Time2.get()
            Class = Class1.get()
            x = (adhar,name,Source,Destination,Date,Time,ReturnDate,ReturnTime)
            insert = con.cursor()
            if name=='' or adhar=='' or Source=='' or Destination == '' or Date == ''or Time == '' or ReturnDate == '' or ReturnTime == '' or Class =='':
                 messagebox.showerror("Error","Please fill all the information!")
            else:
                if Source == Destination:
                    messagebox.showerror("Error","Please fill all the information!")
                else:
                    if Class == 'Economy':
                        insert.execute("insert into ECONOMY1 values(?,?,?,?,?,?,?,?)",x)
                        messagebox.showinfo("Payment Successful","Your Seat is Confirmed!")
                        con.commit()
                        box1.destroy()
                    if Class == 'Business':
                        insert.execute("insert into BUSINESS1 values(?,?,?,?,?,?,?,?)",x)
                        messagebox.showinfo("Payment Successful","Your Seat is Confirmed!")
                        con.commit()
                        box1.destroy()
                    if Class == 'First-Class':
                        insert.execute("insert into FIRST1 values(?,?,?,?,?,?,?,?)",x)
                        messagebox.showinfo("Payment Successful","Your Seat is Confirmed!")
                        con.commit()
                        box1.destroy()
        Label(box1, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=25)
        Book1 = Button(box1, text ="Pay",command=payment).grid(row=25,column=4)
        box1.mainloop() 

    style = Style() 
    style.configure(style = 'TButton', font = ('Times New Roman', 10, 'bold',), borderwidth = '8', foreground = 'blue', width=50, height=50)
    label4 = Label(box1, text = " ", font = ('Times New Roman', 100, 'bold',)).pack()
    one = Button(box1, text ="One Way", command = Oneway).pack()
    round = Button(box1, text ="Round Trip", command = Roundtrip).pack()
    
def CancelTickets():
    box.destroy()
    box1 = Tk(className='Cancel Ticket: Please Verify Your identity!')
    box1.geometry("800x500")
    
    Label(box1, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=1)
    Label(box1, text='Enter Name: ', font = ('Times New Roman', 10, 'bold',)).grid(row=1) 
    name1 = Entry(box1)
    name1.grid(row=1,column=4)
    
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
    Label(box1, text='Enter Adhar Card number: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
    adhar1 = Entry(box1)
    adhar1.grid(row=3,column=4) 
    
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
    Label(box1, text='From: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5) 
    Source1 = Entry(box1)
    Source1.grid(row=5,column=4) 
    
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
    Label(box1, text='Date: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7) 
    Date1 = Entry(box1)
    Date1.grid(row=7,column=4) 
    
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=11)
    n5 = StringVar() 
    Label(box1, text='Class: ', font = ('Times New Roman', 10, 'bold',)).grid(row=11)
    Class1 = Combobox(box1,height=5,textvariable=n5, font = ('Times New Roman', 10, 'bold',))
    Class1['values'] = ('Economy',  
                          'Business',
                          'First-Class'
                          )
    Class1.grid(row=11,column=4)
    
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=13)
    n4 = StringVar() 
    Label(box1, text='Type: ', font = ('Times New Roman', 10, 'bold',)).grid(row=13) 
    Type1 = Combobox(box1,height=5,textvariable=n4, font = ('Times New Roman', 10, 'bold',))
    Type1['values'] = ('One-Way',  
                      'Round-Trip' 
                      )
    Type1.grid(row=13,column=4)
    
    
    def refund():
       messagebox.showinfo("Refund","Your Refund has been started.\n Please wait for 3-5 business days for confirmation.")
    def freeseat():
        messagebox.showinfo("Free Seat","Your Seat reservation has been cancelled.")  

    def validity():
        name = name1.get()
        adhar = adhar1.get()
        adhar=str(adhar)
        Source = Source1.get()
        Date = Date1.get()
        Class = Class1.get()
        Type = Type1.get()
        cur=con.cursor()
        con.commit()
        if name == '' or adhar == '' or Source == '':
            messagebox.showerror("Error","Please fill all the information!")
        else:
            if Type == 'One-Way':
                if Class == 'Economy':
                    cur.execute("delete from ECONOMY where (adhar=(?)) and (date=(?));",(adhar,Date,))
                    con.commit()
                    messagebox.showinfo("Cancel","your reservation is cancelled")

                
                if Class == 'Business':
                    cur.execute("delete from BUSINESS where (adhar=(?)) and (date=(?));",(adhar,Date,))
                    messagebox.showinfo("Cancel","your reservation is cancelled")
                    con.commit()
                    
                if Class == 'First-Class':
                    cur.execute("delete from FIRST where (adhar=(?)) and (date=(?));",(adhar,Date,))
                    messagebox.showinfo("Cancel","your reservation is cancelled")
                    con.commit()
            if Type == 'Round-Trip':
                if Class == 'Economy':
                    cur.execute("delete from ECONOMY1 where (adhar=(?)) and (date=(?));",(adhar,Date,))
                    con.commit()
                    messagebox.showinfo("Cancel","your reservation is cancelled")

                
                if Class == 'Business':
                    cur.execute("delete from BUSINESS1 where (adhar=(?)) and (date=(?));",(adhar,Date,))
                    messagebox.showinfo("Cancel","your reservation is cancelled")
                    con.commit()
                    
                if Class == 'First-Class':
                    cur.execute("delete from FIRST1 where (adhar=(?)) and (date=(?));",(adhar,Date,))
                    messagebox.showinfo("Cancel","your reservation is cancelled")
                    con.commit()
            refund()
            freeseat()
    
    Label(box1, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=17)
    Cancel1 = Button(box1, text ="Cancel",command=validity).grid(row=17,column=4)
    box1.mainloop()
    

    
def viewinfo():
    box.destroy()
    box1 = Tk(className='View information...')
    box1.geometry("800x500")
    
    def pasinfo():
        box2 = Tk(className='View information')
        box2.geometry("800x500")
        
        Label(box2, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
        Label(box2, text='Enter last 4 digits of Adhar Card number: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
        adhar1 = Entry(box2)
        adhar1.grid(row=3,column=4)
        
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
        n5 = StringVar() 
        Label(box2, text='Class: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5)
        Class1 = Combobox(box2,height=5,textvariable=n5, font = ('Times New Roman', 10, 'bold',))
        Class1['values'] = ('Economy',  
                          'Business',
                          'First-Class'
                          )
        Class1.grid(row=5,column=4)
        
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
        n2 = StringVar()
        Label(box2, text='Date: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7)
        Date1 = Combobox(box2,height=5,textvariable=n2, font = ('Times New Roman', 10, 'bold',))
        Date1['values'] = ('11-October-2020',  
                           '12-October-2020', 
                          '13-October-2020', 
                          '14-October-2020',  
                          '15-October-2020' 
                          )
        Date1.grid(row=7,column=4)
        
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=9)
        n4 = StringVar() 
        Label(box2, text='Type: ', font = ('Times New Roman', 10, 'bold',)).grid(row=9) 
        Type1 = Combobox(box2,height=5,textvariable=n4, font = ('Times New Roman', 10, 'bold',))
        Type1['values'] = ('One-Way',  
                      'Round-Trip' 
                      )
        Type1.grid(row=9,column=4)
        
        def info():
           
            adhar = adhar1.get()
            Class = Class1.get()
            Date = Date1.get()
            Type = Type1.get()
            cur=con.cursor()
        
            if adhar == '' or Date == '' or Class=='':
                messagebox.showerror("Error","Please fill all the information!")
            else:
                if Type == 'One-Way':
                    
                    if Class == 'Business':
                        
                        cur.execute("SELECT * FROM BUSINESS where (adhar=(?)) and (date=(?));",(adhar,Date,))
                        rows = cur.fetchall()
                        #pandas dataframe
                        df = pd.DataFrame(rows)
                        df.columns = ['Adhar', 'Name', 'Source', 'Destination', 'Date', 'Time']
                        list = df.to_numpy().tolist()
                        list1 =  (df.columns.values).tolist()
                        mydict={}
                        mydict['key1'] = list1
                        mydict['key2'] = list
                        messagebox.showinfo("Info",mydict)

                    if Class == 'Economy':
                        cur.execute("SELECT * FROM ECONOMY where (adhar=(?)) and (date=(?));",(adhar,Date,))
                        rows = cur.fetchall()
                        df = pd.DataFrame(rows)
                        df.columns = ['Adhar', 'Name', 'Source', 'Destination', 'Date', 'Time']
                        list = df.to_numpy().tolist()
                        list1 =  (df.columns.values).tolist()
                        mydict={}
                        mydict['key1'] = list1
                        mydict['key2'] = list
                        messagebox.showinfo("Info",mydict)
                        
                    if Class == 'First-Class':
                        
                        cur.execute("SELECT * FROM FIRST where (adhar=(?)) and (date=(?));",(adhar,Date,))
                        rows = cur.fetchall()
                        df = pd.DataFrame(rows)
                        df.columns = ['Adhar', 'Name', 'Source', 'Destination', 'Date', 'Time']
                        list = df.to_numpy().tolist()
                        list1 =  (df.columns.values).tolist()
                        mydict={}
                        mydict['key1'] = list1
                        mydict['key2'] = list
                        messagebox.showinfo("Info",mydict)
                    con.commit()
                    
                if Type == 'Round-Trip':
                    
                    if Class == 'Business':
                        
                        cur.execute("SELECT * FROM BUSINESS1 where (adhar=(?)) and (date=(?));",(adhar,Date,))
                        rows = cur.fetchall()
                        #pandas dataframe
                        df = pd.DataFrame(rows)
                        df.columns = ['Adhar', 'Name', 'Source', 'Destination', 'Date', 'Time','ReturnDate','ReturnTime']
                        list = df.to_numpy().tolist()
                        list1 =  (df.columns.values).tolist()
                        mydict={}
                        mydict['key1'] = list1
                        mydict['key2'] = list
                        messagebox.showinfo("Info",mydict)

                    if Class == 'Economy':
                        cur.execute("SELECT * FROM ECONOMY1 where (adhar=(?)) and (date=(?));",(adhar,Date,))
                        rows = cur.fetchall()
                        df = pd.DataFrame(rows)
                        df.columns = ['Adhar', 'Name', 'Source', 'Destination', 'Date', 'Time','ReturnDate','ReturnTime']
                        list = df.to_numpy().tolist()
                        list1 =  (df.columns.values).tolist()
                        mydict={}
                        mydict['key1'] = list1
                        mydict['key2'] = list
                        messagebox.showinfo("Info",mydict)
                        
                    if Class == 'First-Class':
                        
                        cur.execute("SELECT * FROM FIRST1 where (adhar=(?)) and (date=(?));",(adhar,Date,))
                        rows = cur.fetchall()
                        df = pd.DataFrame(rows)
                        df.columns = ['Adhar', 'Name', 'Source', 'Destination', 'Date', 'Time','ReturnDate','ReturnTime']
                        list = df.to_numpy().tolist()
                        list1 =  (df.columns.values).tolist()
                        mydict={}
                        mydict['key1'] = list1
                        mydict['key2'] = list
                        messagebox.showinfo("Info",mydict)
                    con.commit()
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=15)
        Button(box2, text ="View",command=info).grid(row=15,column=4)
        box2.mainloop()
    
    def flightinfo():
        box1.destroy()
        box2 = Tk(className='View information')
        box2.geometry("800x500")
        
        Label(box2, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=0)
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=3)
        Label(box2, text='Enter Source: ', font = ('Times New Roman', 10, 'bold',)).grid(row=3) 
        Source1 = Entry(box2)
        Source1.grid(row=3,column=4)
        
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=5)
        Label(box2, text='Enter Destination: ', font = ('Times New Roman', 10, 'bold',)).grid(row=5) 
        Destination1 = Entry(box2)
        Destination1.grid(row=5,column=4)
        
        Label(box2, text='', font = ('Times New Roman', 20, 'bold',)).grid(row=7)
        Label(box2, text='Enter Flight-id: ', font = ('Times New Roman', 10, 'bold',)).grid(row=7) 
        FID1 = Entry(box2)
        FID1.grid(row=7,column=4)
        
        def info():
            Source = Source1.get()
            Destination = Destination1.get()
            FID = FID1.get()
            cur=con.cursor()
            
            if Source == '' or Destination == '' or FID=='':
                messagebox.showerror("Error","Please fill all the information!")
            else:
                cur.execute("SELECT * FROM FLIGHT where (Source=(?)) and (Destination=(?)) and(FID=(?));",(Source,Destination,FID,))
                rows = cur.fetchall()
                con.commit()
                messagebox.showinfo("Info",rows)
                box2.destroy()

        Label(box2, text='', font = ('Times New Roman', 50, 'bold',)).grid(row=11)
        Button(box2, text ="View",command=info).grid(row=11,column=4)
        box2.mainloop()

    style = Style() 
    style.configure(style = 'TButton', font = ('Times New Roman', 10, 'bold',), borderwidth = '8', foreground = 'blue', width=50, height=50)
    label4 = Label(box1, text = " ", font = ('Times New Roman', 100, 'bold',)).pack()
    passenger = Button(box1, text='Passenger Information',command=pasinfo).pack()
    flight = Button(box1, text ="Flight Information",command=flightinfo).pack()
    box1.mainloop()
    
box = Tk(className='Welcome to Flight Reservation System')
box.geometry("800x500")
style = Style() 
style.configure(style = 'TButton', font = ('Times New Roman', 10, 'bold',), borderwidth = '8', foreground = 'blue', width=50, height=50)
label4 = Label(box, text = " ", font = ('Times New Roman', 100, 'bold',)).pack()
View = Button(box, text ="View Information",command=viewinfo).pack()
Book = Button(box, text ="Book Ticket",command=BookTickets).pack()
Cancel = Button(box, text ="Cancel Ticket",command=CancelTickets).pack()
box.mainloop()
con.close()