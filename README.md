"# APIKaminari" 

"creo que llamo mucho a las mismas librerias, dsp tengo que fijarme que onda donde ponerlo una vez y de ahi empezar a invocar"


dia: 13-11-24:
    estoy haciendo un bardo, pero me esta saliendo todo, cosas a tener en cuenta:
        models: lo uso para mis clases "abs" lo pongo entre comillas pq solo lo puedo usar con pydantic
        scheme: lo uso para crear mis schemas de sqlAlchemis para poder hacer consultas

dia: 18/11/2024
    Termine el CRUD basico de usuario con autenticacion.
    Estructure mejor mi proyecto.
    El directorio scheme van a estar mis modelos de la base de datos para realizar querys con sqlAlchemy.
    El directorio models son para los modelos que voy a usar en mi API.
    Cree y movi el directorio "oathJWT" afuera de "app".
    Mejora a la hora de Codear, aplique las siguentes bases: Controller, Responsabilidad Unica, Alta cohesion, bajo acoplamiento.
    Mejora de estructura de los routes.
    Mejora de validaciones de funciones.
    Captura de errores.
    Defectos para mi de mi proyecto:
        Cantidad de Sessiones que abro para hacer querys.
        No hay implementado respuestas http, sino un true, 'hecho', False, "error", entro otros. Tengo que usar las respuestas http. Recordatorio para mi(usar status de fastapi).
        tengo que implementar la seguridad de visibilidad de mis atributos en las clases que haya creado, no les preste mucha atencion a eso, asi que es una posible mejora.
        Estare utilizando demasiado try, except.
        Acordarme de poner mis datos sensibles como variables de entorno.
        Tengo que implimentar mas el uso de autorizacion, pertenencia se cumple
