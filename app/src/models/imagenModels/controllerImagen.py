from app.src.models.imagenModels.createImagen import CrearImagenProductoIndumentariaInDb
from app.src.models.imagenModels.updateImagen import CambiarImagenInDb

class ControllerImagen():

    @staticmethod
    def crearInstanciaNuevaImagen():
        return CrearImagenProductoIndumentariaInDb
    
    def crearInstanciaCambiarImagen():
        return CambiarImagenInDb