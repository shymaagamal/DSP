import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1=cv.imread('test.jpg')
v=np.fft.fft2(img1)
n=np.abs(v) * 0.7
#o=np.fft.ifft2(n)
img2=cv.imread('tes.jpg')
b=np.fft.fft2(img2)
sw=np.angle(b) * 0.3
#p=np.fft.ifft2(sw)
dd=np.multiply(n,sw)

p=np.fft.ifft2(dd)
u=np.abs(p)


plt.imshow(u,cmap = 'gray')
plt.show()
'''
rows, cols = img.shape

m = cv.getOptimalDFTSize( rows )
n = cv.getOptimalDFTSize( cols )
padded = cv.copyMakeBorder(img, 0, m - rows, 0, n - cols, cv.BORDER_CONSTANT, value=[0, 0, 0])
    
planes = [np.float32(padded), np.zeros(padded.shape, np.float32)]
complexI = cv.merge(planes)         # Add to the expanded another plane with zeros
    
cv.dft(complexI, complexI)         # this way the result may fit in the source matrix
    
cv.split(complexI, planes)
magI = planes[1]
    
matOfOnes = np.ones(magI.shape, dtype=magI.dtype)
cv.add(matOfOnes, magI, magI) #  switch to logarithmic scale
cv.log(magI, magI)
    
magI_rows, magI_cols = magI.shape
    # crop the spectrum, if it has an odd number of rows or columns
magI = magI[0:(magI_rows & -2), 0:(magI_cols & -2)]
cx = int(magI_rows/2)
cy = int(magI_cols/2)
q0 = magI[0:cx, 0:cy]         # Top-Left - Create a ROI per quadrant
q1 = magI[cx:cx+cx, 0:cy]     # Top-Right
q2 = magI[0:cx, cy:cy+cy]     # Bottom-Left
q3 = magI[cx:cx+cx, cy:cy+cy] # Bottom-Right
tmp = np.copy(q0)               # swap quadrants (Top-Left with Bottom-Right)
magI[0:cx, 0:cy] = q3
magI[cx:cx + cx, cy:cy + cy] = tmp
tmp = np.copy(q1)               # swap quadrant (Top-Right with Bottom-Left)
magI[cx:cx + cx, 0:cy] = q2
magI[0:cx, cy:cy + cy] = tmp
    
cv.normalize(magI, magI, 0, 1, cv.NORM_MINMAX) # Transform the matrix with float values into a
    
cv.imshow("Input Image"       , img   )    # Show the result
cv.imshow("spectrum magnitude", magI)
cv.waitKey()
'''
'''
d = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)

dft_shift  = np.fft.fftshift(d)

ccrow,cccol =cv.getOptimalDFTSize(rows) , cv.getOptimalDFTSize(rows)
print("{} {}".format(ccrow,cccol))
crow,ccol = rows/2 , cols/2
print("{} {}".format(crow,ccol))
'''
# create a mask first, center square is 1, remaining all zeros
"""mask = np.zeros((rows,cols,2),np.uint8)
mask[int(crow-30):int(crow+30), int(ccol-30):int(ccol+30)] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.phase(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
"""
"""

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
"""
'''
self.data = np.array(self.data).reshape(2048,2048).astype(np.int32)
qimage = QtGui.QImage(self.data, self.data.shape[0],self.data.shape[1],QtGui.QImage.Format_RGB32)
img = PrintImage(QPixmap(qimage))
'''


'''






            self.rows, self.cols = self.img.shape
            self.m = cv.getOptimalDFTSize( self.rows )
            self.n = cv.getOptimalDFTSize( self.cols )
            self.padded = cv.copyMakeBorder(self.img, 0, self.m - self.rows, 0, self.n - self.cols, cv.BORDER_CONSTANT, value=[0, 0, 0])
    
            self.planes = [np.float32(self.padded), np.zeros(self.padded.shape, np.float32)]
            self.complexI = cv.merge(self.planes)         # Add to the expanded another plane with zeros
            cv.dft(self.complexI, self.complexI)         # this way the result may fit in the source matrix
            cv.split(self.complexI, self.planes)                   # planes[0] = Re(DFT(I), planes[1] = Im(DFT(I))
            cv.magnitude(self.planes[0], self.planes[1], self.planes[0])# planes[0] = magnitude
            self.magI = self.planes[1]
            
            self.matOfOnes = np.ones(self.magI.shape, dtype=self.magI.dtype)
            cv.add(self.matOfOnes, self.magI, self.magI) #  switch to logarithmic scale
            cv.log(self.magI, self.magI)
            
            self.magI_rows, self.magI_cols = self.magI.shape
            # crop the spectrum, if it has an odd number of rows or columns
            self.magI = self.magI[0:(self.magI_rows & -2), 0:(self.magI_cols & -2)]
            self.cx = int(self.check_SizemagI_rows/2)
            self.cy = int(self.check_SizemagI_cols/2)
            self.q0 = self.ccolmagI[0:cx, 0:cy]         # Top-Left - Create a ROI per quadrant
            self.q1 = self.magI[self.cx:self.cx+self.cx, 0:self.cy]     # Top-Right
            self.q2 = self.magI[0:self.cx, self.cy:self.cy+self.cy]     # Bottom-Left
            self.q3 = self.magI[self.cx:self.cx+self.cx, self.cy:self.cy+self.cy] # Bottom-Right
            self.tmp = np.copy(self.q0)               # swap quadrants (Top-Left with Bottom-Right)
            self.magI[0:self.cx, 0:self.cy] = self.q3
            self.magI[self.cx:self.cx + self.cx, self.cy:self.cy + self.cy] = self.tmp
            self.tmp = np.copy(self.q1)               # swap quadrant (Top-Right with Bottom-Left)
            self.magI[self.cx:self.cx + self.cx, 0:self.cy] = self.q2
            self.magI[0:self.cx, self.cy:self.cy + self.cy] = self.tmp
            
            cv.normalize(self.magI, self.magI, 0, 1, cv.NORM_MINMAX) # Transform the matrix with float values into a
            
            cv.imshow("spectrum magnitude", self.magI)
            cv.waitKey()
'''




if self.ui.radioButton.isChecked():
            self.hh=  (self.img1.magnitude * 0.5+self.img2.magnitude * 0.5) * np.exp(0.5* self.img1.phase +0.5 * self.img2.phase)
            #self.kkkl=self.img2.phase * 0.7
            self.j=np.add(self.img1.magnitude * 0.3,self.img2.magnitude * 0.7)
            self.g=np.add(0.7* self.img1.phase ,0.3 * self.img2.phase)
            self.combined = np.multiply(self.j ,np.exp(self.g))
            
            self.fff=np.fft.ifft2(self.combined)
            #self.bbb=np.fft.ifftshift(self.fff)
 
            self.imgCombined = np.real(self.fff)
            cv.imshow("hhh",self.imgCombined )
            cv.waitKey()
            # image2 = Image.fromarray(data)
            #self.ee=np.add(self.hh,self.jj)
            #self.dd=np.array(self.ee).reshape(-1,2).astype(np.int32)
           #self.r=ImageModel(self.img1.magnitude)
            #self.gg=self.r.mix(self.img2.phase,0.3,0.7,Modes.magnitudeAndPhase)
            #self.bb=ImageModel(self.gg)
            #self.bb.image_Display(self.ui.output_1)


                
