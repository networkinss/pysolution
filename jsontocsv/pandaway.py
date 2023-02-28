import pandas as pd


def panda_read_json_file(file_list, inputfolder, outputfolder):
    for file in file_list:
        try:
            df = pd.read_json(inputfolder + "/" + file)
            df.to_csv(outputfolder + "/" + file + ".csv", index=False, encoding='utf-8')
            print("Converted " + file + " to CSV")
        except:
            print("Error with " + file)



