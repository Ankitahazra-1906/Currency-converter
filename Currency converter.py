#importing the required modules
from tkinter import *
import tkinter.messagebox
from forex_python.converter import CurrencyRates
#setting up the window
window=Tk()
window.geometry("600x600")
window.title("currency converter")
window.config(bg="black")
#Adding a caption to the window
lbl=Label(window,text="CURRENCY CONVERTER",font="arial 25 bold",fg="white",bg="#7D0552").place(x=100,y=30)
#declaring the variables
var1=StringVar()
var2=StringVar()
var1.set("Currency")
var2.set("Currency")

def RealTimeCurrencyConversion():
    c=CurrencyRates()
    from_currency=var1.get()
    to_currency=var2.get()
    if (Amt.get()==""):
        tkinter.messagebox.showerror("Error!","Amount not entered \n Please enter a valid amount")
    elif(from_currency=="Currency" or to_currency=="Currency"):
        tkinter.messagebox.showerror("Error!","Currency not selected  \n Please select a currency code From and To Currency menu")
    else:
        new_amt=c.convert(from_currency,to_currency,float(Amt.get()))
        new_amount=float("{0:4f}".format(new_amt))
        ConvtAmt.insert(0,str(new_amount))

def RESET():
    Amt.delete(0,END)
    ConvtAmt.delete(0,END)
    var1.set("Currency")
    var2.set("Currency")



#list of the currency codes
curr_code_list=['USD','GBP', 'HKD', 'IDR', 'ILS', 'DKK', 'INR', 'CHF', 'MXN', 'CZK', 'SGD', 'THB', 'HRK', 'EUR', 'MYR', 'NOK', 'CNY', 'BGN', 'PHP', 'PLN', 'ZAR', 'CAD', 'ISK', 'BRL', 'RON', 'NZD', 'TRY', 'JPY', 'RUB', 'KRW', 'AUD', 'HUF', 'SEK']
#declaring all the required labels
lbl1=Label(window,text="Amount: ",font="garamound 20 bold",fg="white",bg="#F87217").place(x=50,y=100)
lbl2=Label(window,text="From Currency: ",font="garamound 20 bold",fg="white",bg="#F87217").place(x=50,y=170)
lbl3=Label(window,text="To Currency: ",font="garamound 20 bold",fg="white",bg="#F87217").place(x=50,y=220)
lbl4=Label(window,text="Converted Amount: ",font="garamound 20 bold",fg="white",bg="#F87217").place(x=50,y=380)
#creating dropdown currency list
FromCurrency_option=OptionMenu(window, var1, *curr_code_list).place(x=350,y=170,width=200)
ToCurrency_option=OptionMenu(window, var2, *curr_code_list).place(x=350,y=220,width=200)

Amt=Entry(window,width=25,font="bold")
Amt.grid(padx=350,pady=100,ipady=8)

ConvtAmt=Entry(window,width=25,font="bold")
ConvtAmt.grid(padx=350,pady=145,ipady=8)

ConvertBtn=Button(window,text="CONVERT",font="Helvetica 20 bold",fg="white",bg="#E41B17",command=RealTimeCurrencyConversion).place(x=230,y=290)
ResetBtn=Button(window,text="RESET",font="Helvetica 20 bold",fg="white",bg="dark blue",command=RESET).place(x=250,y=450)



window.mainloop()