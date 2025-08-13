from skimage.metrics import mean_squared_error
import numpy as np

if __name__ == '__main__':
    y_current_data_point = np.array((100,95,50,60,40))
    y_prediction_data_point = np.array((100,100,50,60,40))
    value = mean_squared_error(y_current_data_point, y_prediction_data_point)
    print(value)
