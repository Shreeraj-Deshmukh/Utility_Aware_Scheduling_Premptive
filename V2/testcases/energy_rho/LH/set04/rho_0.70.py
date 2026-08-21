"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 72.863997, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.7, "seed": 1004, "set": 4, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 72.863997, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.7, "seed": 1004, "set": 4, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.176411, 0.141129, 0.112903, 0.090322, 0.072258, 0.057806], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.010792, 0.008634, 0.006907, 0.005525, 0.004420, 0.003536], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [1.020442, 0.816354], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [1.740151, 1.392120], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.913760, 0.731008], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [2.500031, 2.000025, 1.600020, 1.280016], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.133177, 0.106542], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [1.301561, 1.041249], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 72.863997
    return processors, tasks, B_BUDGET
