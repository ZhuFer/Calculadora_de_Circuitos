# ⚡ Calculadora de Circuitos (Ri hasta Rj)

[![GitHub Repository](https://img.shields.io/badge/Repositorio-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ZhuFer/Calculadora_de_Circuitos)

Software interactivo desarrollado en Python para el análisis de circuitos en serie y paralelo con soporte para 4 resistores y selección de rango dinámico.

---

## 🛠️ Guía de Instalación para el Ayudante (PowerShell)

Siga estos pasos exactos para configurar el entorno y ejecutar la aplicación en Windows:

### 1. Clonar el repositorio
git clone https://github.com/ZhuFer/Calculadora_de_Circuitos.git
cd Calculadora_de_Circuitos

### 2. Configurar el Entorno Virtual
Es necesario activar el entorno para asegurar que las librerías no entren en conflicto con el sistema.

# Crear el entorno
python -m venv .venv

# IMPORTANTE: Si PowerShell da error de permisos, ejecutar primero:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activar el entorno
.\.venv\Scripts\Activate.ps1

### 3. Instalar Dependencias
pip install customtkinter

### 4. Ejecutar Aplicación
python main.py

---

## 📋 Funcionalidades Técnicas
- **Cálculo de Rango:** Permite seleccionar desde qué resistencia (Ri) hasta cuál (Rj) realizar el análisis.
- **Ley de Ohm y Kirchhoff:** Implementación precisa para circuitos Serie y Paralelo.
- **Notación de Ingeniería:** Los resultados se muestran con prefijos métricos (m, u, k, M) automáticamente.
- **Arquitectura Modular:** Lógica matemática desacoplada de la interfaz gráfica.
