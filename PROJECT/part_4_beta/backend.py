###############
# PART 1 Code #
###############

def get_matches(list_data, key, val):
    list_dict = []
    for i in list_data: 
        if i.get(key) == val:  
            list_dict.append(i) 
    return list_dict

# print(get_matches(data, 'tow_description', 'ILLEGAL'))

def list_descriptions(list_data):
    list_str = []
    for i in list_data: 
        if i.get('tow_description') not in list_str:
            list_str.append(i.get('tow_description'))
    return list_str
    
# print(list_descriptions(data))

def count_by_month(list_data):
    raw_data = [] 
    list_months_count = [] 
    for i in list_data: 
        val = i.get('tow_date')
        month = int(val[5]+val[6])
        raw_data.append(month)
    for i in range(1, 13): 
        val = raw_data.count(i) 
        list_months_count.append(val) 
    return list_months_count
    

# print(count_by_month(data))

def count_by_day(list_data):
    raw_data = [] 
    list_day_count = [] 
    for i in list_data: 
        val = i.get('tow_date')
        date = int(val[8]+val[9])
        raw_data.append(date) 
    for i in range(1, 32):
        val = raw_data.count(i)
        list_day_count.append(val)
    return list_day_count

# print(count_by_day(data))

