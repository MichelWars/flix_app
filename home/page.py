import plotly.express as px
import streamlit as st

from filmes.service import FilmeService


def show_home():
    filme_service = FilmeService()
    filme_stats = filme_service.get_stats_filmes()

    st.title('Estatisticas de filme')

    if len(filme_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Genero')
        fig = px.pie(
            filme_stats['movies_by_genre'],
            values='count',
            names='genero__nome',
            title='Filmes por Genero',
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(filme_stats['total_moveis'])

    st.subheader('Quantidade de Filmes por Genero')
    for genero in filme_stats['movies_by_genre']:
        st.write(f"{genero['genero__nome']}: {genero['count']}")

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(filme_stats['total_avaliacoes'])

    st.subheader('Media Geral de Estrelas')
    st.write(filme_stats['average_stars'])
