# pgadmin code for dbconnection  


# from sqlalchemy.engine import create_engine
# from sqlalchemy import MetaData
# from app.utils.get_secret import get_secret
# import json

# # DataBase Connection using AWS Secrets Manager for Data insert or update in DataBase
# pgadmin = get_secret("postgres_credentials")
# pg_login_details = json.loads(pgadmin)

# # Extract credentials
# db_host = pg_login_details['host']
# db_name = pg_login_details['engine']
# db_user = pg_login_details['username']
# db_pass = pg_login_details['password']
# db_port = pg_login_details['port']

# auth = f'{db_user}:{db_pass}'
# database = f"{db_host}:{db_port}/{db_name}"
# engine = create_engine(f"postgresql://{auth}@{database}", pool_recycle=3600, execution_options={
#         "isolation_level": "AUTOCOMMIT"
#     })
# engine.connect()
# meta = MetaData(bind=engine)