from Question1 import answer_one

def answer_six():
    df = answer_one()
    print(df)

    return (df.index[df['% Renewable'] == df['% Renewable'].max()].tolist()[0], df['% Renewable'].max())

if __name__ == "__main__":
    print(answer_six())