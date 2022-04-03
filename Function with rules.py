#!/usr/bin/env python
# coding: utf-8

# In[4]:


dict_to_validate = {"age": 30, "name": "This is Sarila", "covid": False}
rules = {"min_length" : 6, "max_length" : 8 , "min_value": 18, "max_value": 38}

result = []
def string_validator(string_to_validate, min_length, max_length):
    string_length = len(string_to_validate)
    if string_length >= min_length and string_length <= max_length:
        return True
    else:
        return False
    
def number_validator(number_to_validate, min_value, max_value):
    if number_to_validate >= min_value and number_to_validate <= max_value:
        return True
    else :
        return False
    
def boolean_validator(bool_to_validate):
    if bool_to_validate == True or bool_to_validate == False:
        return True
    else:
        return False
    

# print(dict_to_validate)
def validate_generic_data(dict_to_validate, rules):
    for each in dict_to_validate:
#         print(type(dict_to_validate[each]))
        if type(dict_to_validate[each]) == str:
            res = string_validator(dict_to_validate[each], rules["min_length"], rules["max_length"])
            result.append(res)
        if type(dict_to_validate[each]) == int:
            res = number_validator(dict_to_validate[each], rules["min_value"], rules["max_value"])
            result.append(res)
        if type(dict_to_validate[each]) == bool:
            res = boolean_validator(dict_to_validate[each])
            result.append(res)
        
    print(result)
#         print(each, dict_to_validate[each])
        
validate_generic_data(dict_to_validate, rules)


# In[ ]:




