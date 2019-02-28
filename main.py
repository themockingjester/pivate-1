#aim: software of personal diary
#status:incomplete (left parts are :--if two accounts has same passcode then if you delete delete any one of them then Aautomatically passcode of secong gets deleted
# another problem:to run iot you have to make two files named login.txt and pass.txt and i forget to add a option for viewing entries

def first():
    ctr=0
    while 1:
        
    uname=input("enter username")
    if uname.endswith("@jester.com"):
        break
    else:
        
        pass
        
    uname2=uname+"\n"
    with open('login.txt','r') as f:
        for line in f:
            if(uname2==line):
                print("alredy")
                break
        else:
            print("success")
            ctr+=1
    if(ctr==1):
        with open('login.txt', 'a') as f:
            with open('pass.txt', 'a') as f2:
                password=input("enter your password")
                password+="\n"
                f2.write(password)
                f2.close()
            f.write(uname2)
        f.close()
def second():
    name=input("enter user name")
    nameu=name                              #variable for diary name(nameu)
    name+="\n"
    password=input("enter you password")
    password+="\n"
    with open('login.txt', 'r') as f:                                 #this file is only for verification of user
        with open('pass.txt', 'r') as f2:                              #same here
            for line in f2:
                if(line==password):
                    break
            else:
                print("try again:")
                return
        for line in f:
            if (line == name):
                print("wlcm"+"\t"+line)
                print("wanna to enter a new entry(press 1")
                print("wanna to delete a entry(press 2)")
                input1=int(input("enter your choice"))
                if(input1==1):
                    print("enter date in this format(dd/mm/yyyy)only otherwise you cant delete your entry in future if forgotten")
                    file=nameu + '.txt'

                    with open(file, 'a') as f:
                        date=input("enter date")
                        date+="."
                        input2=input("enter contents(dont hit enter enter till complete)")
                        input2+="\n"
                        f.write(date+input2)
                elif(input1==2):
                    print("enter date in this format(dd/mm/yyyy)only otherwise you cant delete your entry")
                    file=nameu + '.txt'

                    with open(file, 'r') as f:
                        date=input("enter date")
                        date+="."
                        with open('x.txt','a') as f2:
                            for line in f:
                                if date in line:
                                    pass
                                else:
                                    f2.write(line)
                    import os
                    os.remove(file)
                    os.rename('x.txt',file)


                break
        else:
            print("go away")
            return
def third():

    name = input("enter user name")
    nameu = name
    name += "\n"
    password = input("enter you password")
    password += "\n"
    with open('login.txt', 'r') as f:  # this file is only for verification of user
        with open('pass.txt', 'r') as f2:  # same here
            for line in f2:
                if (line == password):
                    break
            else:
                print("try again:")
                return
        for line in f:
            if (line == name):
                nameu+='.txt'
                print("wlcm" + "\t" + line)
                import os
                os.remove(nameu)
                with open('pass.txt', 'r') as f2:
                        with open('y.txt', 'a') as f3:
                            for line2 in f2:
                                if line2 != password :
                                    f3.write(line2)
                                else:
                                    pass
                with open('login.txt', 'r') as f:
                        with open('x.txt', 'a') as f3:
                            for line3 in f:
                                if line3 != name:
                                    f3.write(line3)
                                else:
                                    pass

    os.remove('login.txt')
    os.remove('pass.txt')
    os.rename('x.txt','login.txt')
    os.rename('y.txt','pass.txt')
print("\t\tHlo welcome to personal diary")
print("press 1 for sign up")
print("press 2 for sign in ")
print("press 3 for deleting your account")

choice = int(input("enter your choice"))
if choice==1:
    first()
elif choice==2:
    second()
elif choice==3:
    third()
else:
    print("wrong input try next next time")
