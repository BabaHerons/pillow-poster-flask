from src import app


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

# # Open the background image (1920x1080)
# background_image = img.open("background.jpg")

# # Open the image you want to place (200x200)
# image_to_place = img.open("image_to_place.jpg")
# image_to_place = image_to_place.resize((200, 200))

# # Get the size of the background image
# bg_width, bg_height = background_image.size

# # Get the size of the image to place
# place_width, place_height = image_to_place.size

# # Calculate the position to place the image (bottom right corner)
# x_position = bg_width - place_width
# y_position = bg_height - place_height

# # Paste the image onto the background
# background_image.paste(image_to_place, (x_position, y_position))

# # Save the result
# background_image.save("result_image.jpg")

# # Close the images
# background_image.close()
# image_to_place.close()


# # Open the desired Image you want to add text on
# i = img.open('background.jpg')

# # Call draw Method to add 2D graphics in an image
# Im = ImageDraw.Draw(i)
# mf = ImageFont.truetype(font="arial.ttf", size=100)
# # Add Text to an image
# Im.text((90, 10), "Working",fill=(0, 0, 0),font=mf)

# # Display edited image
# i.show()

# # Save the edited image
# i.save("sn.png")
