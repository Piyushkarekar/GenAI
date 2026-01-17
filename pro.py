#task-1
products=["laptop", "smartphone", "tablet", "smartwatch"," headphones"]
sample_products = ("laptop",4004,"electronics")
print("2nd product:",products[1])
print("last product:",products[-1])

products.append("keyboard")
products.append("mouse")
print("product list after adding items:",products)

sample_list = list(sample_products)
sample_list[1] = 52000
sample_list[0]="mouse" 
sample_list[2]="cse"  # change price
sample_product = tuple(sample_list)

print("Updated sample_product:", sample_product)

#task-2
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Speaker", "Headphone", "Webcam", "Microphone"]

categories = {
    "Electronics","Accessories","Accessories", "Electronics",
    "Audio", "Audio", "Accessories", "Audio"
}
categories_set = set(categories)
print("Categories:", categories_set)

categories_set.add("Gaming")
categories_set.add("Audio")

print("Categories after adding items:", categories_set)

print("is 'Audio'a category?", "Audio" in categories_set)
print("is 'furniture' a category ?", "furniture"in categories_set)

print("Total number of categories:", len(categories_set))

#task-3
price_dict ={
    "laptop":55000,
    "smartphone":30000,
    "tablet":20000,
    "smartwatch":15000,
    "headphones":5000,
    "webcam" :7000
}

price_dict["Speaker"]=3000
price_dict["laptop"]=50000

print("Updated price dictionary:", price_dict)


product_to_remove ="laptop","smartwatch"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(f"{product_to_remove} not found in the price dict.")
    
avg_price = sum(price_dict.values())/len(price_dict)
print("Average price of products:", avg_price)

max_product = max(price_dict, key=price_dict.get)
min_product =min(price_dict, key=price_dict.get)

print("The most valuable Products:",max_product,price_dict[max_product])
print("The least Valuable Products :",min_product,price_dict[min_product])

#task-4

products={
    ("laptop","electronics"),
    ("mouse","electronics"),
    ("keyboard","electronics"),
    ("tablet","electronics"),
    ("speaker","audio"),
    ("headphone","audio"),
    ("webcam","electronics"),
    ("microphone","audio")
}

catalog=[]
for product_name ,category in products:
    if product_name in price_dict:
        catalog.append((product_name,price_dict[product_name],category))
        print("catalog",catalog)
        print("total item in catalog:",len(catalog))


category_to_products={}
for name ,price,category in catalog:
    if category not in category_to_products:
        category_to_products[category]=[]
        category_to_products[category].append(name)
print("Category to products mapping:",category_to_products)

max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
print("Category with maximum products:", max_category)
print("Products:", category_to_products[max_category])
    


