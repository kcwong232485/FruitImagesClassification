# Directory of fruits
import os
directory_path = os.getcwd()
# define the train and test images path
train_dir = directory_path + '\\inputimages\\train\\'
test_dir = directory_path + '\\inputimages\\test\\'

import pandas as pd
dfTrainFruit = pd.DataFrame() # empty dataframe
# global lists
fruits_name = []
fruits_image = []
fruits_dir = [] 

# dummy function
def getDummy():
    print("dummy")

# list the image file(s)
def listImages(thisdir):
    for dirname, _, filenames in os.walk(thisdir):
        for filename in filenames:
            if filename.split(".")[-1] == "txt": 
                continue
            print(os.path.join(dirname, filename))

# fill the lists 
def fillTheLists():
    global fruits_name
    global fruits_image
    global fruits_dir
    ' clear the lists before fill
    fruits_name = []
    fruits_image = []
    fruits_dir = []
    i = 0
    for subdir in os.listdir(train_dir):
        fruits_dir.append(i) # name of the fruit i.e. label
        i += 1
        for image_filename in os.listdir(train_dir + subdir):
            if image_filename.split(".")[-1] == "txt":
                continue
            fruits_name.append(subdir) # name of the fruit 
            fruits_image.append(subdir + '/' + image_filename) # image of the fruit

# fill the Train Fruit
def fillTheDataFrame():  
    global dfTrainFruit
    global fruits_name
    global fruits_image
    # list the images in dataframe  
    dfTrainFruit["Fruits"] = fruits_name
    dfTrainFruit["Fruits Image"] = fruits_image

import pandas as pd
# fill The Train Fruit alternative
def fillTheDataFrame2():
    global dfTrainFruit
    global fruits_name
    global fruits_image
    # combine 2 lists to list of list
    new_lst = [list(x) for x in zip(fruits_name, fruits_image)]
    dfTrainFruit = pd.DataFrame(new_lst, columns=["Fruits", "Fruits Image"])    
    
from collections import Counter
# count for each fruit using collection
def countForEach():
    global lstFruit
    # dictFruit is a dictionary
    dictFruit = Counter(dfTrainFruit["Fruits"])     
    lstFruit = dictFruit.most_common()
    print("Found fruits in the data set and their corresponding count of image(s)")
    print(lstFruit)

from glob import glob    
# show how many type(s) of fruit
def howmanyType():
    global numberOfClass 
    fruitCountUnique = glob(train_dir + '/*' )
    # declare numberOfClass i.e. 5 fruits
    numberOfClass = len(fruitCountUnique)
    print("How many different fruits: ", numberOfClass)
    
# list each fruit
def listForFruit():  
    global lstFruit
    global x
    global y
    if len(lstFruit) == 0:
        print("Provided list(i.e. lstFruit) is empty!")
        return
    # lstFruit = [('apple', 100), ('banana', 100), ('mango', 100), ('orange', 100), ('strawberry', 100)]
    x,y = zip(*lstFruit)
    x,y = list(x),list(y)
    print("Found fruits: ", x)
    print("Number of Images: ", y)

import matplotlib.pyplot as plt
import seaborn as sns    
# plot graphic for each fruit
def plotForFruit():
    global x
    global y
    if (len(x) == 0 or len(y) == 0):
        print("Provided x-list or y-list is empty!")
        return
    plt.figure(figsize=(5,5))
    ax= sns.barplot(x=x, y=y, palette=sns.color_palette("BuGn_r", 15)) 
    plt.xlabel('Fruits', size = 20) 
    plt.ylabel('Number of Fruits', size = 20 )
    plt.xticks(rotation = 75)
    plt.title('Found fruits in the data set and their number') 
    plt.show()


import cv2
from tensorflow.keras.utils import load_img
def plotOneForEach():
    global dfTrainFruit
    global x
    plt.figure(figsize=(25,16))
    how_many_fruits = len(x)
    for i in range(how_many_fruits):
        fruits = dfTrainFruit[dfTrainFruit["Fruits"] == x[i]]["Fruits Image"].values [1]    
        plt.subplot(3,5,i+1)
        img = load_img(train_dir + fruits, target_size=(72, 72))    
        plt.imshow(img)
        plt.title(x[i].upper(), color = "green", fontsize = 15 , fontweight = 600)
        plt.axis("off")
    plt.suptitle("Fruits' label(s)", fontsize = 25 , color = "darkred", fontweight = 'bold')
    plt.show()

from tensorflow.keras.utils import img_to_array
def plotOneImage(whichfruit, whichimage):
    global img    
    # open an image
    img = load_img(train_dir + "/" + whichfruit + "/" + whichimage + ".jpg")     
    plt.imshow(img)
    plt.axis("off")
    plt.title("Image of " + whichimage + " (" + whichfruit + ")")
    plt.show()

def getImageShape():
    global img
    array_image = img_to_array(img)
    print("Image Shape: ", array_image.shape)
    
