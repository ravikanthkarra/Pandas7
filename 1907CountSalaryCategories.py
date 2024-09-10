import pandas as pd
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # sal_cat = ['Low Salary', 'Average Salary', 'High Salary']
    # sal_cat_df = pd.DataFrame(sal_cat, columns = ['category'])
    # accounts['category'] = 'Unknown'
    # accounts.loc[(accounts['income'] < 20000), 'category'] = 'Low Salary'
    # accounts.loc[(accounts['income'] >= 20000) & (accounts['income'] <= 50000), 'category'] = 'Average Salary'
    # accounts.loc[(accounts['income'] > 50000), 'category'] = 'High Salary'
    # df = sal_cat_df.merge(accounts, left_on = 'category', right_on = 'category', how = 'left')
    # df = df.groupby(['category'])['account_id'].count().reset_index()

    # return df.rename(columns = {'account_id': 'accounts_count'})
    low_count = (accounts['income'] < 20000).sum()
    avg_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()
    print(high_count)
    result = [['Low Salary', low_count], ['Average Salary', avg_count], ['High Salary', high_count]]
    return pd.DataFrame(result, columns=['category', 'accounts_count'])
