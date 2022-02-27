from tkinter import SOLID
print("\n-------Ebay Fees Calculator---------")
purchase_price = float(input("Purhcased Price : "))
sold_price = float(input("Sold Price : "))
ebay_fees = float(12)
total_fees = sold_price / 100 * ebay_fees
total_return = round(sold_price - total_fees, 2)
total_profit = round(sold_price - total_fees - purchase_price,2)
print("Total Profit :" + " " + "£" + str(total_profit))
print("Total Return :" + " " + "£" + str(total_return))
print("-----------------------------------")