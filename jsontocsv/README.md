# JSON to CSV transformation
This is a solution to the stackoverflow question: [How to convert a JSON file to CSV using Python?](https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv)
The json in question is **https_tinyurl.com_ywe4bwua.json**.   
Execute:
```
python jsontocsv.py
```
A csv file **output.csv** will be created.  
Change line with f = open(<filename>) to read another JSON.

## Output Panda
Error with differentvaluelength.json
Error with flatbitcoin.json
Converted covidsample.json to CSV (wrongly filled single values to all rows)
Error with simplesample1.json
Converted https_tinyurl.com_ywe4bwua.json to CSV (nested json objects are handled like a string value, no flatttening)
Converted samevaluelength.json to CSV (all correctly converted)
Converted panda_sample.json to CSV (all correctly converted)
Error with simplesample2.json

### Concluseion
Panda cannot convert out of the box most of the JSON files.
One converted file is wrong because Pandas filled up single values to all rows.
The JSON files need to have a certain structure to be converted correctly.

## Output own solution




