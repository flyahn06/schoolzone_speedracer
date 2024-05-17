import glob

real_height = {
    "ahndonggi": 167,
    "choijemo": 181,
    "jooyunjae": 175,
    "kimminsung": 179,
    "leesungryeol": 176,
    "shinjunghoon": 176,
    "shinwoojin": 170,
    "kimyosap": 188
}

data = {

}

files = glob.glob("./result/*.csv")

for file in files:
    if "integrated" in file or "multi" in file:
        continue

    with open(file, 'r') as f:
        name = file.split("/")[-1][:-4]
        datum = list(map(lambda x: x.strip().split(","), f.readlines()))
        data[name] = datum


with open("integrated.csv", 'w') as f:
    for name, datum in data.items():
        for x, y, h in datum:
            f.write("{},{},{}\n".format(y, h, real_height[name]))