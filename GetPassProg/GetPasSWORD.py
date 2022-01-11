import time , smtplib ,secrets
from info import info_file, ClearScreenTerminal

count = 0
input_value = 0
server = smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()
server.login('vanyachizmodi2@gmail.com','ChelikslawChizmodiy2003400.Ivan')


def CreateRandomPass():
    pasword_lenght = 4
    return secrets.token_urlsafe(pasword_lenght)

def GetStartedPss():
    genereted_pass = CreateRandomPass().upper()
    server.sendmail('vanyachizmodi2@gmail.com' , 'vanyachizmodi@gmail.com', genereted_pass)



def ChangePass():
    pass


# To do code

user_pass = str(input(3 * ' ' + 'Введіть пароль - '))
# start loop
running = True
while running:
    if user_pass == info_file['main_pass']:
        # Do func
        break
    else:
        count += 1
        ClearScreenTerminal()
        print(3 * ' ' + f'Спроба - {count}')
        user_pass = str(input(3 * ' ' + 'Введіть пароль - '))
        if count == 3:
            # stop loop
            running = False
            ClearScreenTerminal()
            input_value = int(input((4 * ' ' + '1 - Відновити пароль\n'
                                           '     2 - Відміна\n')))
            if input_value == 1:
                GetStartedPss()
                time.sleep(15)

            if input_value == 2:
                time.sleep(4)
                break


# main

