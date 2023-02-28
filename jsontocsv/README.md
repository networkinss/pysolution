# JSON to CSV transformation
This is a solution to the stackoverflow question: [How to convert a JSON file to CSV using Python?](https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv)
The json in question is **https_tinyurl.com_ywe4bwua.json**.    
I made a comparison with a simple soluton from Pandas.  
Execution of main.py will use both ways, take the input from **inputjson** folder.  
And write into two output folder: **outputpandas** and **outputcustomsolution**.  
You can put your own json files in the inputjson folder.  
```
python main.py
```


## Pandas simple solution

The output is produced by the pandaway.py script.
The script has been taken from this site:  
https://sparkbyexamples.com/pandas/python-pandas-convert-json-to-csv/

### Output Pandas solution

- Converted panda_sample1.json to CSV (all correctly converted)
- Converted panda_sample2.json to CSV (all correctly converted)
- Error with differentvaluelength.json
- Error with flatbitcoin.json
- Converted covidsample.json to CSV (wrongly filled single values to all rows)
- Converted simplesample1.json to CSV
- Error with simplesample2.json
- Converted https_tinyurl.com_ywe4bwua.json to CSV (nested json objects are handled like a string value, no flatttening)
- Converted samevaluelength.json to CSV (all correctly converted)

### Conclusion
Panda cannot convert out of the box most of the JSON files.  
One converted file is wrong because Pandas filled up single values to all rows.  
The JSON files need to have a certain structure to be converted correctly. 

## Output own solution
The customized solution is in the main.py script.

- Converted differentvaluelength.json to CSV
- Converted panda_sample2.json to CSV
- Converted flatbitcoin.json to CSV
- Converted covidsample.json to CSV
- Converted simplesample1.json to CSV
- Converted https_tinyurl.com_ywe4bwua.json to CSV
- Converted samevaluelength.json to CSV
- Converted panda_sample1.json to CSV
- Converted simplesample2.json to CSV

### Conclusion
The own solution can convert all JSON files correctly,   
and is more flexible than Pandas simple solution.  
However, also the ownn solution uses Pandas to convert the JSON to a DataFrame.  
But the dict object must be structured in a certain way to be converted correctly.  
Therefore several steps are needed:
* Flatten the json with recursion for nested objects
* Make all values in the dict a list
* And make all value lists the same length

After that preparation, the dict can be converted to a DataFrame wit Pandas.
And finally written into a CSV file.






