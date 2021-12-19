print('welcome to edureka bank')
restart=('y')
chances=3
balance=900
while chances>=0:
    pin=int(input('please enter your 4 digit pin:'))
    if pin==(1234):
        print('you enter your pin correctly/n')
        while restart not in ('n','no','NO','N'):
            print('please press 1 for your balance/n')
            print('please press 2 for your withdrawal/n')
            print('please press 3 for your pay in/n')
            print('please press 4 for your return card/n')
            option=int(input('what would yu like to choose?'))
            if option==1:
                print('your balance is $',balance )
                restart=input('would you like to go back?')
                if restart in ('n','no','NO','N'):
                    print('thank you for banking with edurika')
                    break
            elif option==2:
                option2=('y')
                withdrawl=float(input('how much would you like to withdrawl?/n$10/$20/$40/$60/$80/$100 for other enter 1'))
                if withdrawl in [10,20,40,60,80,100]:
                    balance=balance-withdrawl
                    print('/n your balance is now $',balance)
                    restart=input('what would you like to do?')
                    if restart in('n','no','NO','N'):
                        print('thank you for banking with edurika')
                        break
                elif withdrawl!=[10,20,40,60,80,100]:
                    print('invalid amount,please retry/n')
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=float(input('please enter the desired amount:'))
            elif option==3:
                pay_in=float(input('how much would you like to pay in?'))
                balance=balance+pay_in
                print('/n your balance is now $',balance)
                restart=input('would you like to go back?')
                if restart in ('n','no','NO','N'):
                    print('thank you for banking with edurika')
                    break
            elif option==4:
                print('please  wait while your card is returned..../n')
                print('thank you for banking with edurika')
                break
            else:
                print('please enter correct number./n')
                restart=('y')
    elif pin!=('1234'):
        print('incorrect password')
        chances=chances-1
        if chances==0:
            print('/n no more tries,contact support@edurika.com')
            break
            
            
         

