import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from atores.service import AtorService


def mostrar_atores():
    # recebe os dados de atores da API
    ator_service = AtorService()
    atores = ator_service.get_ator()

    st.write('Atores')

    # receba os dados como json e converte em data frame
    ator_df = pd.json_normalize(atores)
    AgGrid(
        data=ator_df,
        reload_data=True,
        key='atores'
    )

    st.title('Adicionar Ator')
    name = st.text_input('Nome do Ator')
    nascimento = st.date_input(
        label="Data de Nascimento",
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )

    nacionalidade_dropdown = ['BRA', 'USA']
    nacionalidade = st.selectbox(
        label='Nacionalidade',
        options=nacionalidade_dropdown,
    )
    if st.button('Salvar'):
        novo_ator = ator_service.criar_ator(
            nome=name,
            nascimento=nascimento,
            nacionalidade=nacionalidade,
        )
        if novo_ator:
            st.rerun()
        else:
            st.error("Erro ao cadastrar ator!")
