import streamlit as st

from filmes.repository import FilmesRepository


class FilmeService:
    def __init__(self):
        self.filme_repository = FilmesRepository()

    def get_filmes(self):
        if 'filmes' in st.session_state:
            return st.session_state.filme
        filmes = self.filme_repository.get_filmes()
        st.session_state.filme = filmes
        return filmes

    def create_filme(self, titulo, genero, ano_lancamento, atores, resumo):
        filme = dict(
            titulo=titulo,
            genero=genero,
            ano_lancamento=ano_lancamento,
            atores=atores,
            resumo=resumo,
        )
        novo_filme = self.filme_repository.create_filme(filme)
        st.session_state.filme.append(novo_filme)
        return novo_filme

    def get_stats_filmes(self):
        return self.filme_repository.get_stats_filmes()
