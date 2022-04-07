#!/usr/bin/env python
# coding: utf-8

# In[28]:


dict_to_validate = {"name": "Sarila Ngakhusi", "address": "Chyamasingh, Bhaktapur", "age": 20, "score": 95.6,  "covid": False}
# dict_to_validate = {}
# rules={}
rules = {
    "name": {"data_type": "str", "min": 6, "max": 15},
    "address": {"data_type": "str", "min": 10, "max": 50}, 
    "age" : {"data_type": "int", "min": 10, "max": 40}, 
#     "score" : {"data_type": "float", "min": 40},
#     "height" : {"data_type": "int", "min": 5},
}
# rules = { 
#     "age" : {"data_type": "int", "min": 18, "max": 40}, 
#     "score" : {"data_type": "float", "min": 40},
# #     "height": {"data_type": "float", "min": 5}
# }
result = []

# To compare the length of string and value of numberss
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
    
# Validates the data type of the data and calls validation logic
def validator(item_to_validate, rules):
#     print(rules)
#     if is string
    if rules["data_type"] == "str":
        
        if isinstance(item_to_validate, str) :
            item_to_validate = len(item_to_validate)
            return validation_logic(item_to_validate, rules)
        else: 
            print(f"{item_to_validate} must be string")
            return False
    elif rules["data_type"] == "int":
#     if the number is integer
        if isinstance(item_to_validate, int):
            return validation_logic(item_to_validate, rules)
        else :
            print(f"{item_to_validate} must be integer")
            return False
    if rules["data_type"] == "float":
#     if float 
        if isinstance(item_to_validate, float):
            return validation_logic(item_to_validate, rules)
        else :
            print(f"{item_to_validate} must be float")
            return False

# only validates the mentioned rules and ignores others
def validate_generic_data(dict_to_validate, rules):
    for each in rules:
        res = validator(dict_to_validate[each], rules[each])
        if res == False:    
            result.append(each)  
    if not result:
        return True
    else:
        return False

#checks if the rules consist of extra keys besides in data
def equivalent_rules_dict(dict_to_validate, rules):
    if not dict_to_validate:
        print("Dictionary is empty: No values to validate")
    else:
        set1 = set(list(rules.keys()))
        set2 = set(list(dict_to_validate.keys()))
        if set1.issubset(set2):
            validated = validate_generic_data(dict_to_validate, rules)
            if validated:
                print("True: The data are validated")
            else :
                for item in result:
                    print(item + " doesnot follow the validation rule")
        else :
            print("All the rules are not associated with the keys in dictionary to be validated")                


rules_and_keys = equivalent_rules_dict(dict_to_validate, rules)


# In[ ]:





# In[ ]:




