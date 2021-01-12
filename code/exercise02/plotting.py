import numpy as np 
import matplotlib.pyplot as plt 

data = np.loadtxt("bandwidth.dat") # reads into 2D numpy array 

plt.figure()
plt.loglog(data[:,0],data[:,1],'.-')
axes = plt.gca() # get object 
axes.set_xscale("log",basex=2)
# axes.set_yscale("log",basey=2)
plt.axvline(x=32,color='r') # L1 cache 
plt.axvline(x=256,color='g') # L2 cache 
plt.axvline(x=30*1024,color='k') # L3 cache (shared)
plt.xlabel("Vector size [kB]")
plt.ylabel("Bandwidth [MBytes/s]")
plt.show()