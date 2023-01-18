from tkinter import filedialog
import pandas as pd

def getFilePath():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(
            ("excel", "*.xlsx"),
            ("csv", "*.csv"),
            ("all files", "*.*")
        )
    )
    runData(file_path)
    return 0

def runData(file_path):
    if file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        print(df)
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        print(df)
    else:
        print("File not found")
        return 1
    return 0