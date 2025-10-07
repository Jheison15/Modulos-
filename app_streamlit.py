import streamlit as st
from sympy import symbols, solve, diff, integrate, latex

st.title("Calculadora simbólica con Sympy")

st.write("Esta aplicación permite realizar operaciones simbólicas básicas usando Sympy.")

# Selección de operación
operacion = st.selectbox("Selecciona la operación:", ["Resolver ecuación", "Derivar", "Integrar"])

# Entrada de expresión
expresion = st.text_input("Introduce la expresión (usa 'x' como variable):", value="x**2 - 4")

x = symbols('x')

if operacion == "Resolver ecuación":
    st.subheader("Solución de ecuación:")
    try:
        soluciones = solve(expresion, x)
        st.write(f"Soluciones: {soluciones}")
        st.latex(latex(soluciones))
    except Exception as e:
        st.error(f"Error: {e}")

elif operacion == "Derivar":
    st.subheader("Derivada de la expresión:")
    try:
        derivada = diff(expresion, x)
        st.write(f"Derivada: {derivada}")
        st.latex(latex(derivada))
    except Exception as e:
        st.error(f"Error: {e}")

elif operacion == "Integrar":
    st.subheader("Integral de la expresión:")
    try:
        integral = integrate(expresion, x)
        st.write(f"Integral: {integral}")
        st.latex(latex(integral))
    except Exception as e:
        st.error(f"Error: {e}")
