"""
Project name:cubes
Author:Adhanet Gebretensay
Purpose:Plotting Cubic Numbers
starter code:
Date:11/22/2026



"""
import matplotlib.pyplot as plt

def plot_cubes( ):

    # part 1: first 5cubes

    values = [1, 2, 3, 4, 5]
    cubes = [1, 8, 27, 64, 125]
    plt.figure()
    plt.plot(values, cubes)
    plt.title("First 5 Cubes")
    plt.xlabel(" Values")
    plt.ylabel("Cubes")
    plt.savefig("Cubes_5.png")
    plt.show()


    # Part 2: First 5000 Cubes
    values = list(range(1, 5001))
    cubes = [x**3 for x in values]
    plt.figure()
    plt.plot(values, cubes)
    plt.title("First 5000 Cubes")
    plt.xlabel(" Values")
    plt.ylabel("Cubes")
    plt.savefig("Cubes_5000.png")
    plt.show()


if __name__=="__main__":
    plot_cubes()