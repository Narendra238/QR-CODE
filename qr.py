# Importing library
import qrcode
 
# Data to be encoded
data = 'https://s.id/LINK'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('Hasil.png')