#!/usr/bin/env python
# coding: utf-8

# In[10]:


dict_to_validate = {"name": "Sarila", "address": "Chyamasingh, Bhaktapur", "age": 22, "score": 90,  "covid": False}
rules = {"name": (6, 10), "address": (15, 50), "age" : (18, 40), "score" : (40, 100)}

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
            min_length, max_length = rules[each]
#             print(min_length, max_length)
            res = string_validator(dict_to_validate[each], min_length, max_length)
            result.append(res)
        if type(dict_to_validate[each]) == int:
            min_value, max_value = rules[each]
            res = number_validator(dict_to_validate[each], min_value, max_value)
            result.append(res)
        if type(dict_to_validate[each]) == bool:
            res = boolean_validator(dict_to_validate[each])
            result.append(res)
        
    print(result)
#         print(each, dict_to_validate[each])
        
validate_generic_data(dict_to_validate, rules)


# In[ ]:




