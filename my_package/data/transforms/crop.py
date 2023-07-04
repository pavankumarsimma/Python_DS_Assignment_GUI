#Imports
from PIL import Image
import random
import numpy as np

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if self.crop_type == 'center':
            return self.center_crop(image)
        elif self.crop_type == 'random':
            return self.random_crop(image)
        else:
            raise ValueError(f"Invalid crop type {self.crop_type}, choose either center or random")

    def center_crop(self, image):
        '''
            Center crop the given image to the desired shape
        '''
        if type(image) == np.ndarray:
            image = Image.fromarray(image)
        width, height = image.size
        new_width, new_height = self.shape

        left = (width - new_width) // 2
        top = (height - new_height) // 2
        right = (width + new_width) // 2
        bottom = (height + new_height) // 2

        return image.crop((left, top, right, bottom))

    def random_crop(self, image):
        '''
            Random crop the given image to the desired shape
        '''
        if type(image) == np.ndarray:
            image = Image.fromarray(image)
        width, height = image.size
        new_width, new_height = self.shape

        left = random.randint(0, width - new_width)
        top = random.randint(0, height - new_height)
        right = left + new_width
        bottom = top + new_height

        return image.crop((left, top, right, bottom))
