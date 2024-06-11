import sys

def check_parsing_results(results_file):
    with open(results_file, 'r') as file:
        content = file.read()
    if "Parsing failed" in content:
        print("Parsing failed.")
        sys.exit(1)
    else:
        print("Parsing successful.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_parsing_results.py <results_file>")
        sys.exit(1)
    results_file = sys.argv[1]
    check_parsing_results(results_file)
