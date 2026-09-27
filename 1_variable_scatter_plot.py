import matplotlib.pyplot  as plt
hour = [1,2,3,5,7,9]
marks =[20,40,60,70,90,100]
plt.scatter(hour , marks , cmap= "plasma" , c= marks, marker= "^" , label = "marks obtain" )
plt.xlabel("hours of study")
plt.ylabel("marks obtain")
plt.legend()
plt.title("hour to marks")
plt.grid()
plt.colorbar()
plt.show()
