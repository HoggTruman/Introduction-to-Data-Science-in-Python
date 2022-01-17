from Question1 import answer_one

def answer_five():
    df = answer_one()
    print(df)

    return df['Energy Supply per Capita'].mean()

if __name__ == "__main__":
    print(answer_five())