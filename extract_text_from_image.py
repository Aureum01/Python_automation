from PIL import Image
from pytesseract import pytesseract
import os

#Main path
PATH = r'C:\Image_location'

#Define path
IMAGE_PATH = r'images/'

#CMD to exe
pytesseract.tesseract_cmd = PATH

#pull names from file directory 
for root, dirs, file_names in os.walk(IMAGE_PATH):
	for file_name in file_names:
		pix = Image.open(IMAGE_PATH + file_name)
		
		#extract text 
		etext = pytesseract.img_to_string(pix)
		print(text)
