#made_by_sameer_kaushik
from Tkinter import*
import random
import time
import datetime
import smtplib
import socket
socket.getaddrinfo('localhost', 8080)

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('your email','password of email')        #enter your email and password in this line

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Billing System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Times',50,'bold'),text="CBPGEC RESTAURANT",fg="#00008B",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('Times',20,'bold'),text=localtime,fg="#8B2500",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

    
    if (Pizza.get()==""):
        CoPizza=0
    else:
        CoPizza=float(Pizza.get())


    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())


    if (Biryani.get()==""):
        CoBiryani=0
    else:
        CoBiryani=float(Biryani.get())

        
    if (Thaali.get()==""):
        CoThaali=0
    else:
        CoThaali=float(Thaali.get())

     
    if (Drinks.get()==""):
        CoDrinks=0
    else:
        CoDrinks=float(Drinks.get())


    if (Chips.get()==""):
        CoChips=0
    else:
        CoChips=float(Chips.get())


    if (Pasta.get()==""):
        CoPasta=0
    else:
        CoPasta=float(Pasta.get())


    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())

                   
    CostofBurger =CoBurger * 15
    CostofDrinks=CoDrinks * 20
    CostofPizza = CoPizza* 100
    CostofSandwich = CoSandwich * 25
    CostBiryani = CoBiryani* 30
    CostThaali=CoThaali * 50
    CostofChips=CoChips * 10
    CostofPasta=CoPasta * 40
    CostodNoodles=CoNoodles * 40

    CostofMeal= "Rs", str('%.2f' % (CostofBurger+CostofDrinks+CostofPizza+CostofSandwich+CostBiryani+CostThaali))

    PayGST=((CostofBurger+CostofDrinks+CostofPizza+CostofSandwich+CostBiryani+CostThaali) * 0.18)

    TotalCost=(CostofBurger+CostofDrinks+CostofPizza+CostofSandwich+CostBiryani+CostThaali+CostofChips)
 
    OverAllCost ="Rs", str ('%.2f' % (PayGST+TotalCost))

    PaidGST= "Rs", str ('%.2f' % PayGST)

    Cost.set(CostofMeal)
    GST.set(PaidGST)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Burger.set("")
    Pizza.set("")
    Sandwich.set("")
    Total.set("")
    Drinks.set("")
    GST.set("")
    Cost.set("")
    Biryani.set("")
    Thaali.set("")
    Chips.set("")
    Pasta.set("")
    Noodles.set("")

def email():
    eml=str(txtEmail.get())
    bn=str(txtBill_Number.get())
    btotal=str(txtTotalCost.get())
    ad=str(txtAdd.get())

    Subject="CBPGEC Canteen Billing System"
    a= "Subject:{}\n".format(Subject)
    b="\nBILL NO : {} \nTotal : {} \nAddress : {} \n".format(bn,btotal,ad)
    c="\n\nYou will receive your order within 30 minutes \n\n THANK YOU FOR ORDERING \n"
    content=a + b + localtime + c
    mail.sendmail('your email',eml ,content)        # enter your email in this line
    
#====================================Restaraunt Info ===========================================================
    
rand = StringVar()
Burger=StringVar()
Pizza=StringVar()
Sandwich=StringVar()
Chips=StringVar()
SubTotal=StringVar()
Total=StringVar()
Drinks=StringVar()
GST=StringVar()
Cost=StringVar()
Biryani=StringVar()
Thaali=StringVar()
Pasta=StringVar()
Noodles=StringVar()
Email=StringVar()
Address=StringVar()


lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=0, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=0,column=1)

lblPizza= Label(f1, font=('arial', 16, 'bold'),text="Pizza",bd=16,anchor="w")
lblPizza.grid(row=0, column=2)
txtPizza=Entry(f1, font=('arial',16,'bold'),textvariable=Pizza,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPizza.grid(row=0,column=3)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=0, column=4)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=0,column=5)

lblBiryani= Label(f1, font=('arial', 16, 'bold'),text="Biryani",bd=16,anchor="w")
lblBiryani.grid(row=1, column=0)
txtBiryani=Entry(f1, font=('arial',16,'bold'),textvariable=Biryani,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBiryani.grid(row=1,column=1)

lblThaali= Label(f1, font=('arial', 16, 'bold'),text="Thaali",bd=16,anchor="w")
lblThaali.grid(row=1, column=2)
txtThaali=Entry(f1, font=('arial',16,'bold'),textvariable=Thaali,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtThaali.grid(row=1,column=3)

lblPasta= Label(f1, font=('arial', 16, 'bold'),text="Pasta",bd=16,anchor="w")
lblPasta.grid(row=1, column=4)
txtPasta=Entry(f1, font=('arial',16,'bold'),textvariable=Pasta,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPasta.grid(row=1,column=5)

lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=2, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=2,column=3)

lblChips= Label(f1, font=('arial', 16, 'bold'),text="Chips",bd=16,anchor="w")
lblChips.grid(row=2, column=4)
txtChips=Entry(f1, font=('arial',16,'bold'),textvariable=Chips,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtChips.grid(row=2,column=5)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",fg="#006400",bd=16,anchor="w")
lblCost.grid(row=3, column=0)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=3,column=1)

lblGST= Label(f1, font=('arial', 16, 'bold'),text="GST",fg="#006400",bd=16,anchor="w")
lblGST.grid(row=3, column=2)
txtGST=Entry(f1, font=('arial',16,'bold'),textvariable=GST,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtGST.grid(row=3,column=3)

lblTotalCost= Label(f1, font=('arial', 20, 'bold'),text="Total Cost-->",fg="#006400",bd=16,anchor="w")
lblTotalCost.grid(row=3, column=4)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="#00FA9A",justify='right')
txtTotalCost.grid(row=3,column=5)

lblBill_Number= Label(f1, font=('arial', 16, 'bold'),text="Bill Number",bd=16,anchor="w")
lblBill_Number.grid(row=4, column=0)
txtBill_Number=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBill_Number.grid(row=4,column=1)

lblAdd= Label(f1, font=('arial', 16, 'bold'),text="Address",bd=16,anchor="w")
lblAdd.grid(row=4, column=2)
txtAdd=Entry(f1, font=('arial',16,'bold'),textvariable=Address,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtAdd.grid(row=4,column=3)

lblEmail= Label(f1, font=('arial', 16, 'bold'),text="E-mail",bd=16,anchor="w")
lblEmail.grid(row=4, column=4)
txtEmail=Entry(f1, font=('arial',16),textvariable=Email,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtEmail.grid(row=4,column=5)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="#00C957",command=Ref).grid(row=7,column=1)
btnMail=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Send E-mail",bg="#FFD700",command=email).grid(row=7,column=2)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="#3D59AB",command=Reset).grid(row=7,column=3)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="#FF3030",command=qExit).grid(row=7,column=5)
root.mainloop()
mail.close()
#made_by_sameer_kaushik
