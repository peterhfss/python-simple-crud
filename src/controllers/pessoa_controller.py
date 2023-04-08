from ..models.pessoa import Pessoa
from typing import List

"""
    Controller da entidade Pessoa.
"""

class PessoaController:
    pessoas = []

    @classmethod
    def salvar_pessoa(cls, pessoa:Pessoa) -> None:
        cls.pessoas.append(pessoa)

    @classmethod
    def listar_pessoas(cls) -> List[Pessoa]:
        return cls.pessoas