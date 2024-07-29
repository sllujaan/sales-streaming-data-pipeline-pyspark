import numpy as np
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import uuid
from pathlib import Path

fake = Faker()

products_df = pd.read_csv("random_product_names_with_id.csv")
def product_name():
    return products_df['Product Name'][np.random.randint(0,len(products_df))]


def generate_new_sales(num_rows: int, dir: str):
    _uuid = str(uuid.uuid1())
    df = pd.DataFrame(
        [
            [
                i+1,
                np.random.randint(1, num_rows),
                fake.name(),
                np.random.randint(15,60),
                fake.country(),
                np.random.randint(1, num_rows),
                product_name(),
                np.random.randint(4, 500),
                np.random.randint(1, 100),
                fake.date_between(2*timedelta(days=-365), timedelta())
            ]
            for i in range(num_rows)
        ],
        columns=[
            'order_id',
            'customer_id',
            'customer_name',
            'customer_age',
            'customer_country',
            'product_id',
            'product_name',
            'product_price',
            'product_quantity',
            'order_date'
        ]
    )
    df = df.sort_values(by='order_date', ascending=True)
    Path(f"datasets/{dir}").mkdir(parents=True, exist_ok=True)
    df.to_csv(f"datasets/{dir}/sales-{_uuid}.csv", index=False)