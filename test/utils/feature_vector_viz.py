import numpy

from Utils import FeatureVectorVisualizer


def get_gaussian_filter(filter_size=10, sigma=1.0):
    gaussian_filter_2d = numpy.fromfunction(
        lambda x, y: (1 / (2 * numpy.pi * sigma ** 2)) *
                     numpy.exp(-((x - (filter_size - 1) / 2) ** 2 +
                                 (y - (filter_size - 1) / 2) ** 2) /
                               (2 * sigma ** 2)),
        (filter_size, filter_size)
    )
    gaussian_filter_2d /= numpy.sum(gaussian_filter_2d)
    return gaussian_filter_2d


def visualize_feature_vector():
    feature_vector = get_gaussian_filter(512, 100)
    FeatureVectorVisualizer.draw_2d_dist(feature_vector)
    return


def get_feature_vector_image():
    feature_vector = get_gaussian_filter(512, 100)
    image = FeatureVectorVisualizer.vector2img(feature_vector)
    image.show()
    return


if __name__ == '__main__':
    visualize_feature_vector()
    get_feature_vector_image()
