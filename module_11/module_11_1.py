import re

import matplotlib.pyplot as plt
import pandas as pd
import requests

html_content = requests.get("https://www.cbr.ru/hd_base/KeyRate/").text

pattern = r'"categories":\[(.*?)\],.*,"data":\[(.*?)\]'
match = re.search(pattern, html_content)

if match:
    dates_str = match.group(1).replace('"', '').split(',')
    key_rates_str = match.group(2).split(',')

    dates = pd.to_datetime(dates_str, format="%d.%m.%Y")
    key_rates = pd.to_numeric(key_rates_str)
    df = pd.DataFrame({"Date": dates, "KeyRate": key_rates})

    # оставляем только те строки, в которых значение ключевой ставки поменялось
    df = df[df["KeyRate"] != df["KeyRate"].shift()]  # отличается от предыдущей строки
    print(df)

    plt.clf()
    plt.plot(df["Date"], df["KeyRate"], marker='o')
    plt.title("Ключевая ставка ЦБР")
    plt.xlabel("Дата")
    plt.ylabel("Ключевая ставка (%)")
    plt.grid()
    plt.tight_layout()
    plt.show()
    plt.close()
else:
    print("Данные о ключевой ставке не найдены.")
