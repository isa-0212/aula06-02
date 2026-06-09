 print('\nRelatório de pedidos realizados na cidade de São Paulo')
    print(
        df_cidade[    
            
            [   'codigo_cliente','nome','sobrenome',
            'cidade', 'codigo_pedido','data_pedido',
            'produto','valor'
            
            ]
            
         ]
             )