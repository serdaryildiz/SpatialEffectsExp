import random

import cv2
import numpy
from PIL import Image, ImageDraw


class RandomCircleGenerator:

    def __init__(self, **kwargs):
        self.line_width = None
        self.fill = None
        self.circle_color = "white"
        self.background_color = "black"
        self.radius = None
        self.num_circles = None
        self.image_height = None
        self.image_width = None
        self.radius_min = None
        self.radius_max = None
        for k, v in kwargs.items():
            setattr(self, k, v)
        return

    def get_random_image(self,
                         image_width: int = None,
                         image_height: int = None,
                         num_circles: int = None,
                         radius: int = None,
                         circle_color: str = None,
                         fill: str = None,
                         line_width: int = None,
                         ) -> numpy.ndarray:
        # set arguments
        if image_width is None:
            image_width = self.image_width
            assert image_width is not None

        if image_height is None:
            image_height = self.image_height
            assert image_height is not None

        if num_circles is None:
            num_circles = self.num_circles
            assert num_circles is not None

        if radius is None:
            radius = self.radius
            if radius is None:
                radius = random.randint(self.radius_min, self.radius_max)

        if circle_color is None:
            circle_color = self.circle_color
            assert circle_color is not None

        if fill is None:
            fill = self.fill
            if fill is None:
                fill = circle_color

        if line_width is None:
            line_width = self.line_width
            if line_width is None:
                line_width = 0

        image = Image.new("RGB", (image_width, image_height), self.background_color)

        for i_circle in range(num_circles):
            x = random.randint(radius, image_width - radius)
            y = random.randint(radius, image_height - radius)
            image = self.draw_circle(image, x, y, radius, circle_color, fill, line_width)
        return numpy.array(image)

    @staticmethod
    def draw_circle(image: Image,
                    x: int,
                    y: int,
                    radius: int,
                    circle_color: str,
                    fill: str,
                    width: int) -> Image:
        left_top = (x - radius, y - radius)
        right_bottom = (x + radius, y + radius)
        bounding_box = [left_top, right_bottom]

        draw = ImageDraw.Draw(image)
        draw.ellipse(bounding_box, fill=fill, outline=circle_color, width=width)
        return image


if __name__ == '__main__':
    circleGenerator = RandomCircleGenerator(**{
        "line_width": 512,
        "fill": "white",
        "circle_color": "white",
        "background_color": "black",
        "radius": 10,
        "num_circles": 1,
        "image_height": 512,
        "image_width": 512,
    })
    img = circleGenerator.get_random_image()
    cv2.imshow("", img[..., ::-1])
    cv2.waitKey(0)
