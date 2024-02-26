class TV:
    numTV=0
    def __init__(self, marca, estado):
        self._marca=marca
        self.estado=estado
        self.canal=1
        self.volumen=1
        self._precio=500
        self.control=None
        TV.numTV += 1

    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self.canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self.volumen
    
    def getControl(self):
        return self.control
    
    def getNumTV(self):
        return TV.numTV

    def setMarca(self, marca):
        self._marca=marca

    def setCanal(self, canal):
        if (1<=canal<=120 and self.estado):
            self.canal=canal

    def setPrecio(self, precio):
        self._precio=precio

    def setVolumen(self, volumen):
        if (0<=volumen<=7 and self.estado):
            self.volumen=volumen

    def setControl(self, control):
        self.control=control

    @classmethod
    def setNumTV(cls, numTv):
        cls.numTV=numTv
    
    def turnOn(self):
        self.estado=True
    
    def turnOff(self):
        self.estado=False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if (self.canal != 120 and self.estado):
            self.canal += 1

    def canalDown(self):
        if (self.canal != 1 and self.estado):
            self.canal -= 1

    def volumenUp(self):
        if (self.volumen != 7 and self.estado):
            self.volumen += 1

    def volumenDown(self):
        if (self.volumen != 0 and self.estado):
            self.volumen -= 1
