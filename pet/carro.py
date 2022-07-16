class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            self.session['carro'] = {}
            self.carro = self.session['carro']
        else:
            self.carro = carro

    def agregar(self, accesorio):
        id =str(accesorio.id)
        if id not in self.carro.keys():
            self.carro[id]={
                'accesorio_id': accesorio.id,
                'nombre': accesorio.nombre,
                'precio': accesorio.precio,
                'descripcion': accesorio.descripcion,
                'acumulado': accesorio.precio,
                
                'cantidad': 1,
            }

        else:
            self.carro[id]['cantidad'] += 1
            self.carro[id]['acumulado'] += accesorio.precio
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def eliminar(self, accesorio):
        id = str(accesorio.id)
        if id in self.carro:
            del self.carro[id]
            self.guardar_carro()

    def restar(self, accesorio):
        id = str(accesorio.id)
        if id in self.carro.keys():
            self.carro[id]['cantidad'] -= 1
            self.carro[id]['acumulado'] -= accesorio.precio
            if self.carro[id]['cantidad'] <= 0: self.eliminar(accesorio)
            self.guardar_carro()
    
    def limpiar(self):
        self.session['carro'] = {}
        self.session.modified = True