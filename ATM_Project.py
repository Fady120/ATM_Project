import getpass
import stdiomask


ATM_dict =  {
            215221701332: {'Name' :'Ahmed Ali', 'Password':1783, 'Balance':3500166, 'Access': 1},
            203659302214: {'Name' :'Muhammad Hossam', 'Password':1390, 'Balance':520001, 'Access': 1},
            126355700193: {'Name' :'Hassan Ahmed', 'Password':1214, 'Balance':111000, 'Access': 1},
            201455998011: {'Name' :'Waleed Muhammad', 'Password':2001, 'Balance':1200, 'Access': 1},
            201122369851: {'Name' :'Ahmed Shaban', 'Password':8935, 'Balance':178933, 'Access': 1},
            201356788002: {'Name' :'Muhammad Badr', 'Password':3420, 'Balance':55000, 'Access': 1},
            203366789564: {'Name' :'Muhammad Medhat', 'Password':1179, 'Balance':18000, 'Access': 1},
            201236787812: {'Name' :'Bassem Amr', 'Password':1430, 'Balance':180350, 'Access': 1}
            }

while (True):
 ID=int(input("Please enter your account ID: "))
 f1=0
 f2=0
 i=0
 if(ID == 215221701332) or (ID == 203659302214) or (ID == 126355700193) or (ID == 201455998011) or (ID == 201122369851) or (ID == 201356788002) or (ID == 203366789564) or (ID == 201236787812):
     if(ATM_dict[ID]['Access']==1):
      f1=1
      while(i<3):
          password=int(stdiomask.getpass(prompt='Please enter you password : ',mask='*'))
          #password= int(input("Please enter you password: "))
          if(password==ATM_dict[ID]['Password']):
                print("\n...........................................\n\t\t Welcome\n")
                f2=1
                break
          else:
            print("Wrong passsword, Try agian\n")
            i+=1
           
      if(i==3):
         print("\nSorry you are blocked, please go to the bank to solve the problem")
         ATM_dict[ID]['Access']=0

     else:
         print("It seems there is an issue, please go to the bank to solve it.")

 else:
    print("Wrong ID, try agian\n...........................................")

 if(f1==1 and f2==1):
     f=0
     while(f==0):
      print("If you want cash withdraw, please press 1")
      print("If you want cash balance inquiry, please press 2")
      print("If you want cash Password change , please press 3")
      print("If you want cash Fawry service , please press 4")
      print("If you want cash Exit, please press 5")
      choice=int(input("\nPlease enter your choice: "))
      if(choice == 1):
          w=0
          while(w==0):
           amount=int(input("\nEnter the amount you want to withdraw: "))
           if(amount<=ATM_dict[ID]['Balance']):
                 if(amount%100==0):
                         if(amount>5000):
                             print("Just 5000 was been withdraw, please enter agian to withdraw the rest.\n")
                             ATM_dict[ID]['Balance']-= amount
                         else:
                             print("Your request has been executed.\n...........................................\n")
                             ATM_dict[ID]['Balance']-= amount
                             w=1
                            
                 else:
                     print("Sorry, the value must be multiple of 100, try agian.\n")

           else:
               print("Sorry no sufficient balance.\n...........................................\n")
               w=1

      elif(choice == 2):
           print("\nName= " + ATM_dict[ID]['Name'] + "\nBalance= " + str(ATM_dict[ID]['Balance']) + "\n...........................................\n")

           
      elif(choice == 3):
          p=0
          while(p==0):
             password1=int(input("\nPlease enter the new passowrd: "))
             if( len(str(password1)) == 4 ):
                 password2=int(input("Please enter the new passowrd agian: "))
                 if(password1 == password2):
                     ATM_dict[ID]['Password'] = password1
                     p=1
                     print("Password was changed succfully\n...........................................\n")
                 else:
                     print("Passwords doesn't equl each others, try agian")
             else:
                  print("Password must be length of four and no zero in the beginning, try agian.")

      elif(choice == 4):
        n=0  
        while(n==0):
            print("\nIf you want Orange recharge, please press 1")
            print("If you want Etisalat recharge, please press 2")
            print("If you want Vodafone recharge, please press 3")
            print("If you want We recharge, please press 4")
            choice1=int(input("\nPlease enter your choice: "))
            if(choice1==1):
              PhoneNumber=int(input("\nPlease enter Orange phone number: "))
              if( len(str(PhoneNumber)) == 10 ): #10 becuase len() doesn't count 0 in the beginning
               amount=int(input("Please enter the amount of recharge: "))
               if(amount<=ATM_dict[ID]['Balance']):
                   print("Done succfully\n............................................\n")
                   n=1
                   ATM_dict[ID]['Balance']-= amount
               else:
                   print("There isn't enough money")
                   n=1
                   
              else:
                print("Phone number must be length of eleven and there must be zero in the beginnig, try agian.\n")  
                  
                              
            elif(choice1==2):      
              PhoneNumber=int(input("\nPlease enter Etisalat phone number: "))
              if( len(str(PhoneNumber)) == 10 ):
               amount=int(input("Please enter the amount of recharge: "))
               if(amount<=ATM_dict[ID]['Balance']):
                   print("Done succfully\n............................................\n")
                   n=1
                   ATM_dict[ID]['Balance']-= amount
               else:
                   print("There isn't enough money")
                   n=1

              else:
                print("Phone number must be length of eleven and there must be zero in the beginnig, try agian.\n")  
                    
            elif(choice1==3):
              PhoneNumber=int(input("\nPlease enter Vodafone phone number: "))
              if( len(str(PhoneNumber)) == 10 ):
               amount=int(input("Please enter the amount of recharge: "))
               if(amount<=ATM_dict[ID]['Balance']):
                   print("Done succfully\n............................................\n")
                   n=1
                   ATM_dict[ID]['Balance']-= amount
               else:
                   print("There isn't enough money")
                   n=1

              else:
                print("Phone number must be length of eleven and there must be zero in the beginnig, try agian.\n")
               
            elif(choice1==4):
              PhoneNumber=int(input("\nPlease enter We phone number: "))
              if( len(str(PhoneNumber)) == 10 ):
               amount=int(input("Please enter the amount of recharge: "))
               if(amount<=ATM_dict[ID]['Balance']):
                   print("Done succfully\n............................................\n")
                   n=1
                   ATM_dict[ID]['Balance']-= amount
               else:
                   print("There isn't enough money")
                   n=1

              else:
                print("Phone number must be length of eleven and there must be zero in the beginnig, try agian.\n")

                
            else:
                print("Wrong input, try agian.")
     
      elif(choice == 5):
            print("BYE.\n............................................\n")
            f=1

      else:
            print("Wrong input.\nTry agian.\n...........................................\n")
