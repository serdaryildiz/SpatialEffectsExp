import numpy
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


class FeatureVectorVisualizer:

    def __init__(self):
        return

    @staticmethod
    def draw_2d_dist(feature_vector: numpy.array,
                     title: str = None,
                     colorbar: bool = True
                     ) -> None:
        assert len(feature_vector.shape) == 2, "feature vector has to be 2 dimension!"
        plt.imshow(feature_vector, cmap='gray')
        if colorbar:
            plt.colorbar()
        if title is None:
            h, w = feature_vector.shape
            plt.title(f'{h}x{w} Feature Vector Visualization')
        plt.show()
        return

    @staticmethod
    def vector2img(feature_vector: numpy.array) -> Image:

        # normalize feature vector
        normalized_feature_vector = ((feature_vector - numpy.min(feature_vector))
                                     / (numpy.max(feature_vector) - numpy.min(feature_vector))
                                     * 255)

        image = normalized_feature_vector.astype(numpy.uint8)
        image = Image.fromarray(image)
        return image



if __name__ == '__main__':
    feature = numpy.random.random([5, 5])
    FeatureVectorVisualizer.draw_2d_dist(feature)
