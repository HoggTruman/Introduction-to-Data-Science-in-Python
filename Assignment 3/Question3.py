import Question1 as q

def answer_three():
    df = q.answer_one()
    df = df[[str(x) for x in range(2006, 2016)]]
    df['avgGDP'] = df.mean(axis=1)
    avgGDP = df['avgGDP'].sort_values(ascending=False, axis=0)
    return avgGDP


if __name__ == "__main__":
    print(answer_three())