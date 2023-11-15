# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file_path, json_file_path) -> None:
    try:
        with open(csv_file_path, 'r') as csv_file:

            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)

    except FileNotFoundError:
        raise FileNotFoundError(f"File {csv_file_path} is not found.")


if __name__ == '__main__':
    task(INPUT_FILENAME, OUTPUT_FILENAME)
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
