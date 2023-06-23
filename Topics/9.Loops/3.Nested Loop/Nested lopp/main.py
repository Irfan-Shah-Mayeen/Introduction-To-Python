row = int(input("Enter rows:"))
col = int(input("Enter colums:"))
symbol = input("Enter a symbol:")
for i in range(row):
     for j in range(col):
         print(symbol,end="")
     print()