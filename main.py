import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime

def codigo_uno():
    st.write("# Hola mundo!!!")
    st.write("# st.button")

def codigo_dos():
    st.code("""
    st.write("# st.button")

    if st.button("Say hello"):
        st.write("Why hello there")
    else: 
        st.write("Goodbye")
    """, language="python")

    if st.button("Say hello"):
        st.write("Why hello there")
    else: 
        st.write("Goodbye")

def codigo_tres():
    st.write(f"""
            # st.write
            ## Display text 
            Hello, World!!
    """)
    st.write("# Display numbers")
    st.write(123)

    # Ejemplo 3
    st.write("# Display DataFrame")
    df = pd.DataFrame({
        "Primera Columna": [1,2,3,4],
        "Segunda Columna": [10,20,30,40]
    })
    st.write(df)


def codigo_cuatro():
    df = pd.DataFrame({
    "Primera Columna": [1,2,3,4],
    "Segunda Columna": [10,20,30,40]})
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

def codigo_cinco():
    st.write("# Display chart")
    df = pd.DataFrame(
        np.random.rand(200,3),
        columns=["a", "b", "c"]
    )
    st.write(df.head())
    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )
    st.write(c)


def codigo_seis():
    st.write("# st.slider")
    st.write("Slider")

    edad = st.slider("Cuantos años tienes ?",0, 130, 31)
    st.write(f"Yo tengo {edad} años de edad.")

    st.write("## Range slider:")
    valores = st.slider("Seleccione un rango de valor", 0.0, 100.0, (25.0, 75.0), step=0.1)
    st.write("Valores: ", valores)

    st.write("## Rango de horario:")
    agenda = st.slider("Agendar una reunion:", 
                       value=(time(11,30), time(12,45)))
    st.write(f"Estas programado para el horario de: {agenda}.")

    st.write("## Datetime slider")
    fecha = st.slider("Cuando empiezas?", 
                      value=datetime(2024,12,28,10, 31),
                       format="DD/MM/YY - hh:mm" )
    st.write(f"Comienzas el: {fecha}")


def codigo_siete():
    st.write("# Grafico de Linea")
    df = pd.DataFrame(
        np.random.randn(20,3),  # 20 filas, 3 columnas. datos aletorios
        columns=["A", "B", "C"]        
        )
    
    col1, col2 = st.columns(2, border=True)  # inicio las columnas | El atributo border = True (genera un borde y limita el tamño)

    with col1:
        st.write("## Data Frame")
        st.write(df.head()) # data frame aletorio, primeras 5 filas
    with col2:
        st.write("## Grafico de Linea ")
        st.line_chart(df)   # genera un grafico de linea con los datos generados en el df

    if st.button("Mostrar el codigo"):
        st.code("""
    
    # inicio las columnas 
    # El atributo border = True (genera un borde y limita el tamño)
    col1, col2 = st.columns(2, border=True)  
                
    with col1: # Columnas N° 1 
        st.write("## Data Frame")
        st.write(df.head()) # data frame aletorio, primeras 5 filas
    
    with col2: # Columna N° 2
        st.write("## Grafico de Linea ")
        st.line_chart(df)   # Grafico de linea con el df
        """, language="python")

    
def codigo_ocho():

    tab1, tab2 = st.tabs(["Select Box", "Multi Select"])

    with tab1:
        st.write("# st.selectbox")
        color = st.selectbox("Cual es tu color favorito?", ["Rojo", "Azul", "Amarillo"])
        st.write(f"### Tu color favorito es el {color}")

    with tab2:
        st.write("# st.multiselect")
        colores = st.multiselect("Cuales son tus colores favoritos?", ["Rojo", "Amarillo", "Azul", "Verde", "Naranja", "Violeta"])
        st.write("### Tu seleccionaste", colores)


    if st.button("Mostrar Codigo"):
        st.code("""
    
    # Genea el separador, se debe dar el nombre en formato str
    tab1, tab2 = st.tabs(["Select Box", "Multi Select"])    

    with tab1:
        st.write("# st.selectbox")
        color = st.selectbox("Cual es tu color favorito?", ["Rojo", "Azul", "Amarillo"])
        st.write(f"### Tu color favorito es el {color}")

    with tab2:
        st.write("# st.multiselect")
        colores = st.multiselect("Cuales son tus colores favoritos?", ["Rojo", "Amarillo", "Azul", "Verde", "Naranja", "Violeta"])
        st.write("### Tu seleccionaste", colores)

""", language="python")
    

####################### Codigo de funcionalidad ###############################


def codigo_principal():
    
    custom = st.selectbox("Elegi la opcion: ", 
                          ["Caso 1", "Caso 2", "Caso 3", "Caso 4", 
                           "Caso 5", "Slider", "Grafico Lineal", "Select Box"])
    match custom:
        case "Caso 1":
            codigo_uno()
        case "Caso 2":
            codigo_dos()
        case "Caso 3":
            codigo_tres()
        case "Caso 4":
            codigo_cuatro()
        case "Caso 5":
            codigo_cinco()
        case "Slider":
            codigo_seis()
        case "Grafico Lineal":
            codigo_siete()
        case "Select Box":
            codigo_ocho() 



def main():
    codigo_principal()



if __name__ == "__main__":
    main()