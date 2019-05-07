import json
import numpy as np
import cv2
import pickle
from keras import models
from keras import layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt

network=None


def jsonToImage (str):
    json_data = str
#对传进来的点缩放使其符合28*28
    python_obj = json.loads(json_data)
    x = python_obj["X"]
    y = python_obj["Y"]

    x_max = max(x)
    x_min = min(x)
    delta_x = x_max - x_min
    y_max = max(y)
    y_min = min(y)
    delta_y = y_max - y_min

    x = [int((t - x_min) / delta_x * 15) +5for t in x]#原15
    y = [int((t - y_min) / delta_y * 15) +5for t in y]
    img = np.zeros((28, 28, 3), np.uint8)#新建空图像


#用opencv进行绘制
    for t in range(len(x) - 1):
        cv2.line(img, (x[t], y[t]), (x[t + 1], y[t + 1]), (255, 255, 255), 1)

    #坐标系不同，翻转
    img = cv2.flip(img, 0, 0)
    #灰度化 高斯模糊
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
    img = cv2.GaussianBlur(img, (3, 3), 0)

    return img


def recongnition(img):
    # 获取训练好的网络
    global network
    if  network == None:
        with open('trainedData', 'rb') as f:
            network = pickle.load(f)
    #增加维度
    img = img.reshape((1, 28*28))
    y=network.predict(img)
    y=y[0]*np.array([0,1,2,3,4,5,6,7,8,9])
    return str(int(np.sum(y)))

def jsonRec(str):
    img=jsonToImage(str)
    plt.imshow(img)
    plt.show()
    return recongnition(img)





def test():
    str1 = '{"X":[552.0,532.0,483.0,473.0,455.0,440.0,433.0,431.0,434.0,440.0,462.0,519.0,564.0,603.0,630.0,650.0,659.0,661.0,657.0,652.0,631.0,615.0,596.0,570.0,539.0,511.0,487.0,461.0,442.0,429.0,423.0,423.0,423.0,424.0,424.0,425.0,428.0],"Y":[430.0,430.0,427.0,421.0,409.0,396.0,384.0,373.0,357.0,351.0,341.0,326.0,318.0,308.0,297.0,285.0,273.0,261.0,240.0,233.0,214.0,202.0,193.0,188.0,186.0,186.0,193.0,204.0,216.0,226.0,234.0,235.0,235.0,236.0,236.0,236.0,236.0]}'
    img = jsonToImage(str1)

    from keras.datasets import mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    img=test_images[0]
    img = jsonToImage(str1)

    plt.imshow(img)
    plt.show()
    y = recongnition(img)
    print(y)

    input()




if __name__=='__main__':
    test()