import random

s1=0
s2=0
s3=0
s4=0
tl=0
t="0000"
st=['0','0','0','0']
plus=0
minus=0
counter=0
istrue=False
while s1==0 or s1==s2 or s1==s3 or s1==s4 or s2==s3 or s2==s4 or s3==s4:
    s1=random.randint(0,9)
    s2=random.randint(0,9)
    s3=random.randint(0,9)
    s4=random.randint(0,9)
st[0]=chr(s1+48)
st[1]=chr(s2+48)
st[2]=chr(s3+48)
st[3]=chr(s4+48)
print('I kept a 4 digit number in my mind, can you find it?')
print('New game started !')
while istrue==False:
    plus=0
    minus=0
    t="0000"
    while tl!=4 or t[0]=="0" or t[0]==t[1] or t[0]==t[2] or t[0]==t[3] or t[1]==t[2] or t[1]==t[3] or t[2]==t[3] :
        msg='Enter your guess (' + str(counter+1)+'):'
        t=input(msg)
        tl=len(t)
        if tl!=4 or t[0]=="0" or t[0]==t[1] or t[0]==t[2] or t[0]==t[3] or t[1]==t[2] or t[1]==t[3] or t[2]==t[3]:
            print('Wrong enter, try again please!')
    counter+=1
    for s in range(0,4):
        if st[s]==t[s]:
            plus+=1
    if st[0]==t[1] or st[0]==t[2] or st[0]==t[3]:
        minus+=1
    if st[1]==t[0] or st[1]==t[2] or st[1]==t[3]:
        minus+=1
    if st[2]==t[1] or st[2]==t[0] or st[2]==t[3]:
        minus+=1
    if st[3]==t[1] or st[3]==t[2] or st[3]==t[0]:
        minus+=1
    print(t,'   +',plus,' -',minus)
    if plus==4:
        print('')
        print('Congratulations, you have found the number.')
        print('')
        break
    if counter==10:
        print('')
        print('Sorry, you could not find the number.',s1,s2,s3,s4)
        break
