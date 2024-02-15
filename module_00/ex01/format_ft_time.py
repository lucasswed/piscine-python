import datetime


date_timestamp = datetime.datetime.now().timestamp()
current_date = datetime.date.today()
formatted_date = current_date.strftime('%b %d %Y')

print('Seconds since January 1, 1970: {:,}'.format(date_timestamp), end=' ')
print('or {:e} in scientific notation'.format(date_timestamp))
print('{}'.format(current_date.strftime('%b %d %Y')))
