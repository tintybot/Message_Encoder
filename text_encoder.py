#!/usr/bin/env python
# coding: utf-8
#a gui to send an x-bit encoded text via whatsapp or email
#importing dependencies
from selenium import webdriver
from tkinter import *
import smtplib
import time

#+x encoding to the text message
def encoder(text):
    strr=""
    for i in range(0,len(text)):
        if ord(text[i])>=97 and ord(text[i])<=122:
            ch=ord(text[i])-96
            ch=ch+ch+96
            if ch>122:
                ch=ch-122+96
            strr=strr+chr(int(ch))
        elif ord(text[i])>=65 and ord(text[i])<=90:
            ch=ord(text[i])-64
            ch=ch+ch+64
            if ch>90:
                ch=ch-90+64
            strr=strr+chr(int(ch))
        else:
            strr=strr+text[i]
    return (strr)


#sending message to reciever via whatsapp
def sendmssg():
    msg=str(encoder(text))
    rec=str(recv.get())
    recv_entry.delete(0,END)
    
    ### whatsapp 
    driver = webdriver.Chrome("C:\\Users\\KIIT\\Downloads\\chromedriver.exe")
    driver.get('http://web.whatsapp.com')
    target=f'"{rec}"'
    time.sleep(15)
    user=driver.find_element_by_xpath('//*[contains(@title, ' + target + ')]')
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')
    #you can loop over to text bomb
    #i am not responsible if anyone blocks you
    for i in range(1):
        msg_box.send_keys(msg)
        driver.find_element_by_class_name('_3M-N-').click()
    ###
    screen3.destroy()
    
#gui for whatsapp
def encoder_whatsapp():
    global screen3
    global text
    screen3=Toplevel(screen)
    screen3.geometry("300x150")
    screen3.resizable(0,0)
    text=texts.get()
    text_entry.delete(0,END)
    
    global recv
    global recv_entry
    
    recv=StringVar()
    
    Label(screen3,text="ENTER RECIEVER'S CORRECT NAME",bg="blue").pack()
    Label(screen3,text="").pack()
    recv_entry=Entry(screen3,textvariable=recv)
    recv_entry.pack()
    
    Label(screen3,text="").pack()
    Button(screen3,text="SEND",command=sendmssg,height=1,width=7).pack()

#sending a mail to the reciever
def sendmail():
    s=send_mail.get()
    r=recv_mail.get()
    c=encoder(text)
    p=password.get()
    pass_entry.delete(0,END)
    mail1_entry.delete(0,END)
    mail2_entry.delete(0,END)
    text_entry.delete(0,END)
    
    #operations on mailing servers
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(s,p)
    mail.sendmail(s,r,c)
    mail.close()
    screen2.destroy()

#gui for mailing
def encoder_email():
    global screen2
    global text
    screen2=Toplevel(screen)
    screen2.geometry("300x300")
    screen2.resizable(0,0)
    text=texts.get()
    text_entry.delete(0,END)
    
    global send_mail
    global recv_mail
    global password
    global pass_entry
    global mail1_entry
    global mail2_entry
    
    send_mail=StringVar()
    recv_mail=StringVar()
    password=StringVar()
    
    Label(screen2,text="ENTER YOUR MAIL-ID",bg="blue").pack()
    Label(screen2,text="").pack()
    mail1_entry=Entry(screen2,textvariable=send_mail)
    mail1_entry.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="ENTER RECIEVER'S MAIL-ID",bg="blue").pack()
    Label(screen2,text="").pack()
    mail2_entry=Entry(screen2,textvariable=recv_mail)
    mail2_entry.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="ENTER PASSWORD",bg="blue").pack()
    Label(screen2,text="").pack()
    pass_entry=Entry(screen2,textvariable=password)
    pass_entry.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="SEND",command=sendmail,height=1,width=7).pack()

    
#toplayeer gui for recieving the message 
def main_fun():
    global texts
    global screen
    global text_entry
    
    screen=Tk()
    screen.geometry("300x150")
    screen.title("ENCODER")
    
    texts=StringVar()
    
    Label(screen,text="").pack()
    Label(screen,text="ENTER YOUR TEXT",bg="blue").pack()
    
    Label(screen,text="").pack()
    
    text_entry=Entry(screen,textvariable=texts)
    text_entry.pack()
    
    Label(screen,text="").pack()
    
    Button(screen,text="whatsapp",command=encoder_whatsapp,height=1,width=7).place(x=85,y=90)
    Button(screen,text="email",command=encoder_email,height=1,width=7).place(x=155,y=90)
    screen.mainloop()
#calling the functions
if __name__ == "__main__": 
    main_fun()

