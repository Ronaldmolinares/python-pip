import csv


def read_csv(path):
    with open(path, "r") as file_csv:
        content = csv.reader(file_csv, delimiter=",")

        header = next(content)
        # print(header)
        data = []

        for line in content:
            iterable = zip(header, line)
            # print(list(iterable))
            # print("::::::" * 5)
            # print(line)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)

        return data


def read_csv_2(path):
    with open(path, "r") as file_csv:
        content = csv.DictReader(file_csv, delimiter=",")
        return list(content)


if __name__ == "__main__":
    result = read_csv("./app/data.csv")
    print(result[0])
    print("::" * 15)
    result_2 = read_csv_2("./app/data.csv")
    print(result_2[0])