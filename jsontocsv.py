import json
import pandas as pd


def same_length(flattened: dict):
    max = 0
    for key in flattened.keys():
        if isinstance(flattened[key], list):
            if len(flattened[key]) > max:
                max = len(flattened[key])
    for key in flattened.keys():
        if isinstance(flattened[key], list):
            if len(flattened[key]) < max:
                for i in range(max - len(flattened[key])):
                    flattened[key].append(None)
    return flattened


def process_value(keys, value, flattened):
    if isinstance(value, dict):
        for key in value.keys():
            process_value(keys + [key], value[key], flattened)
    elif isinstance(value, list):
        for idx, v in enumerate(value):
            process_value(keys, v, flattened)
    else:
        jkey = '__'.join(keys)
        if not flattened.get(jkey) is None:
            if isinstance(flattened[jkey], list):
                flattened[jkey] = flattened[jkey] + [value]
            else:
                flattened[jkey] = [flattened[jkey]] + [value]
        else:
            flattened[jkey] = value


def flatten_json(json):
    flattened_result = {}
    json_list = []
    if isinstance(json, dict):
        json_list.append(json)
    elif isinstance(json, list):
        json_list = json
    else:
        print("JSON object must be a dict or list instance, but is type " + str(type(json)))
        return {}
    for j in json_list:
        for key in j.keys():
            process_value([key], j[key], flattened_result)
    return flattened_result


try:
    f = open("https_tinyurl.com_ywe4bwua.json", "r")
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file")
    exit(1)
y = json.loads(f.read())
flat = flatten_json(y)
df = pd.DataFrame.from_dict(same_length(flat), orient='columns')
df.to_csv('output.csv', index=False, encoding='utf-8')





