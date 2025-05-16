import os
from extract_property_combinations import extract_property_combinations
from convert_units import convert_units_in_json
import units_config

def main():
    url = "https://raw.githubusercontent.com/starrydata/starry-visualization/refs/heads/main/all_curves/index.html"
    combinations = extract_property_combinations(url)

    input_dir = "test_data"
    output_dir = "dist"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for prop_x, prop_y, size in combinations:
        input_filename = f"{prop_x} {prop_y}.json"
        input_path = os.path.join(input_dir, input_filename)
        output_filename = f"{prop_x} {prop_y}.json"
        output_path = os.path.join(output_dir, output_filename)

        if os.path.exists(input_path):
            print(f"Converting {input_path} -> {output_path}")
            convert_units_in_json(input_path, output_path, units_config.UNIT_CONVERSIONS)
        else:
            print(f"Input file not found: {input_path}")

if __name__ == "__main__":
    main()
