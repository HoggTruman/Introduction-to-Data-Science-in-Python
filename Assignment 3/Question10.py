from Question1 import answer_one


def answer_ten():
    df = answer_one()

    med = df['% Renewable'].median()
    df['HighRenew'] = df['% Renewable'] < med
    df['HighRenew'] = df['HighRenew'].apply(lambda x: 0 if x else 1)

    return df['HighRenew']


if __name__ == "__main__":
    print(answer_ten())
