"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.600854, 'e_o_k': [0.228011, 0.182409, 0.145927, 0.116742, 0.093393, 0.074715], 'p_i': 10, 'u_i': 4.4924},
        {'id': 1, 'e_m': 1.220515, 'e_o_k': [0.700295, 0.560236, 0.448189], 'p_i': 20, 'u_i': 4.2054},
        {'id': 2, 'e_m': 8.826737, 'e_o_k': [3.676056, 2.940845, 2.352676, 1.882141, 1.505713], 'p_i': 40, 'u_i': 2.8306},
        {'id': 3, 'e_m': 0.565020, 'e_o_k': [0.439460, 0.351568], 'p_i': 80, 'u_i': 2.8504},
        {'id': 4, 'e_m': 0.405741, 'e_o_k': [0.153970, 0.123176, 0.098541, 0.078833, 0.063066, 0.050453], 'p_i': 10, 'u_i': 1.4385},
        {'id': 5, 'e_m': 0.846685, 'e_o_k': [0.321298, 0.257039, 0.205631, 0.164505, 0.131604, 0.105283], 'p_i': 80, 'u_i': 4.3024},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
