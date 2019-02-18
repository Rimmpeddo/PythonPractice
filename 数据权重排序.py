some_arg = [{"name": "goods1", "price": 100, "sales": 100, "stars": 5, "comment": 100}, \
            {"name": "goods2", "price": 200, "sales": 200, "stars": 10 , "comment": 200}, \
            {"name": "goods3", "price": 300, "sales": 300, "stars": 20, "comment": 300}, \
            {"name": "goods4", "price": 600, "sales": 600, "stars": 40, "comment": 400}, \
            {"name": "goods5", "price": 800, "sales": 800, "stars": 100, "comment": 600}]

def weight(arg):
    price = arg["price"]
    sales = arg["sales"]
    stars = arg["stars"]
    comment = arg["comment"]

    return price*0.4 + sales*0.17 + stars*0.13 + comment*0.3

new_weight = sorted(some_arg, key= weight)

print(new_weight)

new_weight_a = sorted(some_arg, key= lambda x: x["price"]*0.4 + x["sales"]*0.17 + x["stars"]*0.13 + x["comment"]*0.3, reverse=True)

print(list(new_weight_a))