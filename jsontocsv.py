import json
import pandas as pd


def process_value(keys, value, flattened):
    if isinstance(value, dict):
        for key in value.keys():
            process_value(keys + [key], value[key], flattened)
    elif isinstance(value, list):
        for idx, v in enumerate(value):
            process_value(keys, v, flattened)
            # process_value(keys + [str(idx)], v, flattened)

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
    if not isinstance(json, dict):
        print("JSON object must be a dict instance, but is type " + str(type(json)))
        return flattened_result
    for key in json.keys():
        process_value([key], json[key], flattened_result)
    return flattened_result


def same_length(flattened: dict):
    max = 0
    for key in flattened.keys():
        if isinstance(flattened[key], list):
            if len(flattened[key]) > max:
                max = len(flattened[key])
    # print("Max length: " + str(max))
    for key in flattened.keys():
        if isinstance(flattened[key], list):
            if len(flattened[key]) < max:
                for i in range(max - len(flattened[key])):
                    flattened[key].append(None)
    return flattened


try:
    f = open("input.json", "r")
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file")
    exit(1)
y = json.loads(f.read())
flat = flatten_json(y)
equallength = same_length(flat)
df = pd.DataFrame.from_dict(equallength, orient='columns')
# df = pd.DataFrame.from_dict(flat, orient='columns')
df.to_csv('output.csv', index=False, encoding='utf-8')





