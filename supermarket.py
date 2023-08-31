#date and time  to need module isimport datetime
from datetime import datetime
#we need datails of person 

name=input("enter your name:")
print("welcome to CHAMU SROTES")
#display items to use list variable

lists='''
Rice   Rs 60/kg
sugar  Rs 40/kg
salt   Rs 20/kg
oil    Rs 150/liter
paneer Rs 200/kg
maggi  RS 50/kg
boost  Rs 200/kg
onions Rs 50/kg
tamota Rs 60/kg
''' 
#declaration of prices and quenty and etc
price = 0
pricelist=[]
totalprice=0
finalpeice=0
ilist=[]
qlist=[]
plist=[]

#rates for items  in distnery formate
items={'Rice':60,
'sugar':40,
'salt': 20,
'oil':  150,
'paneer':200,
'maggi': 50,
'boost': 200,
'onions':50,
'tamota':60}
option=int(input("for lists of items press 1:"))

if option==1:
    print(lists)
    for i in range(len(items)):
        press1=int(input("if you want to buy press 1  or 2 for exit:"))  
        if press1==1:
            item=input("enter your items:")
            quantity=int(input("enter your quantity:"))
            if item in items.keys():
                price=quantity*(items[item])
                print(price)
                pricelist.append((item,quantity,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice

            else:          
                print("sorry your entered item is not avalable")
                continue

        if press1==2 :
            break    
        
        inp=input("can i bill the items yes or continue for no or exit:")
        if inp=='yes':
            pass
             

            if finalamount!=0:
                print(25*"=","CHAMU SUPERMARKET",25*"=")
                print(28*" ",'Tirupati')
                print("Name:",name,30*" ","Date:",datetime.now())
                print(75*"-")
                print("sno",10*" ","items",10*" ","quantity",7*" ","price")
                for i in range(len(pricelist)):
                    print(i,13*" ",ilist[i],12*" ",qlist[i],12*" ",plist[i])
                print(75*"-")
                print(50*" ","Totalamount:","Rs",totalprice)
                print("gst amount",50*" ","Rs",gst)
                print(75*"-")
                print(50*" ","finalamount:","Rs",finalamount)
                print(75*"-")
                print(30*" ","Thanks for visiting"," ")   
                print(75*"-") 
                break
        elif inp=='no':
             continue
        elif inp=='exit':
            break
        else:
            print("enter yes or no only")  
    
            continue     
        
    else:
      print("you entered wrong number")  
else:
    print("you entered wrong number") 

