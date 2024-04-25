import os
import cloudinary
import cloudinary.uploader

cloudinary.config( 
  cloud_name = os.getenv('CLOUDINARY_NAME'), 
  api_key = os.getenv('CLOUDINARY_API_KEY'), 
  api_secret = os.getenv('CLOUDINARY_API_SECRET'),
  secure = True
)

response = cloudinary.uploader.upload('test.jpg')

print(response['url'])
