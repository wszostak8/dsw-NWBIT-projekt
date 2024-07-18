import json

def load_json(file_path):
    if not file_path.endswith('.json'):
        print(f"Błąd: Plik '{file_path}' nie jest plikiem JSON.")
        return None
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Dane z JSON załadowane poprawnie z pliku: {file_path}")
            return data
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None
    except FileNotFoundError as e:
        print(f"Nie znaleziono pliku: {e}")
        return None

if __name__ == "__main__":
    input_file = 'projekt.json'
    data = load_json(input_file)
    if data:
        print("Dane załadowane: ", data)
