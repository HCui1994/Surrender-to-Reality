import numpy as np
import matplotlib.pyplot as plt

class CellularAutomata:

    def __init__(self, cells_shape):
        """
        Args:
            cells_shape: (int, int) 画布大小
        """
        self.cells = np.zeros(cells_shape)  # 初始化画布
        real_width, real_height = cells_shape[0] - 2, cells_shape[1] - 2
        # self.cells[1:-1, 1:-1] = np.random.randint(2, size=(real_width, real_height))
        self.cells[[1, 15, -2], :] = 1
        self.cells[:, [1, 15, -2]] = 1
        self.timer = 0
        self.mask = np.ones((3, 3))
        self.mask[1, 1] = 0

    def update_state(self):
        buffer = np.zeros(self.cells.shape)
        cells = self.cells
        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[1] - 1):
                # 在画布的有效范围内计算
                neighbour = cells[i - 1 : i + 2, j - 1 : j + 2] # 获取 cells[i, j] 的 8-邻域
                neighbour_count = np.sum(self.mask * neighbour)
                if neighbour_count == 3:
                    buffer[i, j] = 1
                elif neighbour_count == 2:
                    buffer[i, j] = cells[i, j]
                else:
                    buffer[i, j] = 0
        self.cells = buffer
        # self._ca_conv(self.cells, self.mask)
        self.timer += 1
    
    def _ca_conv(self, cells, kernel):
        cells_w, cells_h = cells.shape
        # ks = (kl-1)/2 ## kernels usually square with odd number of rows/columns
        # kl = len(kernel)
        for i in range(1, cells_h - 1):
            for j in range(1, cells_w - 1):
                acc = 0
                for ki in range(3): ##kernel is the matrix to be used
                    for kj in range(3):
                        # if 0 <= i-ks <= kl: ## make sure you don't get out of bound error
                        acc += (cells[i - 1 + ki][j - 1 + kj] * kernel[ki][kj]) 
                if acc == 3:
                    cells[i, j] = 1
                elif acc == 2:
                    continue
                else:
                    cells[i, j] = 0


    def plot(self):
        plt.title("Iter: {}".format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def update_and_plot(self, n_iter):
        plt.ion()
        for _ in range(n_iter):
            plt.title('Iter :{}'.format(self.timer))
            plt.imshow(self.cells)
            self.update_state()
            plt.pause(0.2)
        plt.ioff()


CellularAutomata((31, 31)).update_and_plot(200)