Coffee = 10
Tea = 10
Latte = 10
Mocha = 10
profit = 0
price = 0

def payment(customer_requirement):
      global price,profit
      Price_of_item = price_tag[customer_requirement.lower()]
      if Price_of_item == total_amount:
            price += Price_of_item
            print(f"\nplease take your {customer_requirement} ")
      if Price_of_item > total_amount:
            # price += (Price_of_item - total_amount)
            print(f"\ninsufficent amount and you need to pay Rs.{Price_of_item - total_amount}")
            print(f"\nPlease take your money back")
      if Price_of_item < total_amount:
            price += Price_of_item 
            print(f"\nHere is your item")
            print(f"Please take your change of Rs.{total_amount - Price_of_item} back")

      print(f"\nEnjoy your {customer_requirement}")
      



def report (customer_requirement):
      global Coffee,Tea,Latte,Mocha
      if "coffee" in customer_requirement:
             Coffee -= 1
      if "tea" in customer_requirement:
             Tea -= 1
      if "latte" in customer_requirement:
             Latte -= 1
      if "mocha" in customer_requirement:
             Mocha -= 1

      
price_tag = {
     "coffee" : 100,
      "tea" : 75,
      "latte" : 150,
      "mocha" : 200 
      }

avaliable_items = ["coffee","tea","latte","mocha"]

while True:
      customer_requirement = str(input(f"What would you like to have {avaliable_items} : ")).lower()

      if customer_requirement in avaliable_items:
            Five_rupee = int(input("\nhow many 5 Rubee coins : "))
            Ten_rupee = int(input("how many 10 Rubee coins : "))
            Twenty_rupee = int(input("how many 20 Rubee coins : "))
            total_amount = Five_rupee * 5 + Ten_rupee * 10 + Twenty_rupee*20
            payment(customer_requirement)
            report(customer_requirement)
            profit += price 

      if "price" in customer_requirement:
            print(price_tag)

      if "report" in customer_requirement:
            print(f"""
                  Reamaning coffee is : {Coffee}
                  Reamaning Tea is : {Tea}
                  Reamaning Latte is : {Latte}
                  Reamaning Mocha is : {Mocha}""")
            
      if "profit" in customer_requirement:
            print(profit)

      if "off" in customer_requirement:
            exit()







