from pydantic import BaseSettings

class Settings(BaseSettings):
    
    # postgres envs
    
    PGDB_USERNAME: str = "postgres"
    PGDB_PASSWORD: str = "postgres"
    PGDB_PORT: int = 5432
    PGDB_DBNAME: str = "postgres"
    PGDB_HOSTNAME: str = "postgresdb"
    
    # mongo envs
    # MGDB_USERNAME: str
    # MGDB_PASSWORD: str
    # MGDB_PORT: int
    # MGDB_DBNAME: str
    # MGDB_HOSTNAME: str
    
    # Sentry debugger
    ENABLE_SENTRY:bool = False
    SENTRY_DSN:str = "http://sentry-dsn-url/"


settings = Settings()