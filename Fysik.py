import matplotlib.pyplot as plt
import numpy as np
Temp_hemma = [1.9,1.8, -2.5, -2.6, -1.4, -1.2, -4.7, -4.7, 1.3, 1.2]
Temp_Brygga = [4, 3, 3, 0, -3, -2, -5, -5, 1, 1]
Temp_I_Sjön = [5,5,0.5,1,1,1,1,1,1,1]
Temp_SMHI = [4,4,-4,-4,-1,-1,-5,-5,0,0]


plt.plot(Temp_hemma, "-r8", label="Temp Hemma")
plt.plot(Temp_Brygga, "-g8")
plt.plot(Temp_I_Sjön, "-b8")
plt.plot(Temp_SMHI, "-c8")
plt.grid()
plt.ylabel("Tempratur (°C)")
plt.xlabel("Mätning")
plt.axhline(y=0)
plt.xticks(np.arange(0,12, step=1))
plt.yticks(np.arange(-6,6, step= 0.5))
plt.xlim(0,11)


plt.show()
