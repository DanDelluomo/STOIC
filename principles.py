class StoicPrinciples:
    """Repository of Major Stoic Principles."""

    def __init__(self):
        self.principles = {
            'Principle 1': 'Wake up early.' ,
            'Principle 2': 'Manage your expectations. Expect '\
                'unexpected hardships.' ,
            'Principle 3': 'Amor fati. Love fate.' ,
            'Principle 4': 'Find the good in everything.' ,
            'Principle 5': 'Memento mori. Remember death.' ,
            'Principle 6': 'Picture life without the people and '\
                'possessions you have to truly appreciate them.' ,
            'Principle 7': 'Go on long walks.' ,
            'Principle 8': 'Reflect on the good and bad at the '\
                'end of each day.' ,
        }
    
    def display(self):
        display_string = ''
        for principle in self.principles:
            display_string += principle.upper() + '   '
            display_string += self.principles[principle] + '\n'
        return display_string


if __name__ == '__main__':
    principles = StoicPrinciples()
    principles.display()