print("Hello Guys! Welcome to the bucket list of household products: ")
print("-------------------------------------------------------------- ")
bucket = {1120: {'Product_Name':'Apple',"Expiry_date": 2021,"Price":100,"Quantity":200,"Taste":'sweet'},
          1121: {'Product_Name':'Banana',"Expiry_date": 2021,"Price":30,"Quantity":150,"Taste":'sweet'},
          1122: {'Product_Name':'Vinegar',"Expiry_date": 2022,"Price":55,"Quantity":80,"Taste":'sour'},
          1123: {'Product_Name':'Strawberry',"Expiry_date": 2021,"Price":99,"Quantity":120,"Taste":'sweet'},
          1124: {'Product_Name':'Grapes',"Expiry_date": 2021,"Price":55,"Quantity":110,"Taste":'sweet'},
          1125: {'Product_Name':'Candy',"Expiry_date": 2023,"Price":5,"Quantity":250,"Taste":'sweet'},
          1126: {'Product_Name':'Pickle',"Expiry_date": 2023,"Price":110,"Quantity":120,"Taste":'sour'},
          1127: {'Product_Name':'Choco_Cake',"Expiry_date": 2021,"Price":350,"Quantity":10,"Taste":'sweet'},
          1128: {'Product_Namen':'Milk_Cake',"Expiry_date": 2021,"Price":800,"Quantity":25,"Taste":'sweet'},
          1129: {'Product_Name':'Soft_Drinks',"Expiry_date": 2021,"Price":35,"Quantity":250,"Taste":'bitter&sweet'},
          1130: {'Product_Name':'Bittergourd(in kg)',"Expiry_date": 2021,"Price":60,"Quantity":250,"Taste":'bitter'},
          1131: {'Product_Name':'pea(in kg)',"Expiry_date": 2021,"Price":69,"Quantity":140,"Taste":'sweet'},
          1132: {'Product_Name':'Brinjal(in kg)',"Expiry_date": 2021,"Price":40,"Quantity":120,"Taste":'mild_bitter'},
          1133: {'Product_Name':'Tomato(in kg)',"Expiry_date": 2021,"Price":27,"Quantity":90,"Taste":'sour'},
          1134: {'Product_Name':'Potato(in kg)',"Expiry_date": 2021,"Price":37,"Quantity":90,"Taste":'mild_sweet'},
          1135: {'Product_Name':'Mouthfreshener',"Expiry_date": 2022,"Price":20,"Quantity":250,"Taste":'sweet'},
          1136: {'Product_Name':'Papaya(in kg)',"Expiry_date": 2021,"Price":60,"Quantity":90,"Taste":'sweet'},
          1137: {'Product_Name':'Mango(in kg)',"Expiry_date": 2021,"Price":80,"Quantity":150,"Taste":'sweet'},
          1138: {'Product_Name':'Pizza',"Expiry_date": 2021,"Price":199,"Quantity":210,"Taste":'spicy'},
          1139: {'Product_Name':'Burger',"Expiry_date": 2021,"Price":60,"Quantity":120,"Taste":'spicy'},
          1140: {'Product_Name':'Momos',"Expiry_date": 2021,"Price":50,"Quantity":120,"Taste":'spicy'},
          1141: {'Product_Name':'VegRoll',"Expiry_date": 2021,"Price":30,"Quantity":190,"Taste":'spicy'},
          1142: {'Product_Name':'French_Fries',"Expiry_date": 2021,"Price":150,"Quantity":190,"Taste":'sweet'},
          1143: {'Product_Name':'HotDog',"Expiry_date": 2021,"Price":168,"Quantity":50,"Taste":'sweet'},
          1144: {'Product_Name':'Maggi',"Expiry_date": 2021,"Price":45,"Quantity":150,"Taste":'spicy'},
          1145: {'Product_Name':'Butter',"Expiry_date": 2021,"Price":70,"Quantity":150,"Taste":'salty'},
          1146: {'Product_Name':'Almonds(in kg)',"Expiry_date": 2023,"Price":400,"Quantity":190,"Taste":'sweet'},
          1147: {'Product_Name':'Dairy_Milk',"Expiry_date": 2021,"Price":120,"Quantity":100,"Taste":'sweet'},
          1148: {'Product_Name':'Lassi',"Expiry_date": 2021,"Price":30,"Quantity":90,"Taste":'salty&sour'},
          1149: {'Product_Name':'Kurkure',"Expiry_date": 2021,"Price":10,"Quantity":120,"Taste":'spicy'}}
print("These are the product which we have in bucket list " )
print("-------------------------------------------------- ")
print(bucket)
print("-------------------------------------------------- ")
prod_id = int(input("Enter the id that product you want to check from the bucket list: "))
def prod(prod_id):
    if(prod_id in bucket):

       print(bucket[prod_id])
    else:
       print("You entered wrong id Enter Again from bucket list: ")
       prod_id = int(input(""))
       prod(prod_id)
prod(prod_id)
print("Want to Check another Product (y/Y for Yes or N/n for No): ")
choice = str(input(""))
def choices(choice):

    if(choice=='Y' or choice=='y'):



       prod_id = int(input("Enter the id that product you want to check from the bucket list: "))
       prod(prod_id)
       print("Want to Check another Product (y/Y for Yes or N/n for No): ")
       choice=str(input(""))
       choices(choice)
    elif(choice=='N' or choice=='n'):
        print("Thankyou Sir/Madam, Have a great Day!")
    else:

        print("Sorry! Entered Again ")
        choice=str(input(""))
        choices(choice)
choices(choice)
print("----------------------------------------")
import json
js = json.dumps(bucket)
fd = open("bucket.json",'w')
fd.write(js)
fd.close()
fd = open("bucket.json",'r')
txt= fd.read()
bucket=json.loads(txt)
print("Add some new products in bucket list: ")
print("----------------------------------------------")


product_id = input("Enter product id: ")
Product_Name = input("Enter name: ")
Expiry_date = int(input("Enter expiry date: "))
Price = int(input("Enter Price: "))
Quantity = int(input("Enter Quantity: "))
Taste = input("Enter the taste: ")
def update(product_id,Product_Name,Expiry_date,Price,Quantity,Taste):
    bucket[product_id] = {'Product_Name':Product_Name,'Expiry_date':Expiry_date,'Price':Price,'Quantity':Quantity,'Taste':Taste}
update(product_id,Product_Name,Expiry_date,Price,Quantity,Taste)
print("Want to add another Product (Y/y for Yes or N/n for No)")
rec = str(input(""))
def record(rec):

    if(rec=='Y' or rec=='y'):



        product_id = input("Enter product id: ")
        Product_Name = input("Enter name: ")
        Expiry_date = int(input("Enter expiry date: "))
        Price = int(input("Enter Price: "))
        Quantity = int(input("Enter quantity: "))
        Taste =  input("Enter the taste: ")
        update(product_id,Product_Name,Expiry_date,Price,Quantity,Taste)
        print("Want to add another Product (Y/y for Yes or N/n for No)")
        rec=str(input(""))
        record(rec)
    elif(rec=='N' or rec=='n'):
            print("Thankyou Sir/Madam for giving your valuable time!")
    else:
            print("Sorry! Enter Again")
            rec = input("")
            record(rec)
record(rec)


    
print("Our Updated Inventory is: ")
print("------------------------------")
print(bucket)
js = json.dumps(bucket)
fd = open('bucket.json','w')
fd.write(js)
fd.close()
print("Want to delete something from bucket list: ")
print("Press Y for yes or Press another key for exit: ")
dele = input("")
if (dele == 'Y'):

    print("Enter Product id: ")
    id = int(input(""))
    if id in bucket:
       
        del bucket[id]
        print(bucket)
  
else:
    print("Thankyou!")

print("Purchase something: ")
prod = input("Enter the product id: ")
quant = int(input("Enter the quantity: "))

print("Product: ", bucket[prod]['Product_Name'])
print("Price: ", bucket[prod]['Price'])
print("Your billing amount is: ")
print("Billing Amount: ",bucket[prod]['Price']*quant)
bucket[prod]['Quantity'] = bucket[prod]['Quantity'] - quant
print("Your Updated inventory is: ")
js = json.dumps(bucket)

fd = open("bucket.json",'w')
fd.write(js)
fd.close()
print("Sales: ")
sales = {1:{'prod_id':prod,'Quantity':quant,'amount':bucket[prod]['Price']*quant},
         2:{'prod_id':prod,'Quantity':quant,'amount':bucket[prod]['Price']*quant},
         3:{'prod_id':prod,'Quantity':quant,'amount':bucket[prod]['Price']*quant}}
sale = json.dumps(sales)
print(sale)

