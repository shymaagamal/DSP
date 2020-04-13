## This is the abstract class that the students should implement

from modesEnum import Modes
import numpy as np



from modesEnum import Modes

import cv2 as cv
from PyQt5.QtGui import QPixmap ,QImage
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib import pyplot as plt
import  logging 

logger=logging.getLogger(__name__)
fileHandler=logging.FileHandler('ApplicationWindow.log')
Formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
streamHandler=logging.StreamHandler()
streamHandler.setFormatter(Formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
fileHandler.setFormatter(Formatter)

class ImageModel():

    """
    A class that represents the ImageModel"
    """
    
    def __init__(self):

        pass
    
    def __init__(self, imgPath: str):
        self.imgPath = imgPath
        ###
        # ALL the following properties should be assigned correctly after reading imgPath 
        ###
        
        self.imgByte = cv.imread(self.imgPath,cv.IMREAD_GRAYSCALE)
        self.imgByte = np.asarray( self.imgByte, dtype="int32"  )
        self.dft = np.fft.fft2(self.imgByte)
        self.dft = np.fft.fftshift(self.dft) 

        self.magnitude =np.abs(self.dft)

        self.Real=np.real(self.dft)
        self.real=np.array(self.Real).reshape(-1,2).astype(np.int32)

        self.Imaginary = np.imag(self.dft)
        self.imaginary=np.array(self.Imaginary)
        
        self.phase = np.angle(self.dft)
        self.invmagnitude=None
        self.invphase=None
        self.unimagnitude=np.ones(self.magnitude.shape,dtype=None ,order='C')
        self.uniphase=np.zeros(self.phase.shape,dtype=None ,order='C')
        self.invmagnitude = np.fft.ifft2(np.fft.ifftshift( self.magnitude))
        self.invphase = np.fft.ifft2(np.fft.ifftshift( self.phase))
    def image_Display(self,winDisplay):
        try:
            self.imgByte.shape
            print(self.imgByte.shape)
            self.image=QImage(self.imgByte, self.imgByte.shape[0],self.imgByte.shape[1],QImage.Format_Grayscale8)
            self.image=QPixmap.fromImage(self.image)
            winDisplay.setScaledContents(True)
            winDisplay.setPixmap(self.image)
            
        except AttributeError:
            print("shape not found")
        logger.debug('Displayed Image')

    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode: 'Modes') -> np.ndarray:
        ###
        #a function that takes ImageModel object mag ratio, phase ration and
        #return the magnitude of ifft of the mix
        #3return type ---> 2D numpy array
        #please Add whatever functions realted to the image data in this file
        
        ###
        # implement this function
        ###
        if mode==Modes.PhaseAndMagnitudeMode.value:
            
            self.magnitudeImg2=imageToBeMixed.magnitude
            self.phaseImg2=imageToBeMixed.phase
            self.mixMag=self.magnitude * magnitudeOrRealRatio + self.magnitudeImg2*(1- magnitudeOrRealRatio)
            self.mixPhase=(1-phaesOrImaginaryRatio)* self.phase + phaesOrImaginaryRatio* self.phaseImg2
            self.mix=self.mixMag*np.exp(1j*self.mixPhase)
            self.mix=np.fft.ifft2(self.mix)
            logger.debug('mix between Phase and magnitude')
        elif mode==Modes.realAndImaginaryMode.value:
            self.realImg2=imageToBeMixed.real
            self.imagImg2=imageToBeMixed.imaginary
            self.mixReal=self.real * magnitudeOrRealRatio + self.realImg2*(1- magnitudeOrRealRatio)
            self.mixImag=(1-phaesOrImaginaryRatio)* self.imaginary + phaesOrImaginaryRatio* self.imagImg2
            self.mix=self.mixReal +self.mixImag
            
            self.mix=np.fft.ifft2(self.mix)
            self.mix=np.array(self.mix).reshape(-1,2)
            logger.debug('mix between Real and Imaginary')
        return self.mix
     