import sys
import pandas as pd
import json
import pathlib
import shutil

labtainer_instructor_path = pathlib.Path().resolve()
print(labtainer_instructor_path)

labtainer_xfer_path = "/home/student/labtainer_xfer"
foldername = sys.argv[1]
file_grade_name = f"{foldername}.grades.json"
file_grade_path = f"{labtainer_xfer_path}/{foldername}/{file_grade_name}"
file_csv_source = f"{labtainer_instructor_path}/{file_grade_name}.csv"
file_csv_des = f"{labtainer_xfer_path}/{foldername}/{file_grade_name}.csv"

f = open(file_grade_path)
data_dict = json.load(f)

new_rows = []

for i in data_dict:
    one_row = {}
    email_data = i
    taskValues = data_dict[i]["grades"].values()
    taskValuesList = list(taskValues)
    taskKey = data_dict[i]["grades"].keys()
    taskKeyList = list(taskKey)
    one_row['email'] = i
    for k in range(len(taskValuesList)):
        one_row[taskKeyList[k]] = taskValuesList[k]
    totalTask = len(taskValues)
    numsCorrect = sum(value == True for value in taskValues)
    one_row['score'] = f"{numsCorrect}/{totalTask}"
    new_rows.append(one_row)

df = pd.DataFrame.from_dict(new_rows)
df.to_csv(f"{file_grade_name}.csv")

shutil.move(file_csv_source, file_csv_des)
print(df)
f.close()