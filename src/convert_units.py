import json
from pint import UnitRegistry

def convert_units_in_json(input_path: str, output_path: str, unit_map: dict):
    """
    input_path: 入力jsonファイルパス
    output_path: 出力jsonファイルパス
    unit_map: 物理量名 -> 変換先単位の辞書
    """
    ureg = UnitRegistry()
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 元の単位
    original_unit_x = data.get('unit_x')
    original_unit_y = data.get('unit_y')

    # 変換先単位
    target_unit_x = unit_map.get(data.get('prop_x'), original_unit_x)
    target_unit_y = unit_map.get(data.get('prop_y'), original_unit_y)

    # 単位変換のためのpint Quantity作成
    # data['data']['x'], data['data']['y']はリストのリストなので、各値を変換
    def convert_values(values, from_unit, to_unit):
        if from_unit == to_unit:
            return values
        factor = (1 * ureg(from_unit)).to(to_unit).magnitude
        # 変換係数で一括変換
        return [[v * factor for v in sublist] for sublist in values]

    data['data']['x'] = convert_values(data['data']['x'], original_unit_x, target_unit_x)
    data['data']['y'] = convert_values(data['data']['y'], original_unit_y, target_unit_y)

    # unit_x, unit_yを更新
    data['unit_x'] = target_unit_x
    data['unit_y'] = target_unit_y

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    import units_config as units_config
    import sys
    if len(sys.argv) != 3:
        print("Usage: python src/convert_units.py input.json output.json")
        sys.exit(1)
    convert_units_in_json
    (sys.argv[1], sys.argv[2], units_config.UNIT_CONVERSIONS)
