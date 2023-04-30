"""
Conftest

Custom fixtures are defined in the fixtures/ folder, so far there are 2 files:
- Faker data: Fixtures which generates data with Faker
- Session: Fixtures which stores the command line parameters
"""

pytest_plugins = [
    'fixtures.booking_faker_data',
    'fixtures.booking_session',
]
