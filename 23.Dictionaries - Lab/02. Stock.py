stocks = input().split(" ")
products = input().split(" ")
stock_dict = {stocks[i]: (stocks[i+1]) for i in range(0, len(stocks) - 1, 2)}

for p in products:
    if p in stock_dict.keys():
        print(f"We have {stock_dict[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")
