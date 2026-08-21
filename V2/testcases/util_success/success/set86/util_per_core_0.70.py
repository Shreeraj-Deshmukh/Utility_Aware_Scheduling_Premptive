"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439992, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439992, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.088178, 'e_o_k': [0.133792, 0.107034, 0.085627], 'p_i': 10, 'u_i': 2.6742},
        {'id': 1, 'e_m': 0.495426, 'e_o_k': [0.040286, 0.032229, 0.025783, 0.020627, 0.016501, 0.013201], 'p_i': 20, 'u_i': 1.0126},
        {'id': 2, 'e_m': 1.145842, 'e_o_k': [0.102259, 0.081807, 0.065445, 0.052356, 0.041885], 'p_i': 40, 'u_i': 1.6645},
        {'id': 3, 'e_m': 25.538739, 'e_o_k': [2.279159, 1.823327, 1.458662, 1.166930, 0.933544], 'p_i': 80, 'u_i': 1.3774},
        {'id': 4, 'e_m': 6.445748, 'e_o_k': [1.074291, 0.859433], 'p_i': 40, 'u_i': 1.9412},
        {'id': 5, 'e_m': 1.499766, 'e_o_k': [0.249961, 0.199969], 'p_i': 10, 'u_i': 2.2237},
        {'id': 6, 'e_m': 3.334135, 'e_o_k': [0.409935, 0.327948, 0.262358], 'p_i': 10, 'u_i': 2.4269},
        {'id': 7, 'e_m': 21.919742, 'e_o_k': [2.227616, 1.782093, 1.425674, 1.140539], 'p_i': 80, 'u_i': 4.8879},
    ]
    B_BUDGET = 167.439992
    return processors, tasks, B_BUDGET
