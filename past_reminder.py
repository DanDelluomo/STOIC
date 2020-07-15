class Past_Reminder:
    """Cycle through past daily reflections."""  
    
    def __init__(self):
        reflections = open('reflections.txt', 'r')
        self.reflections = [i for i in reflections]
    
    def cycle(self):
        """Print each reflection."""
        print('\n')
        for reflection in self.reflections:
            print(reflection)


if __name__ == '__main__':
    reminders = Past_Reminder()
    reminders.cycle()


        

    
    
    



