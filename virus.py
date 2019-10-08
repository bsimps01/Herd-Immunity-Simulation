class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def virus_sars(self):
    virus = Virus("Sars", 0.75, 0.6)
    virus.name == "Sars"
    virus.repro_rate == 0.75
    virus.mortality_rate == 0.6

def virus_flu(self):
    virus = Virus("Flu", 0.6, 0.5)
    virus.name == "Flu"
    virus.repro_rate == 0.6
    virus.mortality_rate == 0.5

def virus_whooping_cough(self):
    virus = Virus("Whooping Cough", 0.7, 0.25)
    virus.name == "Whooping Cough"
    virus.repro_rate == 0.7
    virus.mortality_rate == 0.25