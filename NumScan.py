from phonenumbers import geocoder
from phonenumbers import carrier
import requests
from threading import Thread
from tkinter import *
import phonenumbers
from time import sleep


window = Tk()
window.geometry('480x250')
window.config(background='black')
window.title("")

def Start():
    Thread(target=Checker).start()

def Checker():
    number = ent.get()
    numberCode = ent2.get()
    numberCountrycode = ent3.get()

    r = requests.get(
        f"http://146.148.112.105/caller/index.php/UserManagement/search_number?number={number}&country_code={numberCountrycode}")
    data = r.json()
    if ('"response":"0","msg":"Record found.') in r.text:
        for r in data['result']:
            name = Label(window, text='Name : '+r['name'], bg='black', fg='yellow').place(x=230,y=10)
            sleep(1)
            phoneNumber = Label(window, text='Phone number : '+r['number'],bg='black', fg='yellow').place(x=230,y=50)
            sleep(1)
            countryCode = Label(window, text='Country code : '+r['country_code'],bg='black', fg='yellow').place(x=230,y=90)
            sleep(1)
            id = Label(window, text='ID : '+r['id'],bg='black', fg='yellow').place(x=230,y=130)
            sleep(1)

            all1 = numberCode + number

            ro_number = phonenumbers.parse(all1, "en")

            Service = carrier.name_for_number(ro_number, "en")

            Gdd = geocoder.description_for_number(ro_number, "en")

            carrierr = Label(window, text='Carrier : '+Service, bg='black', fg='yellow').place(x=230,y=170)
            sleep(1)
            CountryName = Label(window, text='Country name : ' +Gdd, bg='black', fg='yellow').place(x=230, y=210)
            sleep(1)
    else:
        ErrorLabel = Label(window, text='Number Not Found', bg='black',fg='yellow').place(x=230,y=10)



button = Button(window, text='Start', width=5, height=1, font=10, command=Start)
button.place(x=15, y=200)

Number = Label(window, text='Number:', width=20)
Number.place(x=10, y=5)

NumberCode = Label(window, text='Country number code:ex.+966', width=23)
NumberCode.place(x=10, y=60)

NumberCountrycode = Label(window, text='Country Code:ex.SA', width=20)
NumberCountrycode.place(x=10, y=115)


ent = Entry(window, width=18)
ent.place(x=10, y=30)

ent2 = Entry(window, width=18)
ent2.place(x=10, y=85)

ent3 = Entry(window, width=18)
ent3.place(x=10, y=140)

window.mainloop()
