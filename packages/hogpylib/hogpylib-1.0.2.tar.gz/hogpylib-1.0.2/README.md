# HOG_python
### Histogram of Gradients in Python from scratch

```python
import sys
from skimage import color, data
import matplotlib.pyplot as plt

from hogpylib.hog import HistogramOfGradients

def main(args=None):
    from skimage.feature import hog

    PIXELS_PER_CELL = (8, 8)
    CELLS_PER_BLOCK = (2, 2)
    NUMBER_OF_BINS = ORIENTATIONS = 9  # NUMBER_OF_BINS
    VISUALISE = True

    orig_img = color.rgb2gray(data.astronaut())
    # orig_img = color.rgb2gray(skimage.io.imread("../data/people.jpg"))
    custom_hog = HistogramOfGradients(pixels_per_cell=PIXELS_PER_CELL,
                                      cells_per_block=CELLS_PER_BLOCK,
                                      num_of_bins=NUMBER_OF_BINS,
                                      visualise=VISUALISE)
    hog_features, hog_image = custom_hog.compute_features(orig_img)

    hog_features_check, hog_image_scikit = hog(orig_img,
                                               orientations=ORIENTATIONS,
                                               pixels_per_cell=PIXELS_PER_CELL,
                                               cells_per_block=CELLS_PER_BLOCK,
                                               block_norm='L2',
                                               visualize=VISUALISE)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')

    ax1.imshow(orig_img, cmap=plt.get_cmap('gray'))
    ax1.set_title('Input Image')

    ax2.imshow(hog_image, cmap=plt.get_cmap('gray'))
    ax2.set_title('Custom HOG')

    ax3.imshow(hog_image_scikit, cmap=plt.get_cmap('gray'))
    ax3.set_title('Scikit HOG')
    plt.show()


if __name__ == "__main__":
    sys.exit(main())
```

## Result

<img src="https://github.com/shubhamwagh/HOG_python/raw/main/examples/HOG_implementation.png" width="700">
<img src="https://github.com/shubhamwagh/HOG_python/raw/main/examples/HOG_people.png" width="700">
<img src="https://github.com/shubhamwagh/HOG_python/raw/main/examples/Hog_car.png" width="700">

## References

[1] http://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf


[2] [HOG Image rendering](https://github.com/scikit-image/scikit-image/blob/main/skimage/feature/_hog.py#L245-L265)

[3] [HOG bin distribution](https://courses.cs.duke.edu/compsci527/fall15/notes/hog.pdf)
