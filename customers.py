# --- Reflection ---
# 1.  I would use .get() when looking up information that might be missing
# from a dictionary because it allows me to provide a default value instead
# of causing an error. I would use bracket notation when I know the key
# exists and need to access its exact value. My rule of thumb is to use
# .get() when a value might be missing and brackets when I know it exists.

# 2.  Exercise 8 reminds me of using SUMIF in Excel because both involve
# adding values together based on categories. Python can be more useful
# for large datasets because it can automatically process many records
# using loops and organize the results without manually setting up formulas.


#customers.py
#Author: olivia tapscott
# mod 11 lab: customer dictionary and lookup

print("--- Exercise 1---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"]) #accessing  value using bracket notation
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)



# --- Exercise 2: Update and add ---
print("`--- Exercise 2 ---" )
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

#print(customer["email"]) #this will throw a KeyError since the email key was deleted
print(customer.get("email", "Email not found")) #this will return "email not found" since the email key was deleted


print("--- Exercise 3 ---")

# new version
print(customer.get("email", "no email on file")) 

#older version (still used in some codebases)
# try:
#    print(customer["email"])
# except KeyError as error:
#    print(f"KeyError Caught: {error}")

#ctrl ? to comment out all at once

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)


print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")  #platinum
print(f"Discount: {discount_rate * 100:.0f}%")  # 15%
print(f"Final Price: ${final_price:.2f}")       # $170.00


print("--- Exercise 6 ---")
customers = [
    #think of each row in a table/spreadsheet or a record in a database
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0) # if the tier doesnt exist it equals 0, otherwise it gets the value of the tier
    discount = 300 * rate #assuming a purchase of $300 for each customer
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")


print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150}, #key of product(widget_a)
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - only {details['stock']} left in stock!")


print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 250},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
sales_by_region = {} # empty dictionary to hold the sales by region
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"] #if the region is not in the dictionary, it will return 0, otherwise it will return the value of the region and add the amount to it
print(sales_by_region)

for region in sorted(sales_by_region): #prints pretty output with sales totals by reigon
    print(f"{region}: ${sales_by_region[region]:.2f}")

