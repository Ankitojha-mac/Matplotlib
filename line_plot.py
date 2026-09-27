import matplotlib.pyplot as plt
x = ['Mon' , "Tue" , "Wed" ,"Thu" , "Fri" ,"Sat" , "Sun"]
y = [20,25,28,35,7,16,0]
plt.plot(x,y,color = "red" , linestyle  = "--" , linewidth = "2" , marker = "o", label = " week sale data")
plt.title("BOOK SOLD THIS WEEK")
plt.xlabel("DAYS")
plt.ylabel("QUANTITY SOLD ")
plt.grid(color = "black" , linestyle =":")
plt.legend(loc = "upper left" )
plt.show()