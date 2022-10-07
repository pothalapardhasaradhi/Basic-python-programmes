from datetime import datetime
name=input("Enter your name:")
list={"""
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Panner  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Colgate Rs 85/each
"""}
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'Rice':20,'Sugar':30,'Oil':80,'Panner':110,'Maggi':50,'Boost':90,'Colgate':85}
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your item")
        quantity=int(input("Enter youer Quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Invalid entry")

    else:
        print("You entered Wrong number")
    inp=input('Do yo want bill generation press "yes" else "no" ')
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Pardhu SuperMarket",25*"=")
            print(28*" ","SriKalahasti")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ","items",8*" ","Quantity",3*" ","Price")
            
            for i in range(len(pricelist)):
                print(i,8*" ",ilist[i],8*" ",qlist[i],3*" ",plist[i])
            print(75*"-")
            print(50*" ","Totalamount:","Rs",totalprice)
            print("Gst amount",50*" ","Rs",gst)
            print(75*"-")
            print(50*" ","Final Amount:","Rs",finalamount)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(75*"-")
    
    
            


