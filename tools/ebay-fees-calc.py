from tkinter import SOLID
print("-------Ebay Fees Calculator---------")
purchase_price = float(input("Purhcased Price £ : \n"))
sold_price = float(input("Sold Price £ : \n"))
ebay_fees = float(12)
total_fees = sold_price / 100 * ebay_fees
result = sold_price - total_fees - purchase_price
print("Total Profit :" + " " + str(result))