from datetime import datetime
date='01/04/1999 12:10:05'
date_obj=datetime.strptime(date,'%d/%m/%Y %H:%M:%S')
print(date_obj)