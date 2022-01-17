import Question1 as q

def answer_four():
    df = q.answer_one().reset_index()
    avgGDP = df[[str(x) for x in range(2006, 2016)]]
    avgGDP['avgGDP'] = avgGDP.mean(axis=1)
    avgGDP.sort_values('avgGDP', ascending=False, inplace=True)
    change = avgGDP.iloc[5]['2015']-avgGDP.iloc[5]['2006']
    return change


if __name__ == "__main__":
    print(answer_four())