# Modulos-

## Introducción teórica a los módulos en Python

En Python, un **módulo** es un archivo que contiene definiciones y código en Python, como funciones, clases y variables, que pueden ser reutilizados en otros programas. Los módulos permiten organizar el código en partes más pequeñas y manejables, facilitando la reutilización y el mantenimiento.

### ¿Por qué usar módulos?
- Permiten dividir programas grandes en archivos más pequeños y organizados.
- Fomentan la reutilización de código.
- Facilitan la colaboración en proyectos.
- Ayudan a evitar la duplicidad de código.

### Tipos de módulos
1. **Módulos estándar**: Vienen incluidos con Python, como `math`, `os`, `sys`, entre otros.
2. **Módulos de terceros**: Desarrollados por la comunidad y disponibles a través de gestores de paquetes como `pip`.
3. **Módulos propios**: Creados por el usuario para organizar su propio código.

### ¿Cómo importar un módulo?
Para usar un módulo, se emplea la instrucción `import`:
```python
import math
print(math.sqrt(16))  # Imprime 4.0
```

También se puede importar solo una parte específica:
```python
from math import sqrt
print(sqrt(16))  # Imprime 4.0
```

### Conclusión
El uso de módulos es fundamental para escribir código limpio, eficiente y escalable en Python. Aprender a crear, importar y utilizar módulos es una habilidad esencial para cualquier programador en este lenguaje.

---

## Teoría de Streamlit

**Streamlit** es una biblioteca de Python diseñada para crear aplicaciones web interactivas de manera sencilla y rápida, especialmente orientadas a la visualización de datos y prototipos de ciencia de datos. Permite transformar scripts de Python en interfaces gráficas sin necesidad de conocimientos avanzados de desarrollo web.

### Características principales:
- Sintaxis simple y directa.
- Actualización automática de la interfaz al modificar el código.
- Integración con bibliotecas populares como Pandas, Matplotlib y Plotly.
- Ideal para dashboards, visualizaciones y prototipos.

### Ejemplo básico:
```python
import streamlit as st
st.title('Hola Streamlit')
st.write('Esta es una app web sencilla en Python.')
```

## Teoría de Sympy

**Sympy** es una biblioteca de Python para matemáticas simbólicas. Permite realizar cálculos algebraicos, simplificaciones, derivadas, integrales, ecuaciones y más, todo de forma simbólica (no numérica). Es útil para estudiantes, docentes e investigadores que requieren manipulación algebraica en sus programas.

### Características principales:
- Manipulación simbólica de expresiones matemáticas.
- Resolución de ecuaciones algebraicas y diferenciales.
- Cálculo de límites, derivadas e integrales.
- Generación de expresiones matemáticas en formato LaTeX.

### Ejemplo básico:
```python
from sympy import symbols, solve
x = symbols('x')
ecuacion = x**2 - 4
soluciones = solve(ecuacion, x)
print(soluciones)  # Imprime [-2, 2]
```
