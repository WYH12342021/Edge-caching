import numpy as np
from matplotlib import pyplot as plt


def plot_result(filepath, name, type):
    with open(filepath, "r") as file:
        lines = file.readlines()
    print("数据读取成功", filepath)
    data = []
    for line in lines:
        line = line.strip()
        if line:
            values = np.fromstring(line[1:-1], sep=', ')
            data.append(values)
    x = np.arange(len(data[0]))
    for i in range(len(data)):
        if i == 0:
            plt.plot(x, data[i], linewidth=1.5, color='red')
        elif i == 1:
            plt.plot(x, data[i], linewidth=1.5, color='blue')
        else:
            plt.plot(x, data[i], linewidth=1.5, color='green')
    plt.xlabel('episodes', fontsize=11)
    plt.ylabel(type, fontsize=11)
    plt.yticks(size=12)
    plt.xticks(size=12)
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.legend(fontsize=11)
    plt.tight_layout()
    print(str("./"+type+"/" + name))
    plt.savefig("../Draw/"+type+"/" + name + ".png", dpi=1000)
    plt.show()


# capacity = 4
# deadline = 15
# str1 = "cap_" + str(capacity)
# str2 = "_dead_" + str(deadline)
# str3 = str1 + str2
# # 调用函数并传入文件名
# plot_result(filepath='../run_this/data/cap_4_dead_15all_hitrate.txt', type='All Hit Rate', name=str3)
