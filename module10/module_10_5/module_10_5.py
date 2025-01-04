import time

from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, mode="r") as f:
        print(f"{name} is opened in process {__name__}")
        while True:
            s = f.readline()
            if s:
                all_data.append(s)
            else:
                print(f"{name} is finished, read {len(all_data)} lines")
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
print(filenames)

# Линейный вызов
# start = time.time()
# for filename in filenames:
#     read_info(filename)
# print(time.time() - start, "(линейный)")

# Многопроцессный
if __name__ == '__main__':
    start = time.time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    print(time.time() - start, "(многопроцессный)")
