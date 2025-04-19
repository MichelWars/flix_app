import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from generos.service import GeneroService


def mostrar_generos():

    genero_service = GeneroService()
    generos = genero_service.get_generos()

    if generos:
        st.write('Generos')
        genero_df = pd.json_normalize(generos)
        AgGrid(
            data=genero_df,
            reload_data=True,
            key='generos_grid'
        )
    else:
        st.warning('Nenhum genero cadastrado')

    st.title('Adicionar Genero')
    nome = st.text_input('Nome do Genero')
    if st.button('Salvar'):
        novo_genero = genero_service.create_generos(
            nome=nome
        )
        if novo_genero:
            st.success(f'Genero {nome} salvo com sucesso')
            st.rerun()
        else:
            st.error('Erro ao salvar genero')
