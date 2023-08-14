import streamlit as st
from dotenv import load_dotenv
from docxtpl import DocxTemplate
import os

docx_tpl = DocxTemplate("./formato_demanda/formato_demanda.docx")

def main():
    load_dotenv()
    st.header("Crea tus documentos legales :notebook_with_decorative_cover:")

    documentos_legales = ["Demanda laboral", "Contrato de arrendamiento", "Contrato de compraventa", "Contrato de trabajo", 
                          "Contrato de prestación de servicios", "Contrato de sociedad"]
    
    documento_legal = st.selectbox("Selecciona el tipo de documento legal que deseas generar:", documentos_legales)

    def creacion_documento():
        nombre_informe = str(numero_radicado)
        context = {
            'nombre_demandante': nombre_demandante,
            'nombre_demandado': nombre_demandado,
            'cedula_demandante': cedula_demandante,
            'cedula_demandado': cedula_demandado,
            'ciudad': ciudad,
            'fecha': fecha,
            'nombre_abogado': nombre_abogado,
            'cedula_abogado': cedula_abogado
            }
        docx_tpl.render(context)
        docx_tpl.save(f'Informes/{nombre_informe}.docx')


    if documento_legal == "Demanda laboral":
        st.write("A continuación, ingresa la información necesaria para crear el documento")
        numero_radicado = st.text_input("Número de radicado:")
        nombre_demandante = st.text_input("Nombre del demandante:")
        nombre_demandado = st.text_input("Nombre del demandado:")
        cedula_demandante = st.text_input("Cédula del demandante:")
        cedula_demandado = st.text_input("Cédula del demandado:")
        ciudad = st.text_input("Ciudad:")
        fecha = st.date_input("Fecha:")
        nombre_abogado = st.text_input("Nombre del abogado:")
        cedula_abogado = st.text_input("Cédula del abogado:")
        if st.button("Generar documento"):
            creacion_documento()
            st.write("Documento generado")

    if documento_legal == "Contrato de compraventa":
        st.write("A continuación, ingresa la información necesaria para crear el documento")
        numero_radicado = st.text_input("Número de radicado:")
        nombre_demandante = st.text_input("Nombre del demandante:")
        nombre_demandado = st.text_input("Nombre del demandado:")
        cedula_demandante = st.text_input("Cédula del demandante:")
        cedula_demandado = st.text_input("Cédula del demandado:")
        if st.button("Generar documento"):
            creacion_documento()
            st.write("Documento generado")

    if documento_legal == "Contrato de trabajo":
        st.write("A continuación, ingresa la información necesaria para crear el documento")
        numero_radicado = st.text_input("Número de radicado:")
        nombre_demandante = st.text_input("Nombre del demandante:")
        nombre_demandado = st.text_input("Nombre del demandado:")
        cedula_demandante = st.text_input("Cédula del demandante:")
        cedula_demandado = st.text_input("Cédula del demandado:")
        if st.button("Generar documento"):
            creacion_documento()
            st.write("Documento generado")


if __name__ == "__main__":
    main()