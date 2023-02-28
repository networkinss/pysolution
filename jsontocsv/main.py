from Util import Util
from jsontocsv import custom_solution
from pandaway import panda_read_json_file

if __name__ == "__main__":

    util = Util("./inputjson")
    list = util.readAllFiles()
    print("Files in inputjson folder:")
    for file in list:
        print(file)

    print()
    print("Now starting with Panda way of converting JSON to CSV")
    panda_read_json_file(list, "inputjson", "outputpanda")

    print()
    print("Now starting with custom solution of JSON to CSV conversion.")
    custom_solution(list)

    print("Done")




