from person import Person
from virus import Virus
from logger import Logger
from simulation import Simulation

def test_simulation_init():
    virus = Virus("Ebola", .3, .8)
    sim = Simulation(10000, .9, virus, 1)
    assert sim.pop_size == 10000
    assert sim.vacc_percentage == .9
    assert sim.virus.name == "Ebola"
    assert sim.initial_infected == 1

def test_create_population():
    virus = Virus("Ebola", .3, .8)
    sim = Simulation(10, .5, virus, 1)
    assert sim.population[0].infection == virus
    assert sim.population[3].infection is None
    assert sim.population[3].is_alive is True
    assert sim.population[3].is_vaccinated is True
    assert sim.population[7].infection is None
    assert sim.population[7].is_alive is True
    assert sim.population[7].is_vaccinated is False


def test_simulation_should_continue():
    virus = Virus("Ebola", .3, .8)
    sim = Simulation(10, 1, virus, 1)
    person1 = Person(1, True, virus)
    person2 = Person(2, False)
    sim.population = [person1, person2]
    assert sim._simulation_should_continue() is True

    person1.is_alive = False
    person2.is_alive = False
    assert sim._simulation_should_continue() is False

def test_run():
    pass


def test_interaction():
    virus = Virus("Ebola", 1, .8)
    sim = Simulation(10, .5, virus, 1)
    person = Person(1, False, virus)
    random_person = Person(2, True)
    assert sim.interaction(person, random_person) == "random is vaccinated"
    random_person.infection = virus
    random_person.is_vaccinated = False
    assert sim.interaction(person, random_person) == "random is already infected"
    random_person.infection = None
    assert sim.interaction(person, random_person) == "random got infected"
    virus.repro_rate = 0
    assert sim.interaction(person, random_person) == "random got lucky"

def test_time_step():
    pass

def test_infect_newly_infected():
    virus = Virus("Ebola", .2, .8)
    sim = Simulation(10, .5, virus, 1)
    sim.newly_infected = [sim.population[1], sim.population[5]]
    sim._infect_newly_infected()
    assert sim.population[1].infection == virus
    assert sim.population[5].infection == virus