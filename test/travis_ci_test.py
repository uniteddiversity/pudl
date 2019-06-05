"""Limited testing of the PUDL DB ETL for use with Travis CI."""
import logging
import pytest
import pandas as pd
from pudl import constants as pc

logger = logging.getLogger(__name__)

START_DATE_CI = pd.to_datetime(
    '{}-01-01'.format(max(pc.working_years['eia923'])))
END_DATE_CI = pd.to_datetime(
    '{}-12-31'.format(max(pc.working_years['eia923'])))


@pytest.mark.travis_ci
def test_ferc1_init_db(ferc1_engine_travis_ci):
    """
    Create a fresh FERC Form 1 DB and attempt to access it.

    If we are doing ETL (ingest) testing, then these databases are populated
    anew, in their *_test form.  If we're doing post-ETL (post-ingest) testing
    then we just grab a connection to the existing DB.

    Nothing needs to be in the body of this "test" because the database
    connections are created by the fixtures defined in conftest.py
    """
    pass


@pytest.mark.travis_ci
def test_pudl_init_db(pudl_engine_travis_ci):
    """
    Create a fresh PUDL DB and pull in some FERC1 & EIA data.

    If we are doing ETL (ingest) testing, then these databases are populated
    anew, in their *_test form.  If we're doing post-ETL (post-ingest) testing
    then we just grab a connection to the existing DB.

    Nothing needs to be in the body of this "test" because the database
    connections are created by the fixtures defined in conftest.py
    """
    pass
