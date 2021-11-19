from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))
        
        for i in range(self.H):
            for c in range(self.W):
                if self.pixels[i][c]>=S:
                    im_bin.pixels[i][c] = 255
                else :
                    im_bin.pixels[i][c]=0
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        l_min = self.H -1
        c_min = self.W -1
        l_max = 0
        c_max = 0

        
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c] == 0:
                    if l < l_min:
                        l_min = l
                    if l > l_max:
                        l_max = l
                    if c <= c_min:
                        c_min = c
                    if c >= c_max :
                        c_max = c
                
        im_bin = Image()
        im_bin.set_pixels(self.pixels[l_min:l_max+1,c_min:c_max+1])
        return im_bin
                

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):       

        pixels_resized = resize(self.pixels,(new_H,new_W),0)
        pixels_resized = np.uint8(pixels_resized*255)
        im_resize = Image()
        im_resize.set_pixels(pixels_resized)
        return im_resize
        return self
    
    
    #        res_im = Image()
#        n = resize(self.pixels,(new_H,new_W),0)
#        res_im.set_pixels(np.uint8(n*255))
#        return res_im



    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        nombre_similitude = 0
        for x in range(self.H):
            for y in range(self.W):
                if self.pixels[x][y] == im.pixels[x][y]:
                    nombre_similitude += 1
            taux = nombre_similitude/(self.H * self.W)
            return taux
        
        
        
        
#        pixels = 0
#        im_test = self.resize_im(100,100)
#        im_change = im.resize_im(100,100)
#        for i in range(100):
#            for c in range(100):
#                if im_test.pixels[i][c] == im_change.pixels[i][c]:
#                    pixels = pixels + 1 
#        return pixels/100
#    
liste_images =['test1.JPG','test2.JPG','test3.JPG','test4.JPG','test5.JPG','test6.JPG','test7.JPG','test8.JPG','test9.JPG']
 
    
        

