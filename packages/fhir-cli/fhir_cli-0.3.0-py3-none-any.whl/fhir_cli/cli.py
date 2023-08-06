import fire
from psycopg2 import ProgrammingError, connect, sql
from psycopg2.extras import RealDictCursor
from requests import HTTPError

from fhir_cli import (
    DBT_SCHEMA,
    FHIR_COLUMN_NAME,
    POSTGRES_HOST,
    POSTGRES_PORT,
    PROJECT_DB,
    PROJECT_USER,
    PROJECT_USER_PASSWORD,
    log,
)
from fhir_cli.admin import Admin
from fhir_cli.dbt import Dbt
from fhir_cli.fhir_resource import FhirResource, FhirValidationError
from fhir_cli.utils.compact import dict_compact
from fhir_cli.utils.number_print import number_print


def get_resource_from_model(model: str) -> dict:
    """get_resource_from_model looks for a fhir model file and retrieves a Fhir resource"""
    conn = connect(
        host=POSTGRES_HOST,
        dbname=PROJECT_DB,
        port=POSTGRES_PORT,
        user=PROJECT_USER,
        password=PROJECT_USER_PASSWORD,
        cursor_factory=RealDictCursor,
        options=f"-c search_path={DBT_SCHEMA}",
    )
    conn.autocommit = True

    with conn.cursor() as curs:
        curs.itersize = 1
        select_fhir_stmt = sql.SQL("SELECT {fhir_column_name} FROM {fhir_model}").format(
            fhir_column_name=sql.Identifier(FHIR_COLUMN_NAME),
            fhir_model=sql.Identifier(model),
        )
        curs.execute(select_fhir_stmt)
        row = curs.fetchone()
    conn.close()
    resource = dict_compact(row[FHIR_COLUMN_NAME])
    return resource


class Cli:
    """a cli to manage your DbtOnFhir project"""

    def __init__(self):
        self.dbt = Dbt()
        self.admin = Admin()

    @staticmethod
    def validate(model: str):
        """Extract a fhir model row and validates the Fhir resource
        against a Fhir server

        Args:
            model (str): should be a valid DBT Fhir model name such as `observation_heartrate`
        """
        try:
            resource = get_resource_from_model(model)
        except ProgrammingError as e:
            log.error(e)
            return
        fhir = FhirResource(resource)
        number_print(repr(fhir))
        try:
            fhir.validate()
            log.info("\U0001F525 resource is valid")
        except HTTPError as e:
            log.error(e.response.json())
        except FhirValidationError as e:
            log.error(e)


def run():
    cli = Cli()
    fire.Fire(cli)


if __name__ == "__main__":
    run()
