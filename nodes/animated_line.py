
import matplotlib.pyplot as plt

class AnimatedLine:
    def __init__(self, window_name='bodypart', line_color='k'):
        fig, ax = plt.subplots(1,1)
        fig.canvas.set_window_title(window_name)

        ax.set_xlabel('Frame')
        ax.set_ylabel(window_name)

        self.line = ax.plot(0, 0, color=line_color)

    def update_line(self, x, y):
        self.line.set_data(x, y)



#if __name__ == '__main__':
    #main = FileImport()