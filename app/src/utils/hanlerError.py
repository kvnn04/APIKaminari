from app.config.configModuloLogging import logging

logger = logging.getLogger(__name__)

def logException(exception: Exception):
    """Función que recibe una excepción y la guarda en el archivo de log."""
    logger.error("Excepción capturada: %s", exception, exc_info=True)