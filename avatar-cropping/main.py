from PIL import Image

image = Image.open("monro.jpg")
image = image.convert("RGB")

red, green, blue = image.split()

offset = 50

cropped_middle_coordinates = (offset/2, 0, (image.width - offset/2), image.height)
   
cropped_left_red = red.crop((offset, 0, red.width, red.height)) 
cropped_middle_red = red.crop(cropped_middle_coordinates) 
blended_red = Image.blend(cropped_left_red, cropped_middle_red,  0.2)

cropped_right_blue = blue.crop((0, 0,(blue.width - offset), blue.height)) 
cropped_middle_blue = blue.crop(cropped_middle_coordinates) 
blended_blue = Image.blend(cropped_right_blue, cropped_middle_blue, 0.2)

middle_green = green.crop(cropped_middle_coordinates)

final_image = Image.merge("RGB", (blended_red, blended_blue, middle_green))
final_image.thumbnail((80, 80))
final_image.save('final_image.jpg')

