import pandas as pd
data=pd.read_csv("sales_data.csv")
print("Sales Data:")
print(data)
data["Total Sales"]=data["Quantity"]*data["Price"]
print("\nTotal Sales:")
print(data[["Product","Quantity","Price","Total Sales"]])
total_revenue=data["Total Sales"].sum()
print("\nTotal Revenue:",total_revenue)
best_product=data.loc[data["Quantity"].idxmax(),"Product"]
print("\nBest-Selling Product:",best_product)
highest_revenue_product=data.loc[data["Total Sales"].idxmax(),"Product"]
highest_revenue=data["Total Sales"].max()
print("\nHighest Revenue Product:",highest_revenue_product)
print("\nRvenue:",highest_revenue)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.barh(data["Product"],data["Total Sales"])

plt.xlabel("Products")
plt.ylabel("Total Sales")
plt.title("Product Wise-Sales Analysis")

plt.tight_layout()
plt.savefig("product_wise_sales.png",dpi=300)

plt.show()



    
