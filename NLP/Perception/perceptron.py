# encoding: utf-8
from typing import List
import numpy as np
import logging

logger = logging.getLogger("perception")
logger.setLevel(logging.INFO)


class Perceptron(object):
    """感知机的简单实现"""

    def __init__(self, w=None, b=0.0, lr=0.1, max_iter=100):
        self.w = w
        self.b = b
        self.lr = lr
        self.max_iter = max_iter

    def train(self, x: [List], y: [int]):
        """

        :param x:[[1,0.1,3]]
        :param y: [-1/1]
        :return:
        """
        x = np.array(x)
        feature_dim = x.shape[1]
        y = np.array(y)

        if not self.w:
            self.w = np.ones(feature_dim)

        iter_num = 0
        all_fitted = False
        while iter_num <= self.max_iter or not all_fitted:
            neg_grad, yi = self.check_all_fitted(x, y)
            if neg_grad is None:
                return True
            self.w += neg_grad * self.lr
            self.b += yi * self.lr
        if not all_fitted:
            logger.warning("数据集线性不可分或者迭代次数太少")
            return False

    def perdict(self, a_x):
        """
`
        :param a_x: [0.1,100,2121]
        :return:
        """
        cal_res = np.dot(np.array(a_x), self.w) + self.b
        print("计算结果是{}".format(cal_res))
        return [1 if cal_res >= 0 else -1]

    def check_all_fitted(self, x, y):
        for a_x, a_y in zip(x, y):
            if (np.dot(a_x, self.w) + self.b) * a_y < 0:
                logger.info("sample: x<{}>; y<{}> not fitted".format(a_x, a_y))
                return a_y * a_x, a_y

        logger.info("All fitted...w: {}, b: {}".format(self.w, self.b))
        return None, None


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    x = [[3, 3], [4, 4], [1, 1]]

    y = [1, 1, -1]

    a_x = [0, 1]

    pct = Perceptron()
    training_status = pct.train(x,y)
    print(training_status)

    res = pct.perdict(a_x)
    print(res)