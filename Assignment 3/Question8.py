from Question1 import answer_one

def answer_eight():
    df = answer_one()
    df['pop'] = df['Energy Supply']/df['Energy Supply per Capita']
    df.sort_values('pop', ascending=False, inplace=True)

    return df.index[2]

if __name__ == "__main__":
    print(answer_eight())

