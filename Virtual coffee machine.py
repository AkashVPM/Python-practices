def payment(customer_requirement):
      Price_of_item = price_tag[customer_requirement.lower()]

      if Price_of_item == total_amount:
            print(f"\nplease take your {customer_requirement} ")
      if Price_of_item > total_amount:
            print(f"\ninsufficent amount and you need to pay Rs.{Price_of_item - total_amount}")
            print(f"\nPlease take your money back")
            exit()
      if Price_of_item < total_amount:
            print(f"\nHere is your item")
            print(f"Please take your change of Rs.{total_amount - Price_of_item} back")

      print(f"\nEnjoy your {customer_requirement}")

price_tag = {
     "coffee" : 100,
      "tea" : 75,
      "latte" : 150,
      "mocha" : 200 
      }

avaliable_items = ["Coffee","Tea","Latte","Mocha"]


customer_requirement = str(input(f"What would you like to have {avaliable_items} : "))


if customer_requirement in avaliable_items:
      Five_rupee = int(input("\nhow many 5 Rubee coins : "))
      Ten_rupee = int(input("how many 10 Rubee coins : "))
      Twenty_rupee = int(input("how many 20 Rubee coins : "))
      total_amount = Five_rupee * 5 + Ten_rupee * 10 + Twenty_rupee*20
      payment(customer_requirement)

if "price" in customer_requirement:
      print(price_tag)





