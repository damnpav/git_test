from datetime import datetime as dt


with open(r'test_file.txt', 'a') as text_file:
   print('write')
   text_file.write(f'{dt.now().strftime("%H:%M:%S")}: test\n')


