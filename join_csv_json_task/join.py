import csv
import json

import pandas as pd


def create_csv(csv_data: dict, csv_filepath: str) -> None:
    with open(csv_filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_data.keys())
        writer.writerows(zip(*csv_data.values()))

        # Или с использованием pandas
        # df = pd.DataFrame(csv_data)
        # df.to_csv(f, index=False)


def create_json(json_data: dict, json_filepath: str) -> None:
    with open(json_filepath, 'w') as f:
        json.dump(json_data, f)


def join(product_csv_filepath: str, sale_json_filepath: str) -> None:
    with open(product_csv_filepath, 'r') as f:
        product_df = pd.read_csv(f)

    with open(sale_json_filepath, 'r') as f:
        sale_df = pd.read_json(f)

    product_sale_df = product_df.merge(sale_df, how='outer', on='product_id')
    print(product_sale_df)


def main():
    data_to_csv = {'product_id': list(range(1, 5)),
                   'product_name': ['Apple', 'Peach', 'Strawberry', 'Potato']}
    create_csv(csv_data=data_to_csv, csv_filepath='product_csv_data.csv')

    data_to_json = {'sale_id': list(range(100, 106)),
                    'product_id': [1, 2, 4, 4, 1, 4],
                    'amount': [2, 1, 10, 7, 1, 3]}
    create_json(json_data=data_to_json, json_filepath='sale_json_data.json')

    join(product_csv_filepath='product_csv_data.csv', sale_json_filepath='sale_json_data.json')


main()
