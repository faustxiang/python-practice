buy_amount = 2000*40.00
buy_commission = buy_amount * 0.03
sell_amount = 2000*42.75
sell_commission = sell_amount * 0.03
profit = sell_amount - buy_amount - buy_commission - sell_commission
print("The amount paid for the stock: $", format(buy_amount, ".2f"))
print("The amount of the commission paid on the purchase: $", format(buy_commission, ".2f"))
print("The amount the stock sold for: $", format(sell_amount, ".2f"))
print("The amount of the commission paid on the sale: $", format(sell_commission, ".2f"))
print("The amount of profit (or loss if negative): $", format(profit, ".2f"))