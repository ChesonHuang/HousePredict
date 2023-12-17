import requests
import numpy as np


def get_house_data():
    """
    从网络链接中获取房价数据
    网络链接地址为：https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data
    :return:
    """
    data_url = r'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
    req = requests.get(data_url)
    if req.status_code == 200:
        house_data = req.content.decode('utf-8')
        return house_data


if __name__ == "__main__":
    house_data = get_house_data()
    array = np.array(house_data)
    print(array)