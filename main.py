import numpy as np 
import ConfigParser

config = ConfigParser.ConfigParser()

config.read(".config")

data = np.random.uniform(size=config.getint("sec_one","num"))
img_in_file = open("img.jpg","rb")
img = img_in_file.read()

img_out_file = open("~/Dropbox/ise-squad/img1.png","wb")
img_out_file.write(img)
np.save("~/Dropbox/ise-squad/rnddata1.npy",data)
np.save("~/Dropbox/ise-squad/rnddata2.npy",data)
