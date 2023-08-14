import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Gestión documental de casos de derecho con IA",
    page_icon=":books:",
    layout="wide"
)

# Estilos de CSS personalizados
st.markdown(
    """
    <style>
    body {
        background-color: #f4f7f9;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .description {
        font-size: 1.2rem;
        line-height: 1.6;
    }
    .sidebar {
        background-color: #f5f7fa;
        padding: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Diseño del encabezado
st.markdown('<h1 class="title">JurisBot 🤖</h1>', unsafe_allow_html=True)
st.markdown("---")

# Descripción de la aplicación
st.markdown('<p class="description">Bienvenidos a la aplicación de gestión documental de casos de derecho con IA.</p>', unsafe_allow_html=True)
st.write(
    """
    Esta aplicación permite realizar las siguientes tareas:
    - Realizar cualquier pregunta sobre algún dato en el documento.
    - Identificar nombres de lugares en el documento con descripciones.
    - Identificar montos de dinero en el documento con descripciones.
    - Identificar leyes y artículos en el documento con descripciones.
    - Identificar nombres de personas en el documento con descripciones.
    - Realizar preguntas sobre leyes o artículos de la Constitución Colombiana:
      Código penal, Código civil, Código comercial.
    """
)
st.markdown("---")

# Menú lateral
st.sidebar.markdown('<h2 class="sidebar">Menú</h2>', unsafe_allow_html=True)
st.sidebar.info("Selecciona una opción de la lista arriba.")

# Fin del código



