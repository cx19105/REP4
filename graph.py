from window import Window
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Graph:
    def __init__(self, data):
        self.lengths = data[0]
        self.aspect_ratios = data[1]
        self.number_of_cars = data[2]

    def create_graph(self):
        X = self.lengths
        Y = self.aspect_ratios
        Z = self.number_of_cars
        plotx,ploty, = np.meshgrid(np.linspace(np.min(X),np.max(X),100),\
                           np.linspace(np.min(Y),np.max(Y),100))
        plotz = interp.griddata((X,Y),Z,(plotx,ploty),method='linear')

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap='viridis')
        ax.set_title('Surface Plot')
        plt.show()

def get_data(min_length, max_length, min_aspect_ratio, max_aspect_ratio):
    number_of_cars = []
    lengths = []
    aspect_ratios = []
    for length in range(min_length, max_length, 50):
        for aspect_ratio in range(int(min_aspect_ratio*10), int(max_aspect_ratio*10)):
            window = Window(aspect_ratio/10, length)
            data = window.loop()
            number_of_cars.append(data[1])
            lengths.append(length)
            aspect_ratios.append(aspect_ratio/10)
    return [lengths, aspect_ratios, number_of_cars]

if __name__ == "__main__":
    data = get_data(100, 1000, 0.2, 3)
    graph = Graph(data)
    graph.create_graph()
