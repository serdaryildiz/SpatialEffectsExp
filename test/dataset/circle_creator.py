import cv2

from Dataset.circles import RandomCircleGenerator


def circle_generator_test():
    parameters = {
        "line_width": 1,
        "fill": "white",
        "circle_color": "white",
        "background_color": "black",
        "radius": 10,
        "num_circles": 1,
        "image_height": 512,
        "image_width": 512,
    }

    circle_generator = RandomCircleGenerator(**parameters)

    for _ in range(10):
        img = circle_generator.get_random_image()
        cv2.imshow("", img[..., ::-1])
        cv2.waitKey(0)

    parameters["fill"] = "black"
    circle_generator = RandomCircleGenerator(**parameters)

    for _ in range(10):
        img = circle_generator.get_random_image()
        cv2.imshow("", img[..., ::-1])
        cv2.waitKey(0)

    parameters["radius"] = None
    parameters["radius_min"] = 10
    parameters["radius_max"] = 100
    circle_generator = RandomCircleGenerator(**parameters)

    for _ in range(10):
        img = circle_generator.get_random_image()
        cv2.imshow("", img[..., ::-1])
        cv2.waitKey(0)

    parameters["line_width"] = 10
    circle_generator = RandomCircleGenerator(**parameters)

    for _ in range(10):
        img = circle_generator.get_random_image()
        cv2.imshow("", img[..., ::-1])
        cv2.waitKey(0)

    return


if __name__ == '__main__':
    circle_generator_test()
