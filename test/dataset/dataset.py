from PIL import Image, ImageDraw
import random

class RandomImageGenerator:
    def __init__(self, width, height, num_circles):
        self.width = width
        self.height = height
        self.num_circles = num_circles
        self.image = Image.new("RGB", (width, height), "black")
        self.draw = ImageDraw.Draw(self.image)

    def draw_random_circles(self):
        for _ in range(self.num_circles):
            radius = random.randint(10, 50)
            x = random.randint(radius, self.width - radius)
            y = random.randint(radius, self.height - radius)
            color = "white"
            self.draw_circle(x, y, radius, color)

    def draw_circle(self, x, y, radius, color):
        left_top = (x - radius, y - radius)
        right_bottom = (x + radius, y + radius)
        bounding_box = [left_top, right_bottom]
        self.draw.ellipse(bounding_box, fill=color, outline=color)

    def save_image(self, filename):
        self.image.save(filename)

# Example usage:
width = 500
height = 500
num_circles = 10
image_generator = RandomImageGenerator(width, height, num_circles)
image_generator.draw_random_circles()
image_generator.save_image("random_image.png")