#Imports
from PIL import Image
import numpy as np
class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        """assert isinstance(output_size, (int, tuple))
        self.output_size = output_size
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)"""
        self.output_size = output_size
        
    
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        self.size = image.size
        if type(self.output_size)==tuple:
            self.output = self.output_size
        else:
            if self.size[0]<=self.size[1]:
                self.output = (self.output_size, int((self.output_size)*(self.size[1]/self.size[0])))
            else:
                self.output = (int((self.output_size)*(self.size[0]/self.size[1])), self.output_size)
        
        
        image = Image.fromarray(image) if isinstance(image, np.ndarray) else image
        image = image.resize(self.output)
        return image


"""

        
        
        else:
            i = self.output_size
            self.output_size = (int(i*self.size[0]), int(i*self.size[1]))
        """