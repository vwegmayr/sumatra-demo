import numpy as np 
from scipy import misc
import ConfigParser

config = ConfigParser.ConfigParser()

config.read(".config")

data = np.random.uniform(size=config.getint("sec_one","num"))
img = misc.imread("img.jpg")

misc.imsave("Data/img1.png",img)
misc.imsave("Data/img2.png",img)
misc.imsave("Data/img3.png",img)

np.save("Data/rnddata1.npy",data)
np.save("Data/rnddata2.npy",data)
