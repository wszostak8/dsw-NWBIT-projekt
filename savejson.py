import json

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Zapisano dane do pliku JSON: {file_path}")
    except Exception as e:
        print(f"Błąd w zapisywaniu danych do pliku JSON: {e}")

if __name__ == "__main__":
    data = {"example_key": "example_value"}
    output_file = 'output.json'
    save_json(data, output_file)
