import requests
from bs4 import BeautifulSoup

def extract_property_combinations(url: str):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # プロパティの組み合わせを格納するリスト
    combinations = []

    # 例として、aタグのhrefにjsonファイルのパスが含まれていると仮定し抽出
    for a in soup.find_all('a', href=True):
        href = a['href']
        value = a.get_text(strip=True)
        if href.endswith('.html'):
            # htmlファイル名からプロパティ名を抽出（例: Charge capacity-Voltage.html）
            filename = href.split('/')[-1]
            if '-' in filename:
                prop_x, prop_y_ext = filename.split('-', 1)
                prop_y = prop_y_ext.rsplit('.', 1)[0]
                size = value.split('(')[-1].split(')')[0]
                combinations.append((prop_x, prop_y, size))

    return combinations

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/starrydata/starry-visualization/refs/heads/main/all_curves/index.html"
    combos = extract_property_combinations(url)
    for c in combos:
        print(f"prop_x: {c[0]}, prop_y: {c[1]}, size: {c[2]}")


