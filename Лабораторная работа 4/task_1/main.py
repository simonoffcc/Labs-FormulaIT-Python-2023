import json


# TODO решите задачу
def task(json_file_path: str) -> float:
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except:
        raise FileNotFoundError(f"File {json_file_path} is not found.")

    sum_of_products = sum(entry["score"] * entry["weight"] for entry in data)
    result = round(sum_of_products, 3)
    return result


print(task("input.json"))
