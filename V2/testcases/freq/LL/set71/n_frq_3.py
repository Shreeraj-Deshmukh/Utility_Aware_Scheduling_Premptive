"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 25, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 25, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.074983, 'e_o_k': [0.145690, 0.116552, 0.093242, 0.074593, 0.059675, 0.047740], 'p_i': 10, 'u_i': 3.5232},
        {'id': 1, 'e_m': 0.207897, 'e_o_k': [0.057749, 0.046199], 'p_i': 20, 'u_i': 1.0606},
        {'id': 2, 'e_m': 0.505827, 'e_o_k': [0.085675, 0.068540, 0.054832, 0.043866], 'p_i': 40, 'u_i': 3.4010},
        {'id': 3, 'e_m': 11.981266, 'e_o_k': [1.623795, 1.299036, 1.039229, 0.831383, 0.665106, 0.532085], 'p_i': 80, 'u_i': 4.8241},
        {'id': 4, 'e_m': 0.627821, 'e_o_k': [0.106338, 0.085071, 0.068057, 0.054445], 'p_i': 40, 'u_i': 1.6455},
        {'id': 5, 'e_m': 3.196490, 'e_o_k': [0.541411, 0.433129, 0.346503, 0.277202], 'p_i': 40, 'u_i': 1.3745},
        {'id': 6, 'e_m': 0.856156, 'e_o_k': [0.175442, 0.140353, 0.112283], 'p_i': 40, 'u_i': 1.5038},
        {'id': 7, 'e_m': 0.053673, 'e_o_k': [0.010998, 0.008799, 0.007039], 'p_i': 20, 'u_i': 4.4242},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
