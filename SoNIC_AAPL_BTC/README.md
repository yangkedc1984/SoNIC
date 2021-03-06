[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SoNIC_AAPL_BTC** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet:  SoNIC_AAPL_BTC   

Published in: SoNIC

Description: 'estimation of SoNIC model on AAPL and BTC sentiment weights'

Keywords:
- social network
- network autoregression
- clustering
- communities
- influencer
- central node
- sentiment analysis
- stocktwits
- adjacency matrix
- lasso
- greedy algorithm
- Apple
- Bitcoin

See also: 
- SoNIC_simulation_study

Author: Yegor Klochkov

Submitted: Mon, Jun 17 2019 by Yegor Klochkov
```

### PYTHON Code
```python

import read_data
import missing
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from alternating import matrix_competition

if __name__ == '__main__':
    tasks = [
        ('data/users_daily_timeseries_AAPL.csv', "results/theta_daily_AAPL.png")
        , ('data/users_BTC_timeseries_Daily.csv', "results/theta_daily_BTC.png")
    ]

    for task in tasks:
        data_path, save_path = task

        Y, deltas, names = read_data.read_stock_twits_user_sentiment(data_path, min_days=50, min_delta=0.5)
        N, tmax = np.shape(Y)
        print(N, tmax)

        D0 = missing.missing_var(Y[:, :-1], deltas)
        D1 = missing.missing_covar(Y[:, 1:], Y[:, :-1], deltas, deltas)

        # SET NUMBER OF CLUSTERS
        num_clusters = 10

        res = matrix_competition('DIRECT', 5, num_clusters, D0, D1, 0.05)
        theta_est, v_est, u_est, ind_est, loss = res.theta, res.v, res.u, res.index, res.loss

        lists = [[] for i in range(num_clusters)]
        for i in range(N):
            lists[res.index[i]].append(i)

        rearrange = []
        for j in range(num_clusters):
            rearrange += lists[j]
        theta_sort = theta_est[rearrange].T
        theta_sort = theta_sort[rearrange].T

        plt.figure()
        sns.set()
        ax = sns.heatmap(theta_sort, center=0, xticklabels=names[rearrange], yticklabels=names[rearrange], cmap="PiYG")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=-70, fontsize=5)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=5)
        #plt.show()
        plt.savefig(save_path, dpi=500)


```

automatically created on 2019-06-17