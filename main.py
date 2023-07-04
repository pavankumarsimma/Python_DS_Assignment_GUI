#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import Download
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.rotate import RotateImage
from my_package.data.transforms.rescale import RescaleImage
import numpy as np
from PIL import Image

from pathlib import Path

def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    _ds=Dataset(annotation_file, transforms)
    _dd=Download()

    #Print image names and their captions from annotation file using dataset object
    for i in range(len(_ds.data)):
        x = _ds.__getann__(i)
        print(x["file_name"])
        for j in range(len(x["captions"])):
            print((x["captions"])[j])
        
        print()

    #Download images to ./data/imgs/ folder using download object
    for i in range(len(_ds.data)):
        x = _ds.__getann__(i)
        path = Path("./data/imgs/")
        filename = path/x["file_name"]
        _dd.__call__(filename, x["url"])

    #Transform the required image (roll number mod 10) and save it seperately
    x = _ds.__transformitem__("./data/imgs/0.jpg")
    if type(x)==np.ndarray:
        x = Image.fromarray(x)
    x.save("./data/outputs/0.jpg")

    #Get the predictions from the captioner for the above saved transformed image  
    y = captioner("./data/outputs/0.jpg", 3)
    print("Captions of transformed image: ")
    for i in range(len(y)):
        print(y[i])
    print()
    
    #Analysis task
    def analysis(inpath, outpath):
        img = Image.open(inpath)
        (s, j) = img.size
        if s<=j:
            p = s
        else:
            p = j
        x  = [None, FlipImage(), BlurImage(1), RescaleImage(int(2*p)), RescaleImage(int(0.5*p)), RotateImage(270), RotateImage(45)]
        i = 1
        if x:
            for transform in x:
                if transform!=None:
                    img = transform(img)
                path = Path(outpath)
                file_path = path/'0_{}.jpg'.format(i)
                img.save(file_path)
                z = captioner(file_path, 3)
                print("Captions of transformed image {}: ".format(i))
                for k in range(len(z)):
                    print(z[k])
                print()
                i=i+1    
                
                
    analysis('./data/imgs/0.jpg', './data/outputs/')
    

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(2)], "./data/outputs/") # Sample arguments to call experiment()
    

if __name__ == '__main__':
    main()