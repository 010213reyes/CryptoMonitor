# 🪙 Crypto Monitor

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Crypto Monitor** es una aplicación web ligera que muestra en tiempo real los datos de mercado de las principales criptomonedas (precio, variación 24h, capitalización, volumen, etc.). Está construida con **Python** y **Streamlit**, y obtiene los datos desde la API pública de **CoinGecko**.

El proyecto sigue los principios de **Arquitectura Limpia** (Clean Architecture) para garantizar modularidad, escalabilidad y mantenibilidad a largo plazo.

---

## 📋 Tabla de Contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Estrategia de Ramas (Git Flow)](#estrategia-de-ramas-git-flow)
- [Fases de Desarrollo](#fases-de-desarrollo)
- [Guía de Contribución](#guía-de-contribución)
- [Próximas Mejoras](#próximas-mejoras)
- [Licencia](#licencia)

---

## ✨ Características

- Visualización de datos en tiempo real para criptomonedas como BTC, ETH, ADA, SOL, etc.
- Indicadores clave: precio, cambio en 24h, capitalización de mercado, volumen y última actualización.
- Interfaz sencilla y responsive gracias a Streamlit.
- Caché integrado para evitar exceder los límites de la API.
- Código modular, tipado estáticamente y documentado.

---

## 🏛️ Arquitectura

La aplicación se divide en cuatro capas bien diferenciadas:

| Capa | Descripción |
|------|-------------|
| **Dominio** (`src/domain/`) | Entidades de negocio (`Crypto`, `MarketData`) e interfaces de repositorio (abstracciones). Independiente de cualquier framework. |
| **Aplicación** (`src/application/`) | Casos de uso que orquestan el flujo de datos (ej. `GetCryptoMarketDataUseCase`). |
| **Infraestructura** (`src/infrastructure/`) | Implementaciones concretas: cliente HTTP para CoinGecko, repositorio, configuración desde variables de entorno. |
| **Presentación** (`src/presentation/`) | Componentes de interfaz de usuario con Streamlit. Se comunica con la aplicación mediante inyección de dependencias. |

El flujo de datos es unidireccional:  
`Presentación → Aplicación → Infraestructura → API externa`

---

## 🛠️ Tecnologías

- **Python 3.10+**
- **Streamlit** – interfaz web rápida y sin necesidad de frontend tradicional.
- **Requests** – cliente HTTP para consumir la API de CoinGecko.
- **Pydantic** (o dataclasses) – validación y tipado de datos.
- **python-dotenv** – gestión de variables de entorno.
- **pytest** – pruebas unitarias y de integración.
- **Git** – control de versiones con flujo de trabajo basado en ramas.

---

## 📁 Estructura del Proyecto
crypto_monitor/
├── .env.example # Variables de entorno de ejemplo
├── .gitignore
├── README.md # Este archivo
├── requirements.txt # Dependencias del proyecto
├── app.py # Punto de entrada de Streamlit
├── src/
│ ├── domain/
│ │ ├── init.py
│ │ ├── entities.py # Entidades y value objects
│ │ └── interfaces.py # Abstracciones de repositorios
│ ├── application/
│ │ ├── init.py
│ │ └── use_cases.py # Casos de uso
│ ├── infrastructure/
│ │ ├── init.py
│ │ ├── config.py # Configuración (Settings)
│ │ ├── api_client.py # Cliente HTTP para CoinGecko
│ │ └── repositories.py # Implementación del repositorio
│ └── presentation/
│ ├── init.py
│ └── components.py # Componentes UI reutilizables
├── tests/ # Pruebas unitarias y de integración
│ ├── domain/
│ ├── application/
│ └── infrastructure/
└── docs/ # Documentación adicional
└── architecture.md


---

## 🚀 Instalación y Ejecución

### Requisitos previos

- Python 3.10 o superior
- Git

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/010213reyes/CryptoMonitor.git
   cd CryptoMonitor

   python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate


pip install -r requirements.txt



streamlit run app.py


 Estrategia de Ramas (Git Flow)
El proyecto sigue un flujo de trabajo basado en Git Flow simplificado:

Rama	Propósito
main	Código en producción. Solo se actualiza desde develop o mediante hotfix.
develop	Rama de integración donde se fusionan todas las características completadas.
feature/*	Desarrollo de nuevas funcionalidades. Se crea desde develop y se fusiona a develop.
release/*	Preparación de una nueva versión. Se crea desde develop y se fusiona a main y develop.
hotfix/*	Correcciones urgentes en producción. Se crea desde main y se fusiona a main y develop


El desarrollo se organiza en 6 fases, cada una con su propia rama feature/* que se integra a develop.

Fase	Descripción	Rama	Entregable
0	Configuración inicial (estructura, dependencias, Git)	feature/setup	Proyecto base listo.
1	Capa de Dominio (entidades e interfaces)	feature/domain	Módulo domain completo y testeado.
2	Capa de Infraestructura (cliente HTTP, repositorio)	feature/infrastructure	Cliente y repositorio funcionales.
3	Capa de Aplicación (casos de uso)	feature/application	Caso de uso implementado.
4	Capa de Presentación (interfaz Streamlit)	feature/presentation	Aplicación con UI funcional.
5	Integración y pulido (versión 1.0.0)	release/v1.0.0	Versión estable lista para producción.
6	Despliegue en producción	main	Aplicación disponible online.


main
  └── develop
        ├── feature/setup
        ├── feature/domain
        ├── feature/infrastructure
        ├── feature/application
        ├── feature/presentation
        └── release/v1.0.0  (se fusiona a main y develop)
