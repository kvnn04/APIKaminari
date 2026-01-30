# 🌩️ API Kaminari 

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)

**API Kaminari** es un sistema de gestión para e-commerce de indumentaria, enfocado en la escalabilidad, la seguridad y la aplicación de patrones de diseño.

> 📖 **[Ver Documentación Detallada en Google Docs](https://docs.google.com/document/d/1g31WMuzXVAOoPIyzQsrFJ4_TyTjMczjX3QBy0hOXexs/edit?usp=sharing)** > *Incluye bitácora de desarrollo, componentes y análisis de patrones SOLID/GRASP.*

## 🚀 Evolución y Arquitectura
Este proyecto nació como un desafío personal de aprendizaje y evolucionó de un script monolítico hacia una arquitectura limpia basada en:
- **Patrones SOLID & GRASP:** Alta cohesión y bajo acoplamiento.
- **Arquitectura por Capas:** Separación clara entre Rutas, Controladores (Handlers) y Modelos (ORM/Schemas).
- **RESTful API:** Endpoints normalizados siguiendo estándares de la industria.



## 🛠️ Tecnologías utilizadas
- **FastAPI:** Framework principal para la creación de endpoints.
- **SQLAlchemy:** ORM para la interacción con la base de datos SQL.
- **JWT (JSON Web Tokens):** Gestión de autenticación y autorización.
- **Pydantic:** Validación de datos y tipado estricto.
- **Python-Dotenv:** Manejo de variables de entorno para datos sensibles.

## 🔐 Seguridad
- Implementación de **OAuth2** con flujo de tokens JWT.
- Control de acceso (RBAC): Ciertas acciones de modificación y borrado están reservadas exclusivamente para usuarios con permisos de administrador.

## 📂 Estructura del Proyecto
```text
app/
├── src/
│   ├── models/       # Modelos de Pydantic para la API
│   ├── schemes/      # Schemas de SQLAlchemy (Base de Datos)
│   ├── routes/       # Definición de Endpoints (Users, Products, etc.)
│   └── handlers/     # Lógica de negocio y controladores
├── oathJWT/          # Lógica de seguridad y tokens
├── log/              # Logs del sistema
└── config/           # Configuraciones de DB y entorno

