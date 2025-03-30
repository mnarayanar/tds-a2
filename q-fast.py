import csv
import json
from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

def csv_to_json(file_path: str) -> Dict[str, List[Dict[str, str]]]:
    students = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "studentId": int(row["studentId"]),
                "class": row["class"]
            })
    return {"students": students}

file_path = "./q-fastapi.csv"  # Ensure this file exists
json_output = csv_to_json(file_path)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"])

@app.get("/api")
def get_students(class_param: List[str] = Query(None, alias="class")):
    if class_param is None:
        return json_output  # Return all students if no class filter is applied
    
    filtered_students = [s for s in json_output["students"] if s["class"] in class_param]
    return {"students": filtered_students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
