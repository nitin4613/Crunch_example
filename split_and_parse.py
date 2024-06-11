import sys
import xml.etree.ElementTree as ET

def split_and_parse(junit_file):
    try:
        with open(junit_file, 'r') as file:
            xml_content = file.read()
        root = ET.fromstring(xml_content)
        # Simulate test splitting logic here
        # For simplicity, we'll just print out the root tag
        print(f"Root tag: {root.tag}")
        with open("/workspace/parsed_results", 'w') as result_file:
            result_file.write("Parsing successful\n")
    except ET.ParseError as e:
        with open("/workspace/parsed_results", 'w') as result_file:
            result_file.write(f"Parsing failed: {str(e)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_and_parse.py <junit.xml>")
        sys.exit(1)
    junit_file = sys.argv[1]
    split_and_parse(junit_file)
