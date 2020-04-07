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
        
        self.imgByte = None
        self.dft = None
        self.real =np.real(None)
        self.imaginary = None
        self.magnitude = None
        self.phase = None
        self.invmagnitude=None
        self.invphase=None
        self.unimagnitude=None
        self.uniphase=None
        
    def image_Display(self,winDisplay):
        try:
            self.imgPath.shape
            print(self.imgPath.shape)
            self.imgByte=QImage(self.imgPath, self.imgPath.shape[0],self.imgPath.shape[1],QImage.Format_Grayscale8)
            self.imgByte=QPixmap.fromImage(self.imgByte)
            winDisplay.setScaledContents(True)
            winDisplay.setPixmap(self.imgByte)
            
        except AttributeError:
            print("shape not found")
        logger.debug('Displayed Image')
    def magnitude_Component(self):
        self.dft = np.fft.fft2(self.imgPath)
        self.dft = np.fft.fftshift(self.dft) 
        self.magnitude =np.abs(self.dft)
        return self.magnitude
    def phase_Component(self):
        self.dft = np.fft.fft2(self.imgPath)
        self.dft = np.fft.fftshift(self.dft) 
    
        self.phase = np.angle(self.dft)
        return self.phase
    def real_Component(self):
        self.dft = np.fft.fft2(self.imgPath)
        self.dft = np.fft.fftshift(self.dft) 
    
        self.real=np.real(self.dft)
        self.real=np.array(self.real).reshape(-1,2).astype(np.int32)
        return self.real 
    def imaginary_Component(self):
        self.dft = np.fft.fft2(self.imgPath)
        self.dft = np.fft.fftshift(self.dft) 
    
        self.imaginary = np.imag(self.dft)
        self.imaginary=np.array(self.imaginary)
        return self.imaginary 
    def uni_Phase_Component(self):
        self.dft = np.fft.fft2(self.imgPath)
        self.dft = np.fft.fftshift(self.dft) 
    
        self.uniphase = np.angle(self.dft)
        self.uniphase=np.zeros(self.uniphase.shape,dtype=None ,order='C')
        return self.uniphase
    def uni_Magnitude_Component(self):
        self.dft = np.fft.fft2(self.imgPath)
        self.dft = np.fft.fftshift(self.dft) 
    
        self.unimagnitude = np.abs(self.dft)
        self.unimagnitude=np.ones(self.unimagnitude.shape,dtype=None ,order='C')
        return self.unimagnitude
    def invers_Magnitude_Component(self):
        self.dft = self.magnitude_Component()
        self.f_ishift = np.fft.ifftshift(self.dft)
        self.invmagnitude = np.fft.ifft2(self.f_ishift)
        return self.invmagnitude
    def invers_Phase_Component(self):
        self.dft = self.phase_Component()
        self.f_ishift = np.fft.ifftshift(self.dft)
        self.invphase = np.fft.ifft2(self.f_ishift)
        return self.invphase
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
            
            self.magnitudeImg2=imageToBeMixed.magnitude_Component()
            self.phaseImg2=imageToBeMixed.phase_Component()
            self.mixMag=self.magnitude_Component() * magnitudeOrRealRatio + self.magnitudeImg2*(1- magnitudeOrRealRatio)
            self.mixPhase=(1-phaesOrImaginaryRatio)* self.phase_Component() + phaesOrImaginaryRatio* self.phaseImg2
            self.mix=self.mixMag*np.exp(1j*self.mixPhase)
            self.mix=np.fft.ifft2(self.mix)
            logger.debug('mix between Phase and magnitude')
        elif mode==Modes.realAndImaginaryMode.value:
            self.realImg2=imageToBeMixed.real_Component()
            self.imagImg2=imageToBeMixed.imaginary_Component()
            self.mixReal=self.real_Component() * magnitudeOrRealRatio + self.realImg2*(1- magnitudeOrRealRatio)
            self.mixImag=(1-phaesOrImaginaryRatio)* self.imaginary_Component() + phaesOrImaginaryRatio* self.imagImg2
            self.mix=self.mixReal +self.mixImag
            
            self.mix=np.fft.ifft2(self.mix)
            self.mix=np.array(self.mix)
            logger.debug('mix between Real and Imaginary')
        return self.mix
     