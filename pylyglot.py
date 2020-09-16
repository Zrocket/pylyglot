import click

JFIF = bytearray(b'0xff0xd80x00x00') 

class jpeg:
    def __init__(self, fileName):
        with open(fileName, "rb") as data:
            jpg = bytearray(data.read())
            i = jpg.index(b"\xdb")
            self.jfif = jpg[0:i-1]
            print(self.jfif)
            self.imageData = jpg[i:]
            print(self.imageData)

    @property
    def jfif(self):
        return self.__jfif

    @jfif.setter
    def jfif(self, jfif):
        self.__jfif = jfif

    @property
    def imageData(self):
        return self.__imageData

    @imageData.setter
    def imageData(self, imageData):
        self.__imageData = imageData

class jfif:
    def __init__(self, data):
        pass

class pdf:
    def __init__(self, fileName):
        with open(fileName) as data:
            pass

    @property
    def pdfData(self):
        return self.__pdfData

    @pdfData.setter
    def pdfData(self, imageProperty):
        self.__pdfData = pdfData

with open("vapor.jpg", "rb") as jpg:
    with open("koc-do-you-want-vaporwave.pdf", "rb") as pdf:
        pdf = bytearray(pdf.read())
        jpg = jpeg("vapor.jpg") 
        print(type(jpg))

with open("out.pdf", "wb") as o:
    pass
