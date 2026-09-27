import matplotlib.pyplot as plt

year = [2000,2005,2010,2015,2020,2025,2030]
revenu1 = [10,50,100,40,70,200,150]

year = [2000,2005,2010,2015,2020,2025,2030]
revenu2 = [15,30,10,45,73,100,10]

plt.plot(year,revenu1,label="revenu1 in specific yr")
plt.plot(year,revenu2,label="revenu2 in specific yr")
plt.xlabel("in year")
plt.ylabel("revenu in that yr")
plt.title("revenu generated in specific yr")
plt.legend()
plt.show()