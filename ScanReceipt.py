import cv2
import os
import pytesseract
import numpy as np

# Jan 7[not able to scan pdf + planning to store the date and item description from the image so that we can store them in a database and easy to query ???]

# https://medium.freecodecamp.org/getting-started-with-tesseract-part-i-2a6a6b1cf75e

# def get_string():
#     # Read image using opencv
#     img_path='/home/chanakya/Pictures/image-20160515_215338.jpg'
#     img = cv2.imread(img_path)
#     output_dir='/home/chanakya/Pictures/ML'

#     # Extract the file name without the file extension
#     file_name = os.path.basename(img_path).split('.')[0]
#     file_name = file_name.split()[0]

#     print(file_name)

#     # Create a directory for outputs
#     output_path = os.path.join(output_dir, file_name)

#     if not os.path.exists(output_path):
#         os.makedirs(output_path)

# Read image using opencv
img_path=''
img = cv2.imread(img_path)
output_dir=''

# Extract the file name without the file extension
file_name = os.path.basename(img_path).split('.')[0]

# print(file_name)
file_name = file_name.split()[0]
# print(file_name)

# print(file_name)

# Create a directory for outputs
output_path = os.path.join(output_dir, file_name)

if not os.path.exists(output_path):
    os.makedirs(output_path)

# img=''

img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

# # Convert to gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# Apply blur to smooth out the edges
img = cv2.GaussianBlur(img, (5, 5), 0)

# Apply threshold to get image with only b&w (binarization)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# Save the filtered image in the output directory
# save_path = os.path.join(output_path, file_name + "_filter_" + str(method) + ".jpg")
save_path = os.path.join(output_path, file_name + "_filter_.jpg")
cv2.imwrite(save_path, img)

# Recognize text with tesseract for python
result = pytesseract.image_to_string(img, lang="eng")

result_split=result.split(' ')

print(result)
# # return result
