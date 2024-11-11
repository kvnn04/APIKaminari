from app.config.configModuloLogging import logging

# Obtener logger
logger = logging.getLogger(__name__)

# # Ejemplo de uso de logger
# logger.info("Este es un mensaje informativo.")
# logger.error("Este es un mensaje de error.")

def logException(exception: Exception):
    """Función que recibe una excepción y la guarda en el archivo de log."""
    logger.error("Excepción capturada: %s", exception, exc_info=True)