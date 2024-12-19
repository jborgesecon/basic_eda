import pandas as pd
import sqlalchemy as sa


st_conn = sa.create_engine("postgres://my_name:passwd@localhost:0000/my_database")

table_to_add = pd.read_csv('./file.csv')
# send information from this csv to services.dim_client

try:
    # Create the SQLAlchemy engine
    engine = sa.create_engine(db_connection_str)

    # Read the CSV file into a Pandas DataFrame
    table_to_add = pd.read_csv('./file.csv')

    # Use the to_sql method for efficient insertion
    table_to_add.to_sql(
        name='dim_client',  # Table name
        con=engine,          # SQLAlchemy engine
        schema='services',   # Schema name
        if_exists='append',  # Append data if table exists, 'replace' to overwrite, 'fail' to raise an error
        index=False,         # Don't write DataFrame index as a column
        method='multi',     # Use multi-row insert for performance
        chunksize=1000       # Insert in batches of 1000 rows (adjust as needed)
    )

    print("Data successfully inserted into services.dim_client")

except sa.exc.SQLAlchemyError as e:
    print(f"An error occurred during database operation: {e}")
except FileNotFoundError:
    print("Error: CSV file not found.")
except pd.errors.ParserError as e:
    print(f"Error parsing the CSV file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if 'engine' in locals() and engine:
        engine.dispose() #important to release the connection

200.000
170.000

database = {
    'postgres': {
        'data_warehouse': [
            'uname',
            'passwd'
            'dbname',
            'host',
        ],
        'beautiful_garden': [
            'uname2',
            'passwd2',
            'dbname2',
            'host'
        ]
    },
    'mysql':{
        ...
    }
}

jg
0   MASCARA             28566 non-null  float64
1   NOME_ESTADO         28566 non-null  object
2   matricula           28566 non-null  float64
3   Count of matricula  28566 non-null  float64
4   nome                28566 non-null  object
5   dt_inicio_contrato  28566 non-null  datetime64[ns]
6   dt_fim_contrato     28369 non-null  datetime64[ns]
7   dt_desl_termino     15158 non-null  datetime64[ns]
8   tipo_gestao         28566 non-null  object
9   month               28566 non-null  datetime64[ns]

tadeu
0   matricula           34075 non-null  object        
1   matricula_status    34074 non-null  object        
2   nome                34074 non-null  object        
3   possui_cc           34074 non-null  object        
4   centro_de_custo     34074 non-null  object        
5   possui_contrato     34074 non-null  object        
6   tipo_gestao         34074 non-null  object        
7   dt_inicio_contrato  34074 non-null  datetime64[ns]
8   dt_fim_contrato     34074 non-null  datetime64[ns]
9   dt_desl_termino     34074 non-null  datetime64[ns]
10  month               34076 non-null  object        


