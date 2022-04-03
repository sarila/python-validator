#!/usr/bin/env python
# coding: utf-8

# In[20]:


dict_to_validate = {"name": "Sarila Ngakhusi", "address": "Chyamasingh, Bhaktapur", "age": 20, "score": 95.6,  "covid": False}
# rules={}
# rules = {
#     "name": {"data_type": "str", "min_length": 6, "max_length": 15},
#     "address": {"data_type": "str", "min_length": 10, "max_length": 50}, 
#     "age" : {"data_type": "int", "min_value": 18, "max_value": 40}, 
#     "score" : {"data_type": "float", "min_value": 40}
# }
rules = { 
    "age" : {"data_type": "int", "min_value": 18, "max_value": 40}, 
    "score" : {"data_type": "float", "min_value": 40}
}
result = []
def string_validator(string_to_validate, rules):
#     print(rules)
    if isinstance(string_to_validate, str) :
        string_length = len(string_to_validate)
        if "min_length"in rules and "max_length" in rules:
            if string_length >= rules["min_length"] and string_length <= rules["max_length"]:
                return True
            else:
                return False
        elif "min_length" in rules:
            if string_length >= rules["min_length"]:
                return True
            else: 
                return False
        elif "max_length" in rules:
            if string_length <= rules["max_length"]:
                return True
            else: 
                return False
        else:
            return True
    else: 
        print(f"{string_to_validate} must be string")
        return False
    
def int_validator(number_to_validate, rules):
    if isinstance(number_to_validate, int):
        if "min_value"in rules and "max_value" in rules:
            if number_to_validate >= rules["min_value"] and number_to_validate <= rules["max_value"]:
                return True
            else:
                return False
        elif "min_value" in rules:
            if number_to_validate >= rules["min_value"]:
                return True
            else: 
                return False
        elif "max_value" in rules:
            if number_to_validate <= rules["max_value"]:
                return True
            else: 
                return False
        else:
            return True
    else :
        print(f"{number_to_validate} must be integer")
        return False
    
def float_validator(number_to_validate, rules):
    if isinstance(number_to_validate, float):
        if "min_value"in rules and "max_value" in rules:
            if number_to_validate >= rules["min_value"] and number_to_validate <= rules["max_value"]:
                return True
            else:
                return False
        elif "min_value" in rules:
            if number_to_validate >= rules["min_value"]:
                return True
            else: 
                return False
        elif "max_value" in rules:
            if number_to_validate <= rules["max_value"]:
                return True
            else: 
                return False
        else:
            return True
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
                res = string_validator(dict_to_validate[each], rules)
                if res == False:    
                    result.append(each)
            if type(dict_to_validate[each]) == int:
                res = int_validator(dict_to_validate[each], rules)
                if res == False:    
                    result.append(each)
            if type(dict_to_validate[each]) == float:
                res = float_validator(dict_to_validate[each], rules)
                if res == False:    
                    result.append(each)
            if type(dict_to_validate[each]) == bool:
                res = boolean_validator(dict_to_validate[each])
                if res == False:
                    result.append(res)
        else :
            if rules[each]["data_type"] == "str":
                res = string_validator(dict_to_validate[each], rules[each])
                if res == False:    
                    result.append(each)
            if rules[each]["data_type"] == "int":
                item = rules[each]
                res = int_validator(dict_to_validate[each], rules[each])
                if res == False:    
                    result.append(each)
            if rules[each]["data_type"] == "float":
                res = float_validator(dict_to_validate[each], rules[each])
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




