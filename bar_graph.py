import matplotlib.pyplot  as plt
product = ["toy","chips","oil","cloths","bag" ]
sale = [24,15,6,20,9]
plt.bar(product , sale , color = "red" , label = "sale this months")
#for horizontal plot put barh
plt.xlabel("Product Name")
plt.ylabel("Quantity Sale")
plt.title("Total")
plt.legend()
for i in range(len(product)):
    plt.text(product[i],sale[i],str(sale[i]),ha="center")
plt.show()

