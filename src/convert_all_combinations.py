import os
from extract_property_combinations import extract_property_combinations
from convert_units import convert_units_in_json
import units_config

import os
import tempfile
import requests
from extract_property_combinations import extract_property_combinations
from convert_units import convert_units_in_json
import units_config

def main():
    url = "https://raw.githubusercontent.com/starrydata/starry-visualization/refs/heads/main/all_curves/index.html"
    combinations = extract_property_combinations(url)

    input_dir = "test_data"
    output_dir = "dist/v1"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for prop_x, prop_y, size in combinations:
        output_filename = f"{prop_x}-{prop_y}.json"
        output_path = os.path.join(output_dir, output_filename)

        # URLからjsonを取得して一時ファイルに保存し変換
        json_url = f"https://visualizer.starrydata.org/all_curves/json/{prop_x}-{prop_y}.json"
        print(f"Fetching {json_url}")
        response = requests.get(json_url)
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=True) as tmp_file:
                tmp_file.write(response.text)
                tmp_file.flush()
                convert_units_in_json(tmp_file.name, output_path, units_config.UNIT_CONVERSIONS)
        else:
            print(f"Failed to fetch {json_url} with status code {response.status_code}")

    # graph_list.jsonの生成
    graph_list = []
    for prop_x, prop_y, size in combinations:
        graph_list.append({"prop_x": prop_x, "prop_y": prop_y, "count": size})
    graph_list_json = {
        "graphs": graph_list,
        "total": len(graph_list)
    }
    with open(os.path.join(output_dir, "graph_list.json"), "w", encoding="utf-8") as f:
        import json
        json.dump(graph_list_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
