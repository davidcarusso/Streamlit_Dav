import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime

def codigo_uno():
    st.write("# st.button")
    st.write("### Hola mundo!!!")

    if st.button("Di Hola"):
        st.write("¿Por qué hola?")
    else: 
        st.write("Chau")


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
    st.write("# Data Frame en st.write()")
    df = pd.DataFrame({
    "Primera Columna": [1,2,3,4],
    "Segunda Columna": [10,20,30,40]})
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')


def codigo_cinco():
    st.write("# Mostrar Grafico")

    col1, col2 = st.columns(2, border=True)
    df = pd.DataFrame(
        np.random.rand(200,3),
        columns=["a", "b", "c"]
    )
    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )

    with col1:
        st.write("Data Frame")
        st.write(df.head())
    with col2:
        st.write("Grafico")
        st.write(c)
        c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )


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

    tab1, tab2, tab3, codigo = st.tabs(
        ["Select Box", "Multi Select", "Check Box", "Mostrar Codigo"])

    with tab1:
        st.write("# st.selectbox()")
        color = st.selectbox("Cual es tu color favorito?", ["Rojo", "Azul", "Amarillo"])
        st.write(f"### Tu color favorito es el {color}")

    with tab2:
        st.write("# st.multiselect()")
        colores = st.multiselect("Cuales son tus colores favoritos?", ["Rojo", "Amarillo", "Azul", "Verde", "Naranja", "Violeta"])
        st.write("### Tu seleccionaste", colores)

    with tab3:
        st.write("# st.checkbox()")
        st.write("Que quieres ordenar?")

        # hay que seleccionar cada uno como una variable
        # genera un valor booleano de cada variable
        helado = st.checkbox("Helado", help="Helado de chocolate, vainilla o frutilla.")
        cafe = st.checkbox("Cafe")
        coca = st.checkbox("Coca-Cola")
        
        if helado:
            st.write("Great! Here's some more 🍦")
        if cafe:
            st.write("Okay, here's some coffee ☕")
        if coca:
            st.write("Here you go 🥤")
    
    with codigo:
        st.write("# Codigo usado")
        st.code("""
    tab1, tab2, tab3, codigo = st.tabs(
        ["Select Box", "Multi Select", "Check Box", "Codigo"])

    with tab1:
        st.write("# st.selectbox()")
        color = st.selectbox("Cual es tu color favorito?", ["Rojo", "Azul", "Amarillo"])
        st.write(f"### Tu color favorito es el {color}")

    with tab2:
        st.write("# st.multiselect()")
        colores = st.multiselect("Cuales son tus colores favoritos?", 
                ["Rojo", "Amarillo", "Azul", "Verde", "Naranja", "Violeta"])
        st.write("### Tu seleccionaste", colores)

    with tab3:
        st.write("# st.checkbox()")
        st.write("Que quieres ordenar?")

        # hay que seleccionar cada uno como una variable
        # genera un valor booleano de cada variable
        helado = st.checkbox("Helado", 
                help="Helado de chocolate, vainilla o frutilla.")
        cafe = st.checkbox("Cafe")
        coca = st.checkbox("Coca-Cola")
        
        if helado:
            st.write("Great! Here's some more 🍦")
        if cafe:
            st.write("Okay, here's some coffee ☕")
        if coca:
            st.write("Here you go 🥤")
""", language="python")

    

####################### Codigo de funcionalidad ###############################


def codigo_principal():
    
    custom = st.selectbox("Elegi la opcion: ", 
                          ["Boton","Write", "Data Frame", 
                           "Show graph", "Slider", "Grafico Lineal", "Select Box"])
    match custom:
        case "Boton":
            codigo_uno()
        case "Write":
            codigo_tres()
        case "Data Frame":
            codigo_cuatro()
        case "Show graph":
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