"""
Calculate if you should buy the hat in dollars or pesos.

1 peso = 0.02 dollars
"""

while True:
    try:
        price_pesos = int(input("Price in pesos: "))
        price_dollars = int(input("Price in dollars: "))

        pesos_to_dollars = price_pesos * 0.02

        if pesos_to_dollars > price_dollars:
            print("Dollars")
        else:
            print("Pesos")
        break
    except ValueError:
        print("Error: Please enter a number.")
