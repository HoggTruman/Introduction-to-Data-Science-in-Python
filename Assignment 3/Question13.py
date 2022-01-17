
from Question1 import answer_one

def answer_thirteen():
    df = answer_one()
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    return df['PopEst'].apply(lambda x: '{0:,}'.format(x)).astype(str)


if __name__ == "__main__":
    print(answer_thirteen())
