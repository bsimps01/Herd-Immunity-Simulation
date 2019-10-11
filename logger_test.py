import os
from virus import Virus
from person import Person
from logger import Logger


def test_logger_metadata():
    logger = Logger('test_log.txt')
    logger.write_metadata(100, 0.9, 'Ebola', 0.7, 0.25)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert val == '100+0.9+Ebola+0.7+0.25\n'

    os.remove('test_log.txt')


def test_log_interaction_first_case():
    logger = Logger('test_log.txt')

    virus = Virus("Ebola", 0.25, 0.70)

    person1 = Person(1, False, virus)
    person2 = Person(2, True, None)

    logger.log_interaction(person1, person2, True, False)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        print(val)
        assert "1 didn't infect 2 because they are sick" in val
    
    os.remove('test_log.txt')


def test_log_interaction_second_case():
    logger = Logger('test_log.txt')

    virus = Virus("Ebola", 0.25, 0.70)

    person1 = Person(1, False, virus)
    person2 = Person(2, True, None)

    logger.log_interaction(person1, person2, False, True)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert "1 didn't infect 2 because they are vaccinated" in val

    os.remove('test_log.txt')


def test_log_interaction_third_case():
    logger = Logger('test_log.txt')

    virus = Virus("Ebola", 0.25, 0.70)

    person1 = Person(1, False, virus)
    person2 = Person(2, True, None)

    logger.log_interaction(person1, person2, False, False, True)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert "1 infects 2" in val

    os.remove('test_log.txt')


def test_log_infection_survival_survived():
    logger = Logger('test_log.txt')

    person1 = Person(1, False, None)

    logger.log_infection_survival(person1, False)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert '1 survived the infection' in val

    os.remove('test_log.txt')


def test_log_infection_survival_died():
    logger = Logger('test_log.txt')

    person1 = Person(1, False, None)

    logger.log_infection_survival(person1, True)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert '1 died from infection' in val

    os.remove('test_log.txt')


def test_log_timestep():
    logger = Logger('test_log.txt')

    logger.log_time_step(1)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert 'Time step 1 ended, beginning 2' in val

    logger.log_time_step(2)

    with open('test_log.txt', 'r') as f:
        val = f.read()
        assert 'Time step 2 ended, beginning 3' in val

    os.remove('test_log.txt')