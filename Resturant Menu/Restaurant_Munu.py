from tkinter import*
import tkinter.messagebox
import random
import time;
import datetime as dt

root = Tk()
root.geometry('1350x750+0+0')
root.title('Restarant Menu')
root.configure(background='black')

Tops = Frame(root, width=1350, height=100,bd=14, relief='raise')
Tops.pack(side=TOP)

f1= Frame(root, width=900, height=650, bd=8, relief='raise')
f1.pack(side=LEFT)

f2= Frame(root, width=440, height=650,bd=8,relief='raise')
f2.pack(side=RIGHT)


f1a= Frame(f1, width=900, height=330,bd=8,relief='raise')
f1a.pack(side=TOP)

f2a= Frame(f1, width=900, height=320,bd=6,relief='raise')
f2a.pack(side=BOTTOM)

ft2= Frame(f2, width=440, height=450,bd=12,relief='raise')
ft2.pack(side=TOP)
fb2= Frame(f2, width=440, height=250,bd=16,relief='raise')
fb2.pack(side=BOTTOM)


f1aa= Frame(f1a, width=400, height=330,bd=16,relief='raise')
f1aa.pack(side=LEFT)
f1ab= Frame(f1a, width=400, height=330,bd=16,relief='raise')
f1ab.pack(side=RIGHT)

f2aa= Frame(f2a, width=450, height=320,bd=14,relief='raise')
f2aa.pack(side=RIGHT)
f2ab= Frame(f2a, width=450, height=320,bd=14,relief='raise')
f2ab.pack(side=LEFT)


Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')


lblInfo = Label(Tops , font=('arial',70,'bold'),text='   Restuarant Management System   ',bd=10)
lblInfo.grid(row=0,column=0)
#============================================Methods====================================

def ReceiptTotal():
    txtReceipt.delete('1.0',END)
    x = random.randint(0,500876)
    randomRef = str(x)
    Receipt.set('BILL' + randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t' + Receipt.get() +'\t\t' + DataOfOrder.get()+'\n')
    txtReceipt.insert(END,'items\t\t\t\t\t' +'Cost Of Item \n\n')
    txtReceipt.insert(END,'Coffe: \t\t\t\t\t' + E_Coffe.get()+'\n')
    txtReceipt.insert(END, 'Pepsi: \t\t\t\t\t' + E_Pepsi.get() + '\n')
    txtReceipt.insert(END, 'Fanta: \t\t\t\t\t' + E_Fanta.get() + '\n')
    txtReceipt.insert(END, 'Thums_Up: \t\t\t\t\t' + E_Thums_up.get() + '\n')
    txtReceipt.insert(END, 'Red_Bull: \t\t\t\t\t' + E_Red_Bull.get() + '\n')
    txtReceipt.insert(END, 'Lamonade: \t\t\t\t\t' + E_Lemonade.get() + '\n')
    txtReceipt.insert(END, 'SparklingWater: \t\t\t\t\t' + E_SparklingWater.get() + '\n')
    txtReceipt.insert(END, 'Water: \t\t\t\t\t' + E_Water.get() + '\n')
    txtReceipt.insert(END, 'Shahi_Paneer: \t\t\t\t\t' + E_Shahi_Paneer.get() + '\n')
    txtReceipt.insert(END, 'Paneer_Butter_Masala: \t\t\t\t\t' + E_Paneer_Butter_Masala.get() + '\n')
    txtReceipt.insert(END, 'Mix_Vegetable: \t\t\t\t\t' + E_Mix_Vegitable.get() + '\n')
    txtReceipt.insert(END, 'Chicken_Do_Pyaza: \t\t\t\t\t' + E_Chicken_Do_Pyaza.get() + '\n')
    txtReceipt.insert(END, 'Chicken_Butter_Masala: \t\t\t\t\t' + E_Chicken_Butter_Masala.get() + '\n')
    txtReceipt.insert(END, 'Chicken_Kolhapuri: \t\t\t\t\t' + E_Chicken_Kolhapuri.get() + '\n')
    txtReceipt.insert(END, 'Chicken_Munchurian: \t\t\t\t\t' + E_Chicken_Munchurian.get() + '\n')
    txtReceipt.insert(END, 'Chicken_Garlic: \t\t\t\t\t' + E_Chicken_Garlic.get() + '\n')
    txtReceipt.insert(END, 'Cost Of Drink: \t\t' + CostOfTheDrink.get()+'\t Tax Paid:\t\t'+PaidTax.get() + '\n')
    txtReceipt.insert(END, 'Cost Of Food: \t\t' + CostOfTheFood.get() + '\t SubTotal:\t\t' + SubTotal.get() + '\n')
    txtReceipt.insert(END, 'Service Charge: \t\t' + ServiceCharge.get() + '\t Total:\t\t' + Total.get() + '\n')


def qExit():
    qExit= tkinter.messagebox.askyesno('Quit System','Do you waant to Quit?')
    if qExit > 0:
        root.destroy()
        return

def Reset():
    PaidTax.set('')
    SubTotal.set('')
    Total.set('')
    CostOfTheDrink.set('')
    CostOfTheFood.set('')
    ServiceCharge.set('')
    txtReceipt.delete('1.0',END)

    E_Coffe.set('0')
    E_Pepsi.set('0')
    E_Fanta.set('0')
    E_Thums_up.set('0')
    E_Red_Bull.set('0')
    E_Lemonade.set('0')
    E_SparklingWater.set('0')
    E_Water.set('0')


    E_Shahi_Paneer.set('0')
    E_Paneer_Butter_Masala.set('0')
    E_Mix_Vegitable.set('0')
    E_Chicken_Do_Pyaza.set('0')
    E_Chicken_Butter_Masala.set('0')
    E_Chicken_Kolhapuri.set('0')
    E_Chicken_Munchurian.set('0')
    E_Chicken_Garlic.set('0')

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')


    txtCoffe.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtThums_up.configure(state=DISABLED)
    txtRed_Bull.configure(state=DISABLED)
    txtLemonade.configure(state=DISABLED)
    txtSparklingWater.configure(state=DISABLED)
    txtWater.configure(state=DISABLED)
    txtShahi_Paneer.configure(state=DISABLED)
    txtPaneer_Butter_Masala.configure(state=DISABLED)
    txtMix_Vegitable.configure(state=DISABLED)
    txtChicken_Do_Pyaza.configure(state=DISABLED)
    txtChicken_Butter_Masala.configure(state=DISABLED)
    txtChicken_Kolhapuri.configure(state=DISABLED)
    txtChicken_Munchurian.configure(state=DISABLED)
    txtChicken_Garlic.configure(state=DISABLED)

#============================================Veriable====================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DataOfOrder=StringVar()
Receipt=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
Total=StringVar()
CostOfTheDrink=StringVar()
CostOfTheFood=StringVar()
ServiceCharge=StringVar()



E_Coffe = StringVar()
E_Pepsi= StringVar()
E_Fanta =StringVar()
E_Thums_up=StringVar()
E_Red_Bull=StringVar()
E_Lemonade=StringVar()
E_SparklingWater=StringVar()
E_Water=StringVar()
E_Shahi_Paneer=StringVar()
E_Paneer_Butter_Masala=StringVar()
E_Mix_Vegitable=StringVar()
E_Chicken_Do_Pyaza=StringVar()
E_Chicken_Butter_Masala=StringVar()
E_Chicken_Kolhapuri=StringVar()
E_Chicken_Munchurian=StringVar()
E_Chicken_Garlic=StringVar()

DataOfOrder.set(time.strftime('%d/%m/%Y'))


E_Coffe.set('0')
E_Pepsi.set('0')
E_Fanta.set('0')
E_Thums_up.set('0')
E_Red_Bull.set('0')
E_Lemonade.set('0')
E_SparklingWater.set('0')
E_Water.set('0')
E_Shahi_Paneer.set('0')
E_Paneer_Butter_Masala.set('0')
E_Mix_Vegitable.set('0')
E_Chicken_Do_Pyaza.set('0')
E_Chicken_Butter_Masala.set('0')
E_Chicken_Kolhapuri.set('0')
E_Chicken_Munchurian.set('0')
E_Chicken_Garlic.set('0')


#=========================================================CheckButton==================================

def chkbutton_value():
    if(var1.get() == 1):
        txtCoffe.configure(state=NORMAL)
    elif var1.get()==0:
        txtCoffe.configure(state=DISABLED)
        E_Coffe.set('0')
    if (var2.get() == 1):
        txtPepsi.configure(state=NORMAL)
    elif var2.get() == 0:
        txtPepsi.configure(state=DISABLED)
        E_Pepsi.set('0')
    if (var3.get() == 1):
        txtFanta.configure(state=NORMAL)
    elif var3.get() == 0:
        txtFanta.configure(state=DISABLED)
        E_Fanta.set('0')
    if (var4.get() == 1):
        txtThums_up.configure(state=NORMAL)
    elif var4.get() == 0:
        txtThums_up.configure(state=DISABLED)
        E_Thums_up.set('0')
    if (var5.get() == 1):
        txtRed_Bull.configure(state=NORMAL)
    elif var5.get() == 0:
        txtRed_Bull.configure(state=DISABLED)
        E_Red_Bull.set('0')
    if (var6.get() == 1):
        txtLemonade.configure(state=NORMAL)
    elif var6.get() == 0:
        txtLemonade.configure(state=DISABLED)
        E_Lemonade.set('0')
    if (var7.get() == 1):
        txtSparklingWater.configure(state=NORMAL)
    elif var7.get() == 0:
        txtSparklingWater.configure(state=DISABLED)
        E_SparklingWater.set('0')
    if (var8.get() == 1):
        txtWater.configure(state=NORMAL)
    elif var8.get() == 0:
        txtWater.configure(state=DISABLED)
        E_Water.set('0')
    if (var9.get() == 1):
        txtShahi_Paneer.configure(state=NORMAL)
    elif var9.get() == 0:
        txtShahi_Paneer.configure(state=DISABLED)
        E_Shahi_Paneer.set('0')
    if (var10.get() == 1):
        txtPaneer_Butter_Masala.configure(state=NORMAL)
    elif var10.get() == 0:
        txtPaneer_Butter_Masala.configure(state=DISABLED)
        E_Paneer_Butter_Masala.set('0')
    if (var11.get() == 1):
        txtMix_Vegitable.configure(state=NORMAL)
    elif var11.get() == 0:
        txtMix_Vegitable.configure(state=DISABLED)
        E_Mix_Vegitable.set('0')
    if (var12.get() == 1):
        txtChicken_Do_Pyaza.configure(state=NORMAL)
    elif var12.get() == 0:
        txtChicken_Do_Pyaza.configure(state=DISABLED)
        E_Chicken_Do_Pyaza.set('0')
    if (var13.get() == 1):
        txtChicken_Butter_Masala.configure(state=NORMAL)
    elif var13.get() == 0:
        txtChicken_Butter_Masala.configure(state=DISABLED)
        E_Chicken_Butter_Masala.set('0')
    if (var14.get() == 1):
        txtChicken_Kolhapuri.configure(state=NORMAL)
    elif var14.get() == 0:
        txtChicken_Kolhapuri.configure(state=DISABLED)
        E_Chicken_Kolhapuri.set('0')
    if (var15.get() == 1):
        txtChicken_Munchurian.configure(state=NORMAL)
    elif var15.get() == 0:
        txtChicken_Munchurian.configure(state=DISABLED)
        E_Chicken_Munchurian.set('0')
    if (var16.get() == 1):
        txtChicken_Garlic.configure(state=NORMAL)
    elif var16.get() == 0:
        txtChicken_Garlic.configure(state=DISABLED)
        E_Chicken_Garlic.set('0')

#============================================CostOfTheItem

def CostOfItem():
    item1=float(E_Coffe.get())
    item2=float(E_Pepsi.get())
    item3=float(E_Fanta.get())
    item4=float(E_Thums_up.get())
    item5=float(E_Red_Bull.get())
    item6=float(E_Lemonade.get())
    item7=float(E_SparklingWater.get())
    item8=float(E_Water.get())


    item9=float(E_Shahi_Paneer.get())
    item10=float(E_Paneer_Butter_Masala.get())
    item11=float(E_Mix_Vegitable.get())
    item12=float(E_Chicken_Do_Pyaza.get())
    item13=float(E_Chicken_Butter_Masala.get())
    item14=float(E_Chicken_Kolhapuri.get())
    item15=float(E_Chicken_Munchurian.get())
    item16=float(E_Chicken_Garlic.get())

    CostOfDrink = (item1 * 1.2) + (item2 * 1.99) + (item3 * 2.05) \
                    +(item4 * 1.89) + (item5 * 1.99) + (item6 * 2.99) + (item7 * 2.39) + (item8 * 1.29)

    CostOfFood = (item9 * 1.35) + (item10 * 2.2) + (item11 * 1.99) \
                   + (item12 * 1.49) + (item13 * 1.8) + (item14 * 1.67) + (item15 * 1.6) + (item16 * 1.99)


    FoodsPrice = '£',str('%.2f'%(CostOfFood))
    CostOfTheFood.set(FoodsPrice)
    DrinkPrice = '£', str('%.2f' % (CostOfDrink))
    CostOfTheDrink.set(DrinkPrice)
    SC='£',str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalOfITEMS='£',str('%.2f'%(CostOfDrink + CostOfFood + 1.59))
    SubTotal.set(SubTotalOfITEMS)

    Tax='£',str('%.2f'%((CostOfDrink + CostOfFood + 1.59)*0.15))
    PaidTax.set(Tax)
    TT = ((CostOfDrink + CostOfFood + 1.59)*0.15)
    TC = '£',str('%.2f'%(CostOfDrink + CostOfFood + 1.59 + TT))
    Total.set(TC)













#=========================================================CheckButton==================================
var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)




#=============================Drink===================#

Coffe= Checkbutton(f1aa,text='Coffe \t', variable = var1, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 0, sticky=W)

Pepsi= Checkbutton(f1aa,text='Pepsi \t\t', variable = var2, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 1, sticky=W )
Fanta= Checkbutton(f1aa,text='Fanta \t\t', variable = var3, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 2, sticky=W )
Thums_up= Checkbutton(f1aa,text='Thums up \t\t', variable = var4, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 3, sticky=W )
Red_Bull= Checkbutton(f1aa,text='RedBull \t\t', variable = var5, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 4, sticky=W )
Lemonade= Checkbutton(f1aa,text='Lemonade \t\t', variable = var6, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 5, sticky=W )
SparklingWater= Checkbutton(f1aa,text='SparklingWater \t\t', variable = var7, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 6, sticky=W )
Water= Checkbutton(f1aa,text='Water \t\t', variable = var8, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 7, sticky=W )

#=============================Food===================#

Shahi_Paneer= Checkbutton(f1ab,text='Shahi_Paneer \t', variable = var9, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 0, sticky=W )

Paneer_Butter_Masala= Checkbutton(f1ab,text='Paneer_Butter_Masala \t', variable = var10, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 1, sticky=W )
Mix_Vegitable= Checkbutton(f1ab,text='Mix_Vegitable \t', variable = var11, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 2, sticky=W )
Chicken_Do_Pyaza= Checkbutton(f1ab,text='Chicken_Do_Pyaza \t', variable = var12, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 3, sticky=W )
Chicken_Butter_Masala= Checkbutton(f1ab,text='Chicken_Butter_Masala \t', variable = var13, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 4, sticky=W )
Chicken_Kolhapuri= Checkbutton(f1ab,text='Chicken_Kolhapuri \t', variable = var14, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 5, sticky=W )
Chicken_Munchurian= Checkbutton(f1ab,text='Chicken_Munchurian \t', variable = var15, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 6, sticky=W )
Chicken_Garlic= Checkbutton(f1ab,text='Chicken_Garlic \t', variable = var16, onvalue= 1, offvalue = 0,
                   font=('arial',18,'bold'),command=chkbutton_value).grid(row = 7, sticky=W )

#=============================Widget For Drinks===================#


txtCoffe = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Coffe ,state=DISABLED)
txtCoffe.grid(row=0,column=1)
txtPepsi = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Pepsi ,state=DISABLED)
txtPepsi.grid(row=1,column=1)
txtFanta = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Fanta ,state=DISABLED)
txtFanta.grid(row=2,column=1)
txtThums_up = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Thums_up ,state=DISABLED)
txtThums_up.grid(row=3,column=1)
txtRed_Bull = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Red_Bull ,state=DISABLED)
txtRed_Bull.grid(row=4,column=1)
txtLemonade = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Lemonade ,state=DISABLED)
txtLemonade.grid(row=5,column=1)
txtSparklingWater = Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_SparklingWater ,state=DISABLED)
txtSparklingWater.grid(row=6,column=1)
txtWater= Entry(f1aa,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Water ,state=DISABLED)
txtWater.grid(row=7,column=1)




#=============================Widget For Food===================

txtShahi_Paneer = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Shahi_Paneer ,state=DISABLED)
txtShahi_Paneer.grid(row=0,column=1)
txtPaneer_Butter_Masala = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Paneer_Butter_Masala ,state=DISABLED)
txtPaneer_Butter_Masala.grid(row=1,column=1)
txtMix_Vegitable = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Mix_Vegitable ,state=DISABLED)
txtMix_Vegitable.grid(row=2,column=1)
txtChicken_Do_Pyaza = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Chicken_Do_Pyaza ,state=DISABLED)
txtChicken_Do_Pyaza.grid(row=3,column=1)
txtChicken_Butter_Masala = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Chicken_Butter_Masala,state=DISABLED)
txtChicken_Butter_Masala.grid(row=4,column=1)
txtChicken_Kolhapuri = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Chicken_Kolhapuri,state=DISABLED)
txtChicken_Kolhapuri.grid(row=5,column=1)
txtChicken_Munchurian = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Chicken_Munchurian ,state=DISABLED)
txtChicken_Munchurian.grid(row=6,column=1)
txtChicken_Garlic = Entry(f1ab,font=('arial',16,'bold'),bd=8 , width=6, justify='left',textvariable=E_Chicken_Garlic ,state=DISABLED)
txtChicken_Garlic.grid(row=7,column=1)

#=============================Information===================

lblReceipt = Label(ft2,font=('arial',12,'bold'),text='Receipt:',bd=2,anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt= Text(ft2,bd=8 , width=59,bg='white',font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)

#=============================Cost Of The Item Information===================

lblCostOfTheDrink = Label(f2ab,font=('arial',16,'bold'),text='Cost Of The Drink:',bd=8)
lblCostOfTheDrink.grid(row=2,column=0,sticky=W)
txtCostOfTheDrink = Entry(f2ab,font=('arial',16,'bold'), bd=8, justify='left', insertwidth=2,textvariable=CostOfTheDrink)
txtCostOfTheDrink.grid(row=2,column=1,sticky=W)

lblCostOfTheFood = Label(f2ab,font=('arial',16,'bold'),text='Cost Of The Food:',bd=8)
lblCostOfTheFood.grid(row=3,column=0,sticky=W)
txtCostOfTheFood = Entry(f2ab,font=('arial',16,'bold'), bd=8, justify='left', insertwidth=2,textvariable=CostOfTheFood)
txtCostOfTheFood.grid(row=3,column=1,sticky=W)

lblServiceCharge = Label(f2ab,font=('arial',16,'bold'),text='Service Charge:',bd=8)
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge = Entry(f2ab,font=('arial',16,'bold'), bd=8, justify='left', insertwidth=2,textvariable=ServiceCharge)
txtServiceCharge.grid(row=4,column=1,sticky=W)




#=============================Payment Information===================

lblPaidTax = Label(f2aa,font=('arial',16,'bold'),text='Paid Tax:',bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax = Entry(f2aa,font=('arial',16,'bold'), bd=8, justify='left', insertwidth=2, textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1,sticky=W)

lblSubTotal = Label(f2aa,font=('arial',16,'bold'),text='Sub Total:',bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal  = Entry(f2aa,font=('arial',16,'bold'), bd=8, justify='left', insertwidth=2,textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1,sticky=W)

lblTotal = Label(f2aa,font=('arial',16,'bold'),text='Total:',bd=8)
lblTotal.grid(row=4,column=0,sticky=W)
txtTotal = Entry(f2aa,font=('arial',16,'bold'), bd=8, justify='left', insertwidth=2,textvariable=Total)
txtTotal.grid(row=4,column=1,sticky=W)



#=============================Button===================#

btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,
                text='Total',command=CostOfItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial,',16,'bold'),width=5,
                text='Receipt',command=ReceiptTotal).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,
                text='Reset',command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,
                text='Exit',command=qExit).grid(row=0,column=3)



root.mainloop()