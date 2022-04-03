#!/usr/bin/env python
# coding: utf-8

# In[58]:


dict_to_validate = {"name": "Sarila Ngakhusi", "address": "Chyamasingh, Bhaktapur", "age": 20, "score": 95.6,  "covid": False}
# dict_to_validate = {}
# rules={}
# rules = {
#     "name": {"data_type": "str", "min": 6, "max": 15},
#     "address": {"data_type": "str", "min": 10, "max": 50}, 
#     "age" : {"data_type": "int", "min": 18, "max": 40}, 
#     "score" : {"data_type": "float", "min": 40}
# }
rules = { 
    "age" : {"data_type": "int", "min": 18, "max": 40}, 
    "score" : {"data_type": "float", "min": 40},
#     "height": {"data_type": "float", "min": 5}
}
result = []
def validation_logic(item_to_validate, rules) :
    if "min"in rules and "max" in rules:
        if item_to_validate >= rules["min"] and item_to_validate <= rules["max"]:
                return True
        else:
            return False
    elif "min" in rules:
        if item_to_validate >= rules["min"]:
            return True
        else: 
            return False
    elif "max" in rules:
        if item_to_validate <= rules["max"]:
            return True
        else: 
            return False
    else:
        return True
def validator(item_to_validate, rules):
#     print(rules)
#     if is string
    if rules["data_type"] == "str":
        
        if isinstance(item_to_validate, str) :
            item_to_validate = len(item_to_validate)
            validation_logic(item_to_validate, rules)
        else: 
            print(f"{item_to_validate} must be string")
            return False
    elif rules["data_type"] == "int":
#     if the number is integer
        if isinstance(item_to_validate, int):
            validation_logic(item_to_validate, rules)
        else :
            print(f"{item_to_validate} must be integer")
            return False
    if rules["data_type"] == "float":
#     if float 
        if isinstance(item_to_validate, float):
            validation_logic(item_to_validate, rules)
        else:
            print(f"{item_to_validate} must be float")
            return False

def validate_generic_data(dict_to_validate, rules):
    for each in dict_to_validate:
        if each not in rules:
            res = validator(dict_to_validate, {"data_type": type(dict_to_validate[each])})
            if res == False:
                result.append(res)
        else :
            res = validator(dict_to_validate[each], rules[each])
            if res == False:    
                result.append(each)  
    if not result:
        return True
    else:
        return False

def equivalent_rules_dict(dict_to_validate, rules):
    if not dict_to_validate:
        print("Dictionary is empty: No values to validate")
    else:
        for each in rules:
            if each not in dict_to_validate:
                return False

        validated = validate_generic_data(dict_to_validate, rules)
        if validated:
            print("True: The data are validated")
        else :
            for item in result:
                print(item + " doesnot follow the validation rule")

rules_and_keys = equivalent_rules_dict(dict_to_validate, rules)
if rules_and_keys == False:
    print("All the rules are not associated with the keys in dictionary to be validated")


# In[ ]:





# In[ ]:




