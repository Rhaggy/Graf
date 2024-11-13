import matplotlib.pyplot as plt



a = float(input("Mata in a:"))
b = float(input("Mata in b:"))
c = float(input("Mata in c:"))

x_list = [x for x in range(-100,101)]
y_list = []
 
for x in x_list:
    y = a*x**2+ + b*x + c
    y_list.append(y)

plt.plot(x_list,y_list)
plt.grid()
plt.show()

