import numpy as np 
import configparser

PATH = "./"

# Read the config file
config = configparser.ConfigParser()
config.read(".config")

# Produce some data
data = np.random.uniform(size=config.getint("sec_one","num"))
img_in_file = open("img.jpg","rb")
img = img_in_file.read()

# Produe some output
img_out_file = open(PATH+"img1.png","wb")
img_out_file.write(img)
np.save(PATH+"rnddata1.npy",data)
np.save(PATH+"rnddata2.npy",data)

# Write to stdout
print("Demo finished")
