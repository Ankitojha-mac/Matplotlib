import matplotlib.pyplot as plt
days = [ "mon" , "tue","wed","thurs"]
city = ["patna","bhoapl","pune","delhi" ]
temp = [
    [22,32,31,16,19],
    [30,27,25,20,24],
    [19,27,29,24,23],
    [17,19,23,26,23]]

plt.plot(days,temp,color="red", label = city ,marker = "<")
plt.xlabel("name of days")
plt.ylabel("temp in c ")
plt.legend()
plt.grid()
plt.show()