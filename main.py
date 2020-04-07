from PyQt5 import QtWidgets
from Qt import Ui_MainWindow
import sys
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QPixmap

from PyQt5 import QtCore, QtGui, QtWidgets
from modesEnum import Modes
from matplotlib import pyplot as plt
from imageModel import ImageModel
import imageModel
from PIL import Image
from numpy import asarray
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


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ImagButton1=0
        self.ImagButton2=0
        self.sizeFlag1=0
        self.sizeFlag2=0
        
        
        self.ui.DisplayIm_1.clicked.connect(lambda:self.whichBtn(self.ui.DisplayIm_1))
        
        self.ui.DisplayIm_1.clicked.connect(self.open_Image)
        self.ui.DisplayIm_2.clicked.connect(lambda:self.whichBtn(self.ui.DisplayIm_2))
        self.ui.DisplayIm_2.clicked.connect(self.open_Image)
        self.ui.comboBox_1.activated.connect(lambda:self.which_Com_Box(self.ui.comboBox_1))
        self.ui.comboBox_1.activated.connect(self.display_DFT)
        self.ui.comboBox_2.activated.connect(lambda:self.which_Com_Box(self.ui.comboBox_2))
        self.ui.comboBox_2.activated.connect(self.display_DFT)
        self.ui.horizontalSlider.valueChanged.connect(lambda:self.slider_Value(self.ui.horizontalSlider))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda:self.slider_Value(self.ui.horizontalSlider_2))
        self.ui.radioButton.toggled.connect(self.radio_Button)
        self.ui.radioButton_2.toggled.connect(self.radio_Button)
        self.ui.comboBox_3.activated.connect(self.Mode)
        self.ui.comboBox_5.activated.connect(self.output)
    def whichBtn(self,b):
        if b==self.ui.DisplayIm_1:
             logger.debug('Clicked on DisplayIm_1 Button')
             self.ImagButton1=1
             self.sizeFlag1=1
             self.ImagButton2=0
        elif b==self.ui.DisplayIm_2:
            logger.debug('Clicked on DisplayIm_2 Button')
            self.ImagButton1=0
            self.sizeFlag2=1
            self.ImagButton2=1
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def open_Image(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File' , '*.jpg')
        self.imgByte = cv.imread(fileName,cv.IMREAD_GRAYSCALE)
        self.imgByte = np.asarray( self.imgByte, dtype="int32"  )

        if self.ImagButton1==1:
            self.img1=ImageModel(self.imgByte)
            self.sizeImg1=self.imgByte
            self.img1.image_Display(self.ui.Image_1)
            if self.sizeFlag2==1:
                self.sizeImg1=self.img1.check_Size()
                self.sizeImg2=self.img2.check_Size()
                if self.sizeImg1.shape !=self.sizeImg2.shape:
                    logger.debug('Two Images have not the same size')
                    self.showMessageBox('Warning','Two Images have not the same size' )
                     
        elif self.ImagButton2==1:
            
            self.img2=ImageModel(self.imgByte)
            self.img2.image_Display(self.ui.Image_2)
            if self.sizeFlag1==1:
                self.sizeImg2=self.imgByte
                if self.sizeImg1.shape !=self.sizeImg2.shape:
                    logger.debug('Two Images have not the same size')
                    self.showMessageBox('Warning','Two Images have not the same size')
                    
    def which_Com_Box(self,com):
        if com==self.ui.comboBox_1:
            logger.debug('Choose from ComboBox Image1')
            self.comFlag1=1
            self.comFlag2=0
        elif com==self.ui.comboBox_2:
            logger.debug('Choose from ComboBox Image2')
            self.comFlag2=1  
            self.comFlag1=0  
    def display_DFT(self):
            if self.comFlag1==1:
                self.comImg=self.ui.comboBox_1.currentText()
                if self.comImg ==Modes.magnitudeFFT.value:
                    logger.debug('Chose FT Magnitude component Image1')
                    self.spectrum=self.img1.magnitude_Component()
                    logger.debug('returned magnitude_Component_Imag1')
                elif self.comImg ==Modes.phaseFFT.value:
                    logger.debug('Chose FT Phase component Image1')
                    self.spectrum=self.img1.phase_Component()
                    logger.debug('returned phase_Component_Imag1')
                elif self.comImg ==Modes.realFFT.value:
                    logger.debug('Chose FT Real component Image1')
                    self.spectrum=self.img1.real_Component()
                    logger.debug('returned real_Component_Imag1')
                elif self.comImg ==Modes.imaginaryFFT.value:
                    logger.debug('Chose FT Imaginary component Image1')
                    self.spectrum=self.img1.imaginary_Component()
                    logger.debug('returned imaginary_Component_Imag1')
                elif self.comImg ==Modes.inverseMagnitudeFFT.value:
                    logger.debug('Chose Inverse FT Magnitude component Image1')
                    self.spectrum=self.img1.invers_Magnitude_Component()
                    logger.debug('returned invers_Magnitude_Component_Imag1')
                elif self.comImg ==Modes.inversePhaseFFT.value:
                    logger.debug('Chose Inverse FT Phase component Image1')
                    self.spectrum=self.img1.invers_Phase_Component()
                    logger.debug('returned invers_Phase_Component_Imag1')
                elif self.comImg ==Modes.uniMagnitude.value:
                    logger.debug('Chose UniForm Magnitude component Image1')
                    self.spectrum=self.img1.uni_Magnitude_Component()
                    logger.debug('returned uni_Magnitude_Component_Imag1')
                elif self.comImg ==Modes.uniPhase.value:
                    logger.debug('Chose UniForm Phase component Image1')
                    self.spectrum=self.img1.uni_Phase_Component()
                    logger.debug('returned uni_Phase_Component_Imag1')
                    

                self.pix=ImageModel(self.spectrum)
                self.pix.image_Display(self.ui.Image_3)
                

            elif self.comFlag2 == 1:
                self.comImg=self.ui.comboBox_2.currentText()
                if self.comImg ==Modes.magnitudeFFT.value:
                    logger.debug('Chose FT Magnitude component Image2')
                    self.spectrum=self.img2.magnitude_Component()
                    logger.debug('returned magnitude_Component_Imag2')
                elif self.comImg ==Modes.phaseFFT.value:
                    logger.debug('Chose FT Phase component Image2')
                    self.spectrum=self.img2.phase_Component()
                    logger.debug('returned phase_Component_Imag2')
                elif self.comImg ==Modes.realFFT.value:
                    logger.debug('Chose FT Real component Image2')
                    self.spectrum=self.img2.real_Component()
                    logger.debug('returned real_Component_Imag2')
                elif self.comImg ==Modes.imaginaryFFT.value:
                    logger.debug('Chose FT Imaginary component Image2')
                    self.spectrum=self.img2.imaginary_Component()
                    logger.debug('returned imaginary_Component_Imag2')
                elif self.comImg ==Modes.inverseMagnitudeFFT.value:
                    logger.debug('Chose Inverse FT Magnitude component Image2')
                    self.spectrum=self.img2.invers_Magnitude_Component()
                    logger.debug('returned invers_Magnitude_Component_Imag2')
                elif self.comImg ==Modes.inversePhaseFFT.value:
                    logger.debug('Chose Inverse FT Phase component Image2')
                    self.spectrum=self.img2.invers_Phase_Component()
                    logger.debug('returned invers_Phase_Component_Imag2')
                elif self.comImg ==Modes.uniMagnitude.value:
                    logger.debug('Chose UniForm Magnitude component Image2')
                    self.spectrum=self.img2.uni_Magnitude_Component()
                    logger.debug('returned uni_Magnitude_Component_Imag2')
                elif self.comImg ==Modes.uniPhase.value:
                    logger.debug('Chose UniForm Phase component Image2')
                    self.spectrum=self.img2.uni_Phase_Component()
                    logger.debug('returned uni_Phase_Component_Imag2')

                self.pix=ImageModel(self.spectrum)
                self.pix.image_Display(self.ui.Image_4)
            logger.debug('Plot Component')
    def slider_Value(self,slider):
        if slider==self.ui.horizontalSlider:
            self.magnitudeOrRealRatio=float(self.ui.horizontalSlider.value()/100) 
            logger.debug('Slider_Value:{}'.format(self.magnitudeOrRealRatio))
        elif slider==self.ui.horizontalSlider_2:
            self.phaesOrImaginaryRatio=float(self.ui.horizontalSlider_2.value()/100) 
            logger.debug('Slider_Value:{}'.format(self.phaesOrImaginaryRatio))
    def radio_Button(self):
        if self.ui.radioButton.isChecked():
            self.radioFlag1=1
            self.radioFlag2=0
        elif self.ui.radioButton_2.isChecked():
            self.radioFlag1=0
            self.radioFlag2=1   
    def Mode(self):
        self.comImg=self.ui.comboBox_3.currentText()
        if self.radioFlag1==1:    
            if self.comImg==Modes.PhaseAndMagnitudeMode.value:
                logger.debug('Mix between Phase and Magnitde')
                self.mix=self.img1.mix(self.img2,self.magnitudeOrRealRatio,self.phaesOrImaginaryRatio,Modes.PhaseAndMagnitudeMode.value)               
            elif  self.comImg==Modes.realAndImaginaryMode.value:
                self.mix=self.img1.mix(self.img2,self.magnitudeOrRealRatio,self.phaesOrImaginaryRatio,Modes.realAndImaginaryMode.value)
                logger.debug('Mix between Imaginary and Real')
        elif self.radioFlag2==1:
            if self.comImg==Modes.PhaseAndMagnitudeMode.value:
                self.mix=self.img2.mix(self.img1,self.magnitudeOrRealRatio,self.phaesOrImaginaryRatio,Modes.PhaseAndMagnitudeMode.value)
                logger.debug('Mix between Phase and Magnitde')
            elif  self.comImg==Modes.realAndImaginaryMode.value:
                self.mix=self.img2.mix(self.img1,self.magnitudeOrRealRatio,self.phaesOrImaginaryRatio,Modes.realAndImaginaryMode.value)
                logger.debug('Mix between Phase and Magnitde')
    def output(self):
        self.comImg=self.ui.comboBox_5.currentText() 
        self.pix=ImageModel(self.mix)
        if self.comImg==Modes.outputDisplay1.value:
            self.pix.image_Display(self.ui.output_1) 
            
        elif self.comImg==Modes.outputDisplay2.value :
            self.pix.image_Display(self.ui.output_2)
        logger.debug('Display on Output')
   

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()