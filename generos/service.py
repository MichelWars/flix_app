import streamlit as st

from generos.repository import GenerosRepository


class GeneroService:
    def __init__(self):
        self.genero_repository = GenerosRepository()

    def get_generos(self):
        if 'generos' in st.session_state:
            return st.session_state.genero
        generos = self.genero_repository.get_generos()
        st.session_state.genero = generos
        return generos

    def create_generos(self, nome):
        genero = dict(nome=nome)
        novo_genero = self.genero_repository.create_genero(genero)
        st.session_state.genero.append(novo_genero)
        return novo_genero
