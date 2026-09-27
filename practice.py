import matplotlib.pyplot as plt 
roll =[1,2,3]
marks=[50,60,70]
roll2 =[1,2,3]
marks2 =[45,50,70] 

plt.scatter(roll,marks, color="blue",label = "class 1 student marks")
plt.scatter(roll2 ,marks2, color="red",label = "class 2 student marks")
plt.xlabel("roll no. of each student")
plt.ylabel("marks of each student")
plt.legend()
plt.grid()
plt.show()