class ShoppingEllisR:
    def __init__(self, food_name, food_amount):
        self.__food_name = food_name
        self.__food_amount = food_amount
        self.__standard_price=0
        self.__calculated_price=0
    
    def getFoodNameEllisR(self):
        return self.__food_name
    def setFoodNameEllisR(self, food_name):
        self.__food_name = food_name
    def getFoodAmountEllisR(self):
        return self.__food_amount
    def setFoodAmountEllisR(self, food_amount):
        self.__food_amount = food_amount
    
    def __PriceListEllisR(self):
        if(self.__food_name == 'Dry Cured Iberian Ham'):
            self.__standard_price = 177.80
        elif(self.__food_name == 'Wagyu Steaks'):
            self.__standard_price = 450.00
        elif(self.__food_name == 'Matsutake Mushrooms'):
            self.__standard_price = 272.00
        elif(self.__food_name == 'Kopi Luwak Coffee'):
            self.__standard_price = 306.50
        elif(self.__food_name == 'Moose Cheese'):
            self.__standard_price = 487.20
        elif(self.__food_name == 'White Truffles'):
            self.__standard_price = 3600.00
        elif(self.__food_name == 'Blue Fin Tuna'):
            self.__standard_price = 3603.00
        elif(self.__food_name == 'Le Bonnotte Potatoes'):
            self.__standard_price = 270.81
        else:
            self.__standard_price = 0.00
    
    def PriceCalculationEllisR (self):
        self.__PriceListEllisR()
        self.__calculated_price = self.__food_amount * self.__standard_price
        return f'{self.__calculated_price:,.2f}'
    
    def getStandardPriceEllisR(self):
        self.__PriceListEllisR()
        return self.__standard_price
    def getCalculatedPriceEllisR(self):
        self.__PriceListEllisR()
        return self.__calculated_price
    
    def __str__(self):
        self.__PriceListEllisR()
        return f"Item: {self.__food_name} \nAmount ordered: {self.__food_amount} pounds \nPrice per pound: ${self.__standard_price:,.2f} \nPrice of order: ${self.PriceCalculationEllisR()} \n"
    
    
