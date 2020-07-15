class Stoic_Principles:
    """Repository of Major Stoic Principles."""
    
    def __init__(self):
        self.principles = {
            'Principle 1': 'Wake up early.' ,
            'Principle 2': 'Manage your expectations. Expect '\
                'unexpected hardships.' ,
            'Principle 3': 'Amor fati: Love fate.' ,
            'Principle 4': 'Find the good in everything.' ,
            'Principle 5': 'Memento mori: Remember death.' ,
            'Principle 6': 'Picture life without the people and '\
                'possessions you have to truly appreciate them.' ,
        }
    
    def display(self):
        for principle in self.principles:
            print(principle + ': ' + self.principles[principle])


if __name__ == '__main__':
    principles = Stoic_Principles()
    principles.display()