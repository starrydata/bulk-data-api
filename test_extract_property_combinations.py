import pytest
import os
from unittest.mock import patch, Mock
from src.extract_property_combinations import extract_property_combinations

def load_test_html():
    test_html_path = os.path.join(os.path.dirname(__file__), 'test_data', 'fixtures', 'xy_combination_list.html')
    with open(test_html_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_expected_results():
    expected_path = os.path.join(os.path.dirname(__file__), 'test_data', 'results', 'xy_combination_result.csv')
    expected = []
    with open(expected_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                expected.append((parts[0], parts[1], parts[2]))
    return expected

@patch('src.extract_property_combinations.requests.get')
def test_extract_property_combinations(mock_get):
    # モックのレスポンスを設定
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = load_test_html()
    mock_get.return_value = mock_response

    # 関数実行
    url = "http://dummy-url-for-test"
    result = extract_property_combinations(url)

    # 期待結果の読み込み
    expected = load_expected_results()

    # resultのサイズは期待結果と同じ
    assert len(result) == len(expected)

    # 各要素の比較（sizeはintに変換して比較）
    for (rx, ry, rsize), (ex, ey, esize) in zip(result, expected):
        assert rx == ex
        assert ry == ey
        assert str(rsize) == esize
