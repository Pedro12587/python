import json # lidar com arquivos JSON
from pathlib import Path # lidar com os caminhos do windows

# JSON - JavaScript Object Notation

class BancoFake:
    # Instancionando o inicio da classe

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": []} # clientes iniciando com vazio

        # Carregar valores anteriores salvos
        self._carregar()

    def _carregar(self):
        """
        Carregar dados d arquivo JSON, se existir.
        Caso não exista, inicar banco novo
        """

        caminho = Path(self.arquivo_db)
        # verifica se arquivo existe
        if caminho.is_file():
            # abrindo arquivo no modo leitura em UTF-8 (PT-BR)
            with open(caminho, "r", encoding="utf-8") as arquivo:
                # carregar dados anteriores salvos
                self.dados = json.load(arquivo)
        else:
            # chamar função para criar novo arquivo
            self._salvar()
    
    def _salvar(self):
        """

        Salvar o conteudo do self.dados no JSON

        """
        # Abrir o arquivo no modo W (Escrita)

        with open(self.arquivo_db, "w", encoding="utf-8") as dados:
            # realizar um DUMP de PYTHON para JSON
            # ensure_ascii = false - Escritas, emojis, não viram código
            # indent = identação - 4 recuo
            json.dump(self.dados, dados, ensure_ascii=False, indent=4)

    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]
    