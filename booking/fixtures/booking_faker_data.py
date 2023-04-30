from datetime import datetime, timedelta
from pytest import fixture
from faker import Faker


@fixture(scope='module')
def randomFirstNameGenerator():
    '''Generates a random First Name'''
    return Faker().first_name()


@fixture(scope='module')
def randomLastNameGenerator():
    '''Generates a random Last Name'''
    return Faker().last_name()


@fixture(scope='module')
def todayDate():
    '''Returns todays' date with the specified format'''
    currentDate = datetime.now()
    currentDateFormatted = currentDate.strftime('%m/%d/%Y %H:%M')
    return currentDateFormatted


@fixture(scope='module')
def nextWeekDate():
    '''Returns next weeks' same date with the specified format'''
    currentDate = datetime.now()
    nextWeekDate = currentDate + timedelta(7)
    nextWeekDateFormatted = nextWeekDate.strftime('%m/%d/%Y %H:%M')
    return nextWeekDateFormatted
