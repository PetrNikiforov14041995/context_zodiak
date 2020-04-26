import datetime
from pip._internal.utils import encoding

class Logger:
    def __init__(self, log_path, encoding='utf-8'):
      self.log_file = open(log_path, 'a', encoding=encoding)
        
    def __enter__(self):
      self.start_time = datetime.datetime.utcnow()
      return self
    def write_log(self, action):
      self.log_file.write(f'{datetime.datetime.utcnow()}\n')  
    def __exit__(self, exc_type, exc_val, exc_tb):
      self.stop_time = datetime.datetime.utcnow()
      self.diff = self.stop_time - self.start_time
      self.log_file.write(f'Время старта: {self.start_time}\nВремя финиша: {self.stop_time}\nКод выполнился за {self.diff}\n')       
      self.log_file.close()

      print(f'Время старта: {self.start_time}')
      print(f'Время финиша: {self.stop_time}')
      print(f'Код выполнился за {self.diff}')
    
      
      

def zodiak():
  month = input('Введите название месяца рождения:')
  day = int(input('Введите число рождения:'))


  if (month in {'январь','март','май','июль','август','октябрь','декабрь'} and 1<= day<=31) or (month in {'апрель','июнь','сентябрь','ноябрь'} and 1<= day<= 30) or (month == 'февраль' and 1<= day <= 29):

    if (21 <= day and month == 'март') or (day <= 20 and month == 'апрель'):
      print('Овен')
    elif (21 <= day and month == 'апрель') or (day <= 21 and month == 'май'):
      print('Телец')
    elif (22 <= day and month == 'май') or (day <= 21 and month == 'июнь'):
      print('Близнецы')
    elif (22 <= day and month == 'июнь') or (day <= 22 and month == 'июль'):
      print('Рак')
    elif (23 <= day and month == 'июль') or (day <= 21 and month == 'август'):
      print('Лев')
    elif (22 <= day and month == 'август') or (day <= 23 and month == 'сентябрь'):
      print('Дева')
    elif (24 <= day and month == 'сентябрь') or (day <= 23 and month == 'октябрь'):
      print('Весы')
    elif (24 <= day and month == 'октябрь') or (day <= 22 and month == 'ноябрь'):
      print('Скорпион')
    elif (23 <= day and month == 'ноябрь') or (day <= 22 and month == 'декабрь'):
      print('Стрелец')
    elif (23 <= day and month == 'декабрь') or (day <= 20 and month == 'январь'):
      print('Козерог')  
    elif (21 <= day and month == 'январь') or (day <= 19 and month == 'февраль'):
      print('Водолей')
    elif (20 <= day and month == 'февраль') or (day <= 20 and month == 'март'):
      print('Рыбы') 
  else:
    print('Неверное значение!')

if __name__ == '__main__':
  with Logger('Time.log') as log:
    zodiak()
    
    