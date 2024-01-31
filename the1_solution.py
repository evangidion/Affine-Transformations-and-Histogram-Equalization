# Andaç Berkay Seval 2235521
# Asrın Doğrusöz 2380301

import os
import matplotlib.pyplot as plt
from skimage import io, img_as_ubyte
from skimage.transform import rotate
from skimage import exposure


INPUT_PATH = "./THE1_Images/"
OUTPUT_PATH = "./Outputs/"

def read_image(img_path, rgb = True):
    if rgb == False:
        img = io.imread(img_path, as_gray = True)
    else:
        img = io.imread(img_path)
    return img

def write_image(img, output_path, rgb = True):
    image = img_as_ubyte(img)
    io.imsave(output_path, image)

def extract_save_histogram(img, path):
    plt.hist(img.ravel(), bins=50)
    plt.savefig(path)
    plt.clf()

def rotate_image(img, degree = 0, interpolation_type = "linear"):
    #interpolation type: "linear" or "cubic"
    #degree: 45 or 90
    if interpolation_type == "linear":
        rotated = rotate(img, angle=-degree, order=1)
    else:
        rotated = rotate(img, angle=-degree, order=3)

    return rotated

def histogram_equalization(img):
    img_hist_eq = exposure.equalize_hist(img)
    return img_hist_eq

def adaptive_histogram_equalization(img):
    adapt_hist_eq = exposure.equalize_adapthist(img)
    return adapt_hist_eq

if __name__ == '__main__':
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    #PART1
    img = read_image(INPUT_PATH + "a1.png")
    output = rotate_image(img, 45, "linear")
    write_image(output, OUTPUT_PATH + "a1_45_linear.png")

    img = read_image(INPUT_PATH + "a1.png")
    output = rotate_image(img, 45, "cubic")
    write_image(output, OUTPUT_PATH + "a1_45_cubic.png")

    img = read_image(INPUT_PATH + "a1.png")
    output = rotate_image(img, 90, "linear")
    write_image(output, OUTPUT_PATH + "a1_90_linear.png")

    img = read_image(INPUT_PATH + "a1.png")
    output = rotate_image(img, 90, "cubic")
    write_image(output, OUTPUT_PATH + "a1_90_cubic.png")

    img = read_image(INPUT_PATH + "a2.png")
    output = rotate_image(img, 45, "linear")
    write_image(output, OUTPUT_PATH + "a2_45_linear.png")

    img = read_image(INPUT_PATH + "a2.png")
    output = rotate_image(img, 45, "cubic")
    write_image(output, OUTPUT_PATH + "a2_45_cubic.png")

    #PART2
    img = read_image(INPUT_PATH + "b1.png", rgb = False)
    extract_save_histogram(img, OUTPUT_PATH + "original_histogram.png")
    equalized = histogram_equalization(img)
    equalized = img_as_ubyte(equalized)
    extract_save_histogram(equalized, OUTPUT_PATH + "equalized_histogram.png")
    write_image(equalized, OUTPUT_PATH + "enhanced_image.png")

    # BONUS
    # Define the following function
    equalized = adaptive_histogram_equalization(img)
    equalized = img_as_ubyte(equalized)
    extract_save_histogram(equalized, OUTPUT_PATH + "adaptive_equalized_histogram.png")
    write_image(equalized, OUTPUT_PATH + "adaptive_enhanced_image.png")





