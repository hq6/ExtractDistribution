
import matplotlib.pyplot as plt

def plot_cdf(cdf):
    numbers = [x[0] for x in cdf]
    fractions =  [x[1] for x in cdf]
    plt.plot(numbers, fractions)
    plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
