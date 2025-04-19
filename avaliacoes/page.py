import pandas as pd
import streamlit as st
from avaliacoes.service import AvaliacaoService
from filmes.service import FilmeService
from st_aggrid import AgGrid


def mostrar_avaliacoes():
    avaliacao_service = AvaliacaoService()
    avaliacao = avaliacao_service.get_avaliacoes()

    if avaliacao:
        st.write('Avaliações')
        avaliacao_df = pd.json_normalize(avaliacao)
        AgGrid(
            data=avaliacao_df,
            reload_data=True,
            key='avaliacoes'
        )
    else:
        st.warning("Nenhuma avaliação encontrada")

    st.title("Cadastrar avaliacao")

    filme_service = FilmeService()
    filme = filme_service.get_filmes()
    titulo_filme = {filme['titulo']: filme['id'] for filme in filme}
    selecionar_filme = st.selectbox('Filme', list(titulo_filme.keys()))

    estrelas = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comentario = st.text_area('Comentario')

    if st.button('Avaliar'):
        nova_avaliacao = avaliacao_service.create_avaliacao(
            filme=titulo_filme[selecionar_filme],
            estrelas=estrelas,
            comentario=comentario,
        )
        if nova_avaliacao:
            st.rerun()
        else:
            st.error("Erro ao avaliar")
