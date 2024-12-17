import streamlit as st 

st.title("Mi primera aplicacion con Streamlit")

saludar=st.button("Saludar")

if saludar:
    st.write('Hola Como estas')
else:
    st.write('No me saludo')


medio=st.selectbox('Que medios usas para conectarte??',('Email','Celular','Llamada'))

st.write('Se ha elegido:', medio)


medio_seleccionado=st.multiselect('Que medios usas para conectarte??',('Email','Celular','Llamada'))

st.write('Se ha elegido:', medio_seleccionado)

autor=st.sidebar.text_input("Nombre de Autor",'Carlos Meza')
st.sidebar.write("Tu autor preferido es:", autor)

fecha_nacimiento=st.sidebar.date_input("¿Cual es la fecha de tu cumpleaños?")

st.sidebar.write("La fecha seleccionada es ", fecha_nacimiento)

acuerdo=st.checkbox('Estoy de Acuerdo??')
if acuerdo:
    st.write('Ud. Esta de Acuerdo')
else:
    st.write("Ud no esta de acuerdo")


edad=st.slider('Cuantos Años tienes?', 0, 70, 10)

st.write('Tengo', edad, 'años')