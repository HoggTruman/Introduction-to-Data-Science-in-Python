from Question1 import answer_one

def answer_seven():
    df = answer_one()
    df['rat'] = df['Self-citations']/df['Citations']

    return df.index[df['rat'] == df['rat'].max()].tolist()[0], df['rat'].max()

if __name__ == "__main__":
    print(answer_seven())