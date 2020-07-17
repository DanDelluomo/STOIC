class PastReminder:
    """Cycle through past daily reflections."""  
    
    def __init__(self):
        reflections = open('reflections.txt', 'r')
        self.reflections = [i for i in reflections]
    
    def cycle(self):
        """Print each reflection and take user input."""
        print('\n')
        self.analysis = {}
        for reflection in self.reflections:
            print('Ponder this...' + '\n' + reflection)
            self.analysis[reflection] = input('Have you improved this? ')
    
    def log(self):
        """Log results in reflect_log.txt."""
        with open('reflect_log.txt', 'a') as f:
            for principle in self.analysis:
                response = self.analysis[principle]
                if '\n' in principle:
                    principle = principle[:principle.index('\n')]
                log_string = principle + ': \n\t\t\t' + response + '\n\n'
                f.write(log_string)

          
if __name__ == '__main__':
    reminders = PastReminder()
    reminders.cycle()
    reminders.log()


        

    
    
    



