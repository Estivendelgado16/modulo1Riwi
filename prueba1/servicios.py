import datetime 

listProducts = [{"title": "Cien Años de Soledad", "author": "Gabriel García Márquez", "category": "Ficción", 
                 "price":  23000, "amountStock": 12
                },
                {"title": "El Alquimista", "author": "Paulo Coelho", "category": "Fábula", "price": 18000, "amountStock": 7
                },
                {"title": "1984", "author": "George Orwell", "category": "Distopía", "price": 25000, "amountStock": 10
                },
                {"title": "El Principito", "author": "Antoine de Saint-Exupéry", "category": "Infantil / Filosófico",
                "price": 15000, "amountStock": 20
                },
                {"title": "La Sombra del Viento", "author": "Carlos Ruiz Zafón", "category": "Misterio", "price": 27000,
                "amountStock": 5}]

listClient = []

def addProduct():
    while True:
        try: 
            title = input("Enter the title: ").title()
            if not title or title == " " or title == "":
                print("The name cannot be empty.")
                continue

            author = input("Enter the author's name:").title()
            if not author or author == " " or author == "":
                print("The author cannot be empty.")
                continue
            
            category = input("Enter the category: ").title()
            if category == " " or category == "":
                print("The category cannot be empty.")
                continue

            price = float(input("Enter the product price: "))
            if price < 0:
                print("The price cannot be empty.")
                continue

            amountStock = int(input("Enter the product quantity: "))
            if amountStock < 0:
                print("The amount cannot be negative.")
                continue

            product = {
                "title": title,
                "author": author,
                "category": category,
                "price": price,
                "amountStock": amountStock
            }

            listProducts.append(product)
            print("Product successfully registered.")
            break
        except ValueError:
            print("Invalid entry. Please enter the information correctly.")


def searchProducts():
    if not listProducts:
        print("No products are registered.")
        return

    for product in listProducts:
        print(f"Title: {product['title']} | Author: {product['author']} | Category: {product['category']} | Price: {product['price']} | amount stock: {product['amountStock']}")
        

def upDateProduct():

    if not listProducts:
        print("No products are registered.")
    else:
        searchTitle = input("Enter the title of the product to be updated: ").title()
        for product in listProducts:

            if product['title'] == searchTitle:
                newTitle = input("Enter the new title: ").title()
                newAuthor = input("Enter the new author: ").title()
                newCategory = input("Enter category ").title()
                newPrice = float(input("Enter price: "))
                newAmountStock = int(input("enter amount: "))

                product['title'] = newTitle
                product['author'] = newAuthor
                product['category'] = newCategory
                product['price'] = newPrice
                product['amountStock'] = newAmountStock

                print("Product updated successfully.")
                return
            print(listProducts)
                

def deleteProduct():
    if not listProducts:
        print("No products are registered.")
    else:
        searchTitle = input("Enter the title of the product to be deleted: ").title()
        for index, product in enumerate(listProducts):
            if product['title'] == searchTitle:
                del listProducts[index]
                print("Product successfully removed.")
                return
        print("Product not found.")


def registerClient():
    name = input("Enter customer name: ")
    category = input("Enter the category (vip, general)")

    client = {
        'name' : name,
        'category' : category
    }

    listClient.append(client)


def calculateDiscount(categoria):
    if categoria == "vip":
        return 10.0
    if categoria == "wholesale":
        return 15.0
    return 0.0

sales = []
def sellProduct():
    if not listProducts:
        print("No products are registered.")
    else:
        registerClient()
        searchTitle = input("Enter the title of the product to be sold: ").title()
        for product in listProducts:
            if product['title'] == searchTitle:
                quantity = int(input("Enter the quantity to sell: "))
                if quantity > product['amountStock']:
                    print("There is not enough stock to complete the sale.")
                    return
                
                
                totalPrice = product['price'] * quantity
                discount = calculateDiscount(listClient[-1]['category'])
                discountedPrice = totalPrice - (totalPrice * (discount / 100))
                print(f"Client: {listClient[-1]['name']}")
                print(f"Total price: {totalPrice}")
                print(f"Discount: {discount}%")
                print(f"Price after discount: {discountedPrice}")
                product['amountStock'] -= quantity
                print(f"There are {product['amountStock']} units left in stock.")
                return
        print("Product not found.")






            

