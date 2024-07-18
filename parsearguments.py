import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program - projekt')
    parser.add_argument('--input', type=str, help='Ścieżka do pliku wejściowego JSON', required=True)
    parser.add_argument('--output', type=str, help='Ścieżka do pliku wyjściowego JSON', required=True)
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        print("\033[91mBłąd: Musisz podać nazwę pliku wejściowego i wyjściowego.\033[0m") 
    
    args = parser.parse_args()
    return args
