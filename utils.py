from src.models import BackgroundImage, Image
from io import BytesIO
from PIL import Image as img, ImageDraw, ImageFont


def adding_frame(bg_img_id, user_img_id):
   # Open the background image (1920x1080)
   bg_image = BackgroundImage.query.filter_by(id = bg_img_id).first()
   background_image = img.open(BytesIO(bg_image.image))

   # Open the image you want to place (200x200)
   user_image = Image.query.filter_by(id = user_img_id).first()
   image_to_place = img.open(BytesIO(user_image.image))
   image_to_place = image_to_place.resize((250, 250))

   # Get the size of the background image
   bg_width, bg_height = background_image.size

   # Get the size of the image to place
   place_width, place_height = image_to_place.size

   # Calculate the position to place the image (bottom right corner)
   x_position = bg_width - place_width -50
   y_position = bg_height - place_height -100

   # Paste the image onto the background
   background_image.paste(image_to_place, (x_position, y_position))

   # Save the result
   # background_image.save("result.jpg")
   buffer = BytesIO()
   background_image.save(buffer, format='JPEG')

   # Close the images
   background_image.close()
   image_to_place.close()

   # return background_image
   return buffer.getvalue()
