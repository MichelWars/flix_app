import streamlit as st

from atores.repository import AtorRepository


class AtorService:
    def __init__(self):
        self.ator_repository = AtorRepository()

    def get_ator(self):
        if 'atores' in st.session_state:
            return st.session_state.ator
        atores = self.ator_repository.get_atores()
        st.session_state.ator = atores
        return atores

    def criar_ator(self, nome, nascimento, nacionalidade):
        ator = dict(
            nome=nome,
            nascimento=nascimento,
            nacionalidade=nacionalidade,
        )
        novo_ator = self.ator_repository.create_ator(ator)
        st.session_state.ator.append(novo_ator)
        return novo_ator
