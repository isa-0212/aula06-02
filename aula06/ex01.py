import pandas as pd
from sqlalchemy import create_engine

host = 'localhost' #127.0.0.1
user = 'root'
password = ''
database = 'bd_biblioteca03'

#URL de conexão
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


try:
    #lendo as tabelas
    df_usuarios = pd.read_sql('tb_usuarios',engine)
    # print(df_usuarios)
    df_livros = pd.read_sql('tb_livros',engine)
    # print(df_livros)
    df_itens_alugados = pd.read_sql('tb_itens_alugados',engine)
    # print(df_itens_alugados)
    df_alugados = pd.read_sql('tb_alugados',engine)
    # print(df_alugados)


except Exception as e:
    print(f'Erro na conexão {e}')


# Relacionando
    
try:
        #Livros com itens
        df_merge1 = pd.merge(
            df_livros,
            df_itens_alugados,
            on ='id_livro'
        )
        #print(df_merge1)
        # OBS: quando as séries forem de nomes diferentes
        # df_merge1 = pd.merge(
        #     df_livros,
        #     df_itens_alugados,
        #     left_on ='codigo_livro'
        # )




        df_merge2 = pd.merge(
          df_merge1,
          df_alugados,
          on = 'id_aluguel'
     )

        # print(df_merge2)

        
        
        #Resultado atual (merge 1 e alugados) com usuários

        df_dados = pd.merge(df_merge2, df_usuarios, on='id_usuario')
        # print(df_dados)

        filtro = (
             (df_dados['data_devolucao'] >= '2024-11-01') & 
             (df_dados['data_devolucao']<='2024-11-30')
        )
        
        # print(filtro)
        df_novembro = df_dados.query(
             'data_devolucao >= "2021-11-01" and data_devolucao <= "2024-11-30"'

        )
      

        # df_novembro = df_dados[filtro]
        print('\nRelatório de livros alugados em novembro: ')
        print(
             df_novembro[
                  [
                       'id_usuario', 'nome', 'cidade',
                       'id_aluguel', 'data_aluguel', 'data_devolucao','valor',
                       'id_livro','titulo','autor'
                  ]
             ]
        )


except Exception as e:
    print(f'Erro {e}')

