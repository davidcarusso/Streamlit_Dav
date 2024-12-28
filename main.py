import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

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


def codigo_principal():
    
    custom = st.selectbox("Elegi la opcion: ", ["Caso 1", "Caso 2", "Caso 3", "Caso 4", "Caso 5"])
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


def main():
    codigo_principal()



if __name__ == "__main__":
    main()