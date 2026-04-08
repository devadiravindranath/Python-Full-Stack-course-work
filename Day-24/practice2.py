customer = ("Ravi","hyd") #tuple

items = ["apple","banana","coconut","apple"] #list

unique_items = set(items) #set

shopping = {
    "customer": customer,
    "items" : items,
    "unique_items": unique_items
}

name,city = shopping["customer"]
print("customer:",name)
print("city:",city)

print("all items:",shopping["items"])
print("unique items:",shopping["unique_items"])

print("total Items:",len(shopping["items"]))
print("unique count:",len(shopping["unique_items"]))
