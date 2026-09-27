import matplotlib.pyplot as plt
x = ['Monday' , "Tuesday" , "Wednesday" ,"Thursday" , "Friday" ,"Saturday" , "Sunday"]
y = [20,25,28,35,7,16,0]
plt.plot(x,y)
plt.title("BOOK SOLD THIS WEEK")
plt.xlabel("DAYS OF WEEK")
plt.ylabel("QUANTITY SOLD ")
plt.show()