import pandas as pd  
from sqlalchemy import create_engine

host = 'localhost' #127.0.0.1
user = 'root'
password = ''
database = 'bd_mod02_aula03'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

query1 = '''
select * 
from materiais_construcao;
'''

query2 = '''
select produto, preco
from materiais_construcao;
'''

query3 = '''
select *
from  materiais_construcao
where categoria = 'cimento';
'''

query4 = '''
select *
from materiais_construcao
where preco > 200;
'''

query5 ='''
select *
from materiais_construcao
where categoria = 'agregado'
and preco > 200;
'''
query6 = '''
select *
from materiais_construcao
where categoria = 'cimento'
and `quantidade_vendida` > 3000;

'''

query7 = '''
select *
from materiais_construcao
where fornecedor = 'local'
or 'votoran';

'''

query8 = '''
select *
from materiais_construcao
where categoria = 'alvenaria'
and fornecedor = 'olaria';

'''

df_materiais = pd.read_sql(query1,engine)
print('\nTodos os registros')
print(df_materiais)
print(30*'-')

df_materiais = pd.read_sql(query2,engine)
print('\nProdutos e Preços')
print(df_materiais)
print(30*'-')

df_materiais = pd.read_sql(query3,engine)
print('\nCimeto')
print(df_materiais)
print(30*'-')


df_materiais = pd.read_sql(query4,engine)
print('\nPreço acima de 20')
print(df_materiais)
print(30*'-')


df_materiais = pd.read_sql(query5,engine)
print('\nAgregado acima de 200')
print(df_materiais)
print(30*'-')


df_materiais = pd.read_sql(query6,engine)
print('\nCimento vendido acima de 3000')
print(df_materiais)
print(30*'-')

df_materiais = pd.read_sql(query7,engine)
print('\nFornecedor Local ou Votoran')
print(df_materiais)
print(30*'-')

df_materiais = pd.read_sql(query8,engine)
print('\nFornecedor olaria e caegoria alvenaria ')
print(df_materiais)
print(30*'-')



