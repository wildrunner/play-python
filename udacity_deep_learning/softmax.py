"""Softmax
N개의 값이 존재할때, 각 값의 편차를 확대시켜 큰 값을 상대적으로 더 크게 작은 값은 상대적으로 더 작게 만든 다음 Normalization 하는 함수

참고: http://nerve.tistory.com/160
"""
from math import exp
import numpy as np
import matplotlib.pyplot as plt

scores = [3.0, 1.0, 0.2]

def softmax(x):
    # sum = 0
    # for score in scores:
    #     sum += exp(score)
    #
    # result = []
    # for score in scores:
    #     result.append(exp(score) / sum)
    #
    # # return result
    # npsum = np.sum(np.exp(x), axis=0)
    # npexp = np.exp(x)
    # npresult = np.exp(x) / np.sum(np.exp(x), axis=0)

    return np.exp(x) / np.sum(np.exp(x), axis=0)




if __name__ == "__main__":
    print(softmax(scores))

    x = np.arange(-2.0, 6.0, 0.1)
    scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

    plt.plot(x, softmax(scores).T, linewidth=2)
    plt.show()