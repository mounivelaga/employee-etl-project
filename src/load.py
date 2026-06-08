from sqlalchemy import create_engine
from logger import logger


def load_data(df, config):

    if df.empty:
        logger.warning("No data to load")
        return

    connection_string = (
        f"postgresql://{config['db_user']}:"
        f"{config['db_password']}@"
        f"{config['db_host']}:"
        f"{config['db_port']}/"
        f"{config['db_name']}"
    )

    engine = create_engine(connection_string)

    df.to_sql("employees", con=engine, if_exits="replace", index=False)

    logger.info("data loaded successfully")

    engine.dispose()

    print("Employee data  loaded into PostgreSQL")
