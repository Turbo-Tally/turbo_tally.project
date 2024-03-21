from cerberus import schema_registry
from datetime import datetime
from modules.common.locations import regions, provinces

###########################
# Default Datetime Format #
###########################
datetime_format = "%Y-%m-%d %H:%M:%S"

#####################
# Custom Validators #
#####################

formats = {}

# username validator
formats["username"] =  {
    "type" : "string", 
    "minlength" : 3, 
    "maxlength" : 20, 
    "regex" : 
        "^[A-Za-z0-9\.\-\_]+$"
}

# email validator 
formats["email"] = {
    "type" : "string", 
    "minlength" : 4, 
    "maxlength" : 320, 
    "regex" :   
        "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" 
}

# password validator  

formats["password"] = {
    "type" : "string", 
    "minlength" : 8, 
    "maxlength" : 255,
    "allof" : [
        { 
            "type" : "string", 
            "regex" : ".*[0-9].*"
        },
        { 
            "type" : "string", 
            "regex" : ".*[A-Z].*"
        },
        { 
            "type" : "string", 
            "regex" : ".*[a-z].*"
        },
        { 
            "type" : "string", 
            "regex" : 
                ".*" +
                "[\s/!/%22/#\%\&\'\(\)\*\+\'" +
                "\-\.\/\:\;\%3C\=\%3E\?\@\[\]\^\_\%" + 
                "\&\{\|\}\-]" +
                ".*"
        }
    ]
}

# datetime 
def check_datetime(field, value, error): 
    try: 
        datetime.strptime(value, datetime_format)
    except: 
        error(field, "Must be a valid datetime.") 


formats["datetime_str"] = {
    "type" : "string", 
    "check_with" : check_datetime
}

# gender 
formats["gender"] = {
    "type" : "string",
    "allowed" : ["M", "F"]
}

# regions 
formats["region"] = {
    "type" : "string", 
    "allowed" : list(map(lambda x: x["key"], regions))
}

# province 
formats["province"] = {
    "type" : "string", 
    "allowed" : list(map(lambda x: x["key"], provinces))
}

# PH mobile number 
formats["ph_mobile_no"] = {
    "type" : "string", 
    "minlength" : 11, 
    "maxlength" : 11, 
    "regex" : "09[0-9]{9}"
}

# verification code 
formats["verif_code"] = {
    "type" : "string", 
    "minlength" : 6, 
    "maxlength" : 6, 
    "regex" : "[0-9]{6}"
}


def extend_format(dict_a, dict_b): 
    return dict(dict_a, **dict_b)

def require_all(dict_a): 
    dict_b = {} 
    for key in dict_a:
        dict_b[key] = dict_a[key] 
        dict_b[key]["required"] = True
    return dict_b