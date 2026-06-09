import pandas as pd
from sqlalchemy import create_engine

host = 'localhost' #127.0.0.1
user = 'root'
password = ''
database = 'bd_pedidos'

#URL de conexão
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

try:
    df_clientes = pd.read_sql('tb_clientes', engine)
    # print(df_clientes)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    # print(df_pedidos)
    df_itens = pd.read_sql('tb_itens', engine)
    # print(df_itens)
    df_produtos = pd.read_sql('tb_produtos', engine)
    # print(df_produtos)
except Exception as e:
    print(f'Erro na conexão {e}')


try:
    df_merge1 = pd.merge(
        df_produtos,
        df_itens,
        on = 'codigo_produto'    
    )
    # print(df_merge1)

    df_merge2 = pd.merge(
        df_merge1,
        df_pedidos,
        on = 'codigo_pedido'
    )
    # print(df_merge2)

    df_merge3 = pd.merge(
        df_merge2,
        df_clientes,
        on = 'codigo_cliente'
    )
    print(df_merge3)

    # filtro = (
    #     (df_merge3['cidade'] == 'Sao Paulo')
        
    # )


    filtro = (
        (df_merge3['cidade'] == 'Sao Paulo') |
        
        (df_merge3['cidade'] == 'Curitiba')
    )

    print(filtro)
    
    # df_cidade = df_merge3.query(
    #     'cidade == "Sao Paulo"' 
    # )

    df_cidade = df_merge3.query(
        'cidade == "Sao Paulo" or cidade == "Curitiba"'
    )
    # print(df_cidade)

    print('\nRelatório de pedidos realizados na cidade de São Paulo ou Curitiba')
    print(
        df_cidade[    
            
            [
                # 'codigo_cliente',
                'nome','sobrenome',
                'cidade', 'codigo_pedido','data_pedido',
                'produto','valor'
            
            ]
            
         ]
)
    


except Exception as e:
    print(f'Erro {e}')

