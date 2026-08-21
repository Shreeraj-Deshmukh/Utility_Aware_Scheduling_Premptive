"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.721674, 'e_o_k': [0.107341, 0.085873, 0.068698, 0.054959, 0.043967], 'p_i': 10, 'u_i': 3.4325},
        {'id': 1, 'e_m': 2.496139, 'e_o_k': [0.693372, 0.554697], 'p_i': 20, 'u_i': 2.7085},
        {'id': 2, 'e_m': 0.886501, 'e_o_k': [0.181660, 0.145328, 0.116262], 'p_i': 40, 'u_i': 2.7857},
        {'id': 3, 'e_m': 2.410461, 'e_o_k': [0.408276, 0.326621, 0.261297, 0.209037], 'p_i': 80, 'u_i': 3.1834},
        {'id': 4, 'e_m': 2.948362, 'e_o_k': [0.438536, 0.350828, 0.280663, 0.224530, 0.179624], 'p_i': 40, 'u_i': 3.1028},
        {'id': 5, 'e_m': 4.596887, 'e_o_k': [1.276913, 1.021530], 'p_i': 80, 'u_i': 2.9295},
        {'id': 6, 'e_m': 0.004759, 'e_o_k': [0.000806, 0.000645, 0.000516, 0.000413], 'p_i': 40, 'u_i': 2.9225},
        {'id': 7, 'e_m': 0.388865, 'e_o_k': [0.079685, 0.063748, 0.050999], 'p_i': 20, 'u_i': 3.3922},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
