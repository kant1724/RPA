import datetime

def reprocess_value(value):
    value = value.replace('{prev_date}', str(datetime.date.today() - datetime.timedelta(1)))
    value = value.replace('-', '')
    
    return value
