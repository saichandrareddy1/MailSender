#https://myaccount.google.com/lesssecureapps?pli=1

import smtplib
import time

__author__ = "SaiReddy"

class MailSender(object):
    def __init__(self, Your_name, Sender_mail, Password, Reciver_mail, Need_time, acc, val_acc, epoch, num):
        self.Your_name = Your_name
        self.Sender_mail = Sender_mail
        self.Password = Password
        self.Reciver_mail = Reciver_mail
        self.Need_time = Need_time
        self.acc = acc
        self.val_acc = val_acc
        self.epoch = epoch
        self.num = num
    def mailsend(self):
        try:
            t = time.localtime()
            present_time = time.strftime("%M", t)
            full_time = time.strftime("%H:%M:%S", t)
            if (self.epoch)%(self.num) == 0:
                print("INFO[] ENTERED.....")
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.login(self.Sender_mail, self.Password)
                str_acc = str(self.acc)
                str_val = str(self.val_acc)
                str_epoch = str(self.epoch)
                print(type(str_epoch))
                message = "Hello " + str(self.Your_name) +  " mail from " + str(self.Sender_mail) +"\n" +"Time is "+ str(full_time) + " and your accuracy was at " +str(str_acc) +" Val accuracy is " + str(str_val) +" epoch is " + str(str_epoch)
                s.sendmail(self.Sender_mail ,self.Reciver_mail, message)
                s.quit()
                print("INFO[] Mail was sended {}:".format(self.Your_name))
            else:
                print("INFO[] It's not the correct time to send {}:".format(self.Your_name))
        except:
            print("INFO[] some exception was came {}".format(self.Your_name))

if __name__ == '__main__':
    mail = MailSender(Your_name, Sender_mail, Password, Reciver_mail, Need_time, acc, val_acc, epoch, num)
    mail.mailsend()
    
