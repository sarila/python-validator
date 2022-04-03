#!/usr/bin/env python
# coding: utf-8

# In[64]:


dict_to_validate = {"name": 18, "address": "Chyamasingh, Bhaktapur", "age": "twenty", "score": 95.6,  "covid": False}
# rules={}
rules = {"name": ("str", 6, 15), "address": ("str", 10, 50), "age" : ("int", 18, 40), "score" : ("float", 40, 100)}
# rules = {"name": ("str", 6, 15), "age": ("int", 18, 40)}
# print(type(dict_to_validate["covid"]))
result = []
def string_validator(string_to_validate, data_type= "str", min_length= 6, max_length= 255):
#     print(type(string_to_validate))
    if isinstance(string_to_validate, str) :
        string_length = len(string_to_validate)
        if string_length >= min_length and string_length <= max_length:
            return True
        else:
            return False
    else: 
        print(f"{string_to_validate} must be string")
        return False
    
def int_validator(number_to_validate, data_type= "int", min_value= 1 , max_value= 100):
    if isinstance(number_to_validate, int):
        if number_to_validate >= min_value and number_to_validate <= max_value:
            return True
        else :
            return False
    else :
        print(f"{number_to_validate} must be integer")
        return False
    
def float_validator(number_to_validate, data_type= "float", min_value= 1 , max_value= 100):
    if isinstance(number_to_validate, float):
        if number_to_validate >= min_value and number_to_validate <= max_value:
            return True
        else :
            return False
    else:
        print(f"{number_to_validate} must be float")
        return False
    
def boolean_validator(bool_to_validate):
    if bool_to_validate == True or bool_to_validate == False:
        return True
    else:
        return False
    

def validate_generic_data(dict_to_validate, rules):
    for each in dict_to_validate:
        if each not in rules:
            if type(dict_to_validate[each]) == str:
                res = string_validator(dict_to_validate[each])
                if res == False:    
                    result.append(each)
            if type(dict_to_validate[each]) == int:
                res = int_validator(dict_to_validate[each])
                if res == False:    
                    result.append(each)
            if type(dict_to_validate[each]) == float:
                res = float_validator(dict_to_validate[each])
                if res == False:    
                    result.append(each)
            if type(dict_to_validate[each]) == bool:
                res = boolean_validator(dict_to_validate[each])
                if res == False:
                    result.append(res)
        else :
            if rules[each][0] == "str":
                data_type, min_length, max_length = rules[each]
                res = string_validator(dict_to_validate[each], data_type, min_length, max_length)
                if res == False:    
                    result.append(each)
            if rules[each][0] == "int":
                data_type, min_value, max_value = rules[each]
                res = int_validator(dict_to_validate[each], data_type, min_value, max_value)
                if res == False:    
                    result.append(each)
            if rules[each][0] == "float":
                data_type, min_value, max_value = rules[each]
                res = float_validator(dict_to_validate[each], data_type, min_value, max_value)
                if res == False:    
                    result.append(each)
            
    if not result:
        return True
    else:
        return False
        
validated = validate_generic_data(dict_to_validate, rules)
if validated:
    print("True: The data are validated")
else :
    for item in result:
        print(item + " doesnot follow the validation rule")


# In[ ]:




