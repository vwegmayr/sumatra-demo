import numpy as np 
import ConfigParser

config = ConfigParser.ConfigParser()

config.read(".config")

data = np.random.uniform(size=config.getint("sec_one","num"))
img_in_file = open("img.jpg","rb")
img = img_in_file.read()

path = "full/path/to/Dropbox/ise-squad/"

img_out_file = open(path+"img1.png","wb")
img_out_file.write(img)
np.save(path+"rnddata1.npy",data)
np.save(path+"rnddata2.npy",data)
