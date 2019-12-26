import sys
import time
while True:
    print('Is it raining?')
    answer1 = input()
    if answer1.upper() == 'NO':
        break
    if answer1.upper() =='YES':
        break
    if answer1.upper() != 'YES' or answer1.upper() != 'NO':
        print('Please answer with Yes or No !')
        continue
if answer1.upper() =='NO':
    print('Go outside.')
    sys.exit(0)
if answer1.upper() =='YES':
    while True:
         print('Do you have an umbrella?')
         answer2=input()
         if answer2.upper() =='YES':
             break
         if answer2.upper() == 'NO':
             break
         if answer2.upper() != 'YES' or answer2.upper() != 'NO':
             print('Please answer with Yes or No !')
             continue
if answer2.upper() == 'YES':
    print('Go outside.')
    sys.exit(0)
if answer2.upper() == 'NO':
    while True:
        print('Wait a little.')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('Is it still raining?')
        answer3=input()
        if answer3.upper() == 'NO':
            break
        if answer3.upper() == 'YES':
            continue
        if answer3.upper() != 'YES' or answer3.upper() != 'NO':
            print('Please answer with Yes or No !')
            continue
if answer3.upper() == 'NO':
     print('Go outside.')
     sys.exit(0)


