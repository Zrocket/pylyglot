import click

class jpeg:
    def __init__(self, fileName):
        with open(fileName, "rb") as data:
            jpg = bytearray(data.read())
            i = jpg.index(b"\xdb")
            self.jfif = jpg[0:i-1]
            self.imageData = jpg[i:]

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
        with open(fileName, "rb") as data:
            pdf = bytearray(data.read())
            i = 0
            while i <= len(pdf):
                if chr(pdf[i]) == 'o' and chr(pdf[i+1]) == 'b' and chr(pdf[i+2]) == 'j':
                    self.pdfHeader = pdf[:i-1]
                    self.pdfData = pdf[i:]
                    break
                i += 1

    @property
    def pdfHeader(self):
        return self.__pdfHeader

    @pdfHeader.setter
    def pdfHeader(self, pdfHeader):
        self.__pdfHeader = pdfHeader

    @property
    def pdfData(self):
        return self.__pdfData

    @pdfData.setter
    def pdfData(self, pdfData):
        self.__pdfData = pdfData

def jpgInPdf(jpg, pdf):
    output = bytearray()
    head = jpg.jfif
    tail = ""
    dummyObject = bytearray()
    head[2] = ord('\x00')
    head[3] = ord('\x00')
    output.extend(head)
    with open("out.pdf", "wb") as outputFile:
        pass

with open("vapor.jpg", "rb") as jpg:
    pdf = pdf("koc-do-you-want-vaporwave.pdf")
    jpg = jpeg("vapor.jpg") 
    jpgInPdf(jpg, pdf)

