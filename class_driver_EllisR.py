from class_module_EllisR import ShoppingEllisR

def objectsListEllisR():
    object_list=[]
    item_number = int(input("Enter the number of items: "))
    while item_number<1:
        print("Number of items must be at least 1")
        item_number = int(input("Re-Enter the number of items: "))
    
    for i in range (item_number):
        item_name=input("Enter the name of the food: ")
        item_amount = float(input("Enter the amount of food (in pound): "))
        while item_amount<=0 :
            print("Item amount must be greater than 0")
            item_amount = float(input("Re-Enter the amount of food (in pound): "))
        
        object_list.append(ShoppingEllisR(item_name, item_amount))
    
    return object_list

def displayContentEllisR(object_list):
    print("\nHere's a summary of the items purchased: ")
    for i in range(len(object_list)):
        print(object_list[i].__str__())

def calculateTotalPriceEllisR(object_list):
    calculate_price_list=[]
    for i in range(len(object_list)):
        temp = object_list[i].getCalculatedPriceEllisR()
        calculate_price_list.append(temp)

    total_price=0
    for prices in calculate_price_list:
        total_price+=prices
    return total_price



main1 = objectsListEllisR()
displayContentEllisR(main1)

print(f"Total cost: ${calculateTotalPriceEllisR(main1):,.2f}")
    
