class PastReminder:
    """Cycle through past daily reflections."""  
    
    def __init__(self):
        reflections = open('reflections.txt', 'r')
        self.reflections = [i for i in reflections]
    
    def cycle(self):
        """Print each reflection."""
        print('\n')
        reflections = {}
        for reflection in self.reflections:
            print('Ponder this...' + '\n' + reflection)
            reflections[reflection] = input('Have you improved this? ')
        return reflections
        
        
if __name__ == '__main__':
    reminders = PastReminder()
    reminders.cycle()


        

    
    
    



