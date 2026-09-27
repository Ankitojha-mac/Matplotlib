import matplotlib.pyplot as plt
product = ["a","b","c","d","e"]
sale = [2,3,5,7,9]
plt.pie(sale , labels = product , autopct = "%1.1f%%" , colors = ["lightgreen","lightblue","lightcoral" ,"lightyellow","lightpink" ])

plt.title("total sale this week")
plt.show()