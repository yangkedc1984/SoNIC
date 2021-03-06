import subprocess
import numpy as np
import pandas as pd

if __name__ == '__main__':
    cl_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    pmin = "0.5"
    tasks = [
        ["python", "simusimu.py", '100', str(cl_num), '1', '200', pmin] for cl_num in cl_nums
    ]
    procs = [subprocess.Popen(task) for task in tasks]
    for i, proc in enumerate(procs):
        out, err = proc.communicate()
        if err is not None:
            print("ERROR for TASK {}".format(" ".join(tasks[i])))
            print(err)

    data = []
    for cl_num in cl_nums:
        data.append(pd.read_csv("simu_n100k{}s1T200.csv".format(cl_num)))

        ############################
        #
        # lambda graphs
        #
        #
    if False:
        for i, cl_num in enumerate(cl_nums):
            plt.plot(data[i]['alpha'] / sqrt(log(cl_num) / 200), np.array(data[i]['theta_diff']),label=str(cl_num))
        plt.savefig('alpha_loss.png', dpi=1000)
        #plt.show()
        plt.clf()

    ############################
    #
    #
    # loss with best lambda
    #
    #
    if False:
        theta_min_diffs = []
        for i, cl_num in enumerate(cl_nums):
            theta_min_diffs.append(np.min(data[i]['theta_diff']))
            
        plt.plot(cl_nums, theta_min_diffs)
        plt.savefig('n_loss.png', dpi=1000)
        #plt.show()
        plt.clf()

    ############################
    #
    #
    # cluster distances
    #
    #
    if False:
        plt.plot(data[5]['alpha'], data[5]['cl_diff'])
        plt.savefig('cl_diff.png', dpi=1000)
        #plt.show()
        plt.clf()

