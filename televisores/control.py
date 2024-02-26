class Control:
    def __init__(self,tv):
        self.tv=tv

    def __init__(self):
        self.tv=None

    def turnOn(self):
        self.tv.estado=True

    def turnOff(self):
        self.tv.estado=False

    def canalUp(self):
        if (self.tv.canal != 120 and self.tv.estado):
            self.tv.canal += 1

    def canalDown(self):
        if (self.tv.canal != 1 and self.tv.estado):
            self.tv.canal -= 1

    def volumenUp(self):
        if (self.tv.volumen != 7 and self.tv.estado):
            self.tv.volumen += 1

    def volumenDown(self):
        if (self.tv.volumen != 0 and self.tv.estado):
            self.tv.volumen -= 1
    
    def setCanal(self, canal):
        if (1<=canal<=120 and self.tv.estado):
            self.tv.canal = canal

    def setVolumen(self, volumen):
        if (0<=volumen<=7 and self.tv.estado):
            self.tv.volumen=volumen
    
    def enlazar(self, tv):
        self.tv=tv
        tv.control=self
    
    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv=tv