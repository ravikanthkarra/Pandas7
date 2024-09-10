import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    imm = (delivery['order_date'] == delivery['customer_pref_delivery_date']).sum()
    result = (imm / len(delivery['delivery_id']) * 100).round(2)
    return pd.DataFrame([result], columns=['immediate_percentage'])
    # return delivery