import matplotlib.pyplot  as plt
plt.scatter([1,2,3],[50,60,70] , color = "blue" , marker= "^" , label = "class A" )
plt.scatter([1,2,3],[45,50,70] ,color = "red" , marker= "^" , label = "class B" )
plt.xlabel("hours of study")
plt.ylabel("marks obtain")
plt.legend()
plt.title("hour to marks")
plt.grid()
plt.show()
