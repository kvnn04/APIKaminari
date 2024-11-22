from app.src.models.productoModels.readProductoModels import ReadProductoIndumentaria, ReadIfProductoIndumentaria,ReadProductoIndumentariaIfExiste
from app.src.models.productoModels.createProducto import CrearProductoIndumentariaInDb, CreateProductoIndumentariaVarianteInDb
from app.src.models.productoModels.modifyProducto import ModifiStockProductoIndumentariaVarianteInDb
from app.src.models.productoModels.deleteProducto import EliminarProductoIndumentariaInDb
from abc import ABC, abstractmethod

class ProductoController(ABC):

    @abstractmethod
    def crearGetProducto():
        pass
    
    @abstractmethod
    def crearProductoInDb():
        pass
    
    @abstractmethod
    def crearProductoVarianteInDb():
        pass 
    # @staticmethod
    # @abstractmethod
    # def crearIfProductoIndumentaria():
    #     pass
    
    @abstractmethod
    def crearModifyStockProductoIndumentaria():
        pass
    
    @abstractmethod
    def crearEliminarProductoIndumentaria():
        pass



    
class ProductHandler(ProductoController):

    def crearGetProducto(self):
        return ReadProductoIndumentaria()
    
    def crearProductoInDb(self):
        return CrearProductoIndumentariaInDb()
    
    def crearProductoVarianteInDb(self) -> CreateProductoIndumentariaVarianteInDb:
        return CreateProductoIndumentariaVarianteInDb()
    
    # def crearIfProductoIndumentaria(self):
    #     return ReadIfProductoIndumentaria()
    
    def crearModifyStockProductoIndumentaria(self):
        return ModifiStockProductoIndumentariaVarianteInDb()
    
    def crearEliminarProductoIndumentaria(self):
        return EliminarProductoIndumentariaInDb()