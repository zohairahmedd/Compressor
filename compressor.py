import PIL # Python Imaging Library (PIL)
from PIL import Image
from tkinter.filedialog import * # standard Python interface to the Tk GUI toolkit

file_path = askopenfilename() # opens file explorer to allow user to select any file
img=PIL.Image.open(file_path) # opens file and returns the value of the image object which is then stored in img
myHeight, myWidth = img.size # receives the size of image in pixels

img = img.resize((myHeight, myWidth), PIL.Image.Resampling.LANCZOS) # resizes the image to specified dimensions (doesn't change the dimensions only size)
save_path = asksaveasfilename() # allows user to select a path where they want to save the image
img.save(save_path+ "compressed.jpg") # saves resized image to the specified path and names it "compressed.jpg"