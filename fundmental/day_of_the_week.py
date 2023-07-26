from datetime import datetime
date_time_str = '21/01/2017'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y')
print ("The date is", date_time_obj.strftime('%A'))
