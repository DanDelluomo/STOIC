class Daily_Reflection:
    """Performs daily reflection task based on user input."""
    
    def __init__(self):
        self.improvements = []
        user_input = input('What went wrong today? What can you improve on? ')
        self.improvements.append(user_input)

    def extra_grabber(self):
        """Adds as many extra improvements as necessary."""
        more = input('Is there anything else you can improve on? ')
        if more in {'yes', 'y', 'YES', 'Yes', 'yup', 'yeah', 'Y',
                    'YUP', 'si', 'oh yes'}:
                extra = input('What was it? ')
                self.improvements.append(extra)
        else:
            return False

    def file_writer(self):
        with open('reflections.txt', 'a') as file:
            for i in self.improvements:
                file.write(i + '\n')
    
    def log_writer(self):
        from datetime import datetime
        time = datetime.today()
        year, month, day = time.year, time.month, time.day
        hour, minute = time.hour, time.minute
        if minute < 10:
            minute = str(minute).zfill(2)
        with open('date_log.txt', 'a') as file:
            for i in self.improvements:
                file.write(i + '\n')
            date_string = f'{month}/{day}/{year} at {hour}:{minute}\n'
            file.write('\t' * 3 + 'Recorded on ' + date_string)
        

if __name__ == '__main__':
    daily_reflect = Daily_Reflection()
    while daily_reflect.extra_grabber() is not False:
        daily_reflect.extra_grabber()
    # record improvements       
    daily_reflect.file_writer()
    daily_reflect.log_writer()





