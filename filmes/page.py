import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from atores.service import AtorService
from filmes.service import FilmeService
from generos.service import GeneroService


def mostrar_filmes():
    filme_service = FilmeService()
    filmes = filme_service.get_filmes()

    if filmes:
        st.write('Lista de Filmes')

        filmes_df = pd.json_normalize(filmes)
        filmes_df = filmes_df.drop(columns=['atores', 'genero.id', 'resumo'])

        AgGrid(data=filmes_df, reload_data=True, key='filmes')
    else:
        st.warning('Nenhum filme encontrado')

    st.title('Adicionar filme')
    titulo = st.text_input('Nome do filme')

    ano_lancamento = st.number_input(
        label='Ana de Lançamento',
        min_value=1930,
        max_value=2025,
        step=1,
    )
    genero_service = GeneroService()
    generos = genero_service.get_generos()
    genero_nomes = {genero['nome']: genero['id'] for genero in generos}
    selecionar_genero = st.selectbox('Gênero', list(genero_nomes.keys()))

    ator_service = AtorService()
    atores = ator_service.get_ator()
    nome_atores = {ator['nome']: ator['id'] for ator in atores}
    selecionar_atores = st.multiselect('Elenco', list(nome_atores.keys()))
    selecionar_atores_id = [nome_atores[nome] for nome in selecionar_atores]

    resumo = st.text_area('Resumo')

    if st.button('Salvar'):

        novo_filme = filme_service.create_filme(
            titulo=titulo,
            ano_lancamento=ano_lancamento,
            genero=genero_nomes[selecionar_genero],
            atores=selecionar_atores_id,
            resumo=resumo,
        )

        if novo_filme:
            # debug
            print(novo_filme)
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme')
