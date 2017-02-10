import numpy as np 
from scipy import misc
import ConfigParser

config = ConfigParser.ConfigParser()

config.read(".config")

data = np.random.uniform(size=config.getint("sec_one","num"))
img = misc.imread("img.jpg")

misc.imsave("/home/vikweg/Dropbox/sumatra_test/img1.png",img)
misc.imsave("/home/vikweg/Dropbox/sumatra_test/img2.png",img)
misc.imsave("/home/vikweg/Dropbox/sumatra_test/img3.png",img)

np.save("/home/vikweg/Dropbox/sumatra_test/rnddata1.npy",data)
np.save("/home/vikweg/Dropbox/sumatra_test/rnddata2.npy",data)
