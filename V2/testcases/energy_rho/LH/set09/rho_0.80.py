"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 78.016002, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.8, "seed": 1009, "set": 9, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 78.016002, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.8, "seed": 1009, "set": 9, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.868614, 'e_o_k': [0.675588, 0.540471], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 0.707032, 'e_o_k': [0.268303, 0.214642, 0.171714, 0.137371, 0.109897, 0.087918], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 4.447481, 'e_o_k': [1.852235, 1.481788, 1.185430, 0.948344, 0.758675], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 1.996160, 'e_o_k': [1.552569, 1.242055], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.078011, 'e_o_k': [0.032489, 0.025991, 0.020793, 0.016634, 0.013308], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.176089, 'e_o_k': [0.101035, 0.080828, 0.064662], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 2.563544, 'e_o_k': [1.215773, 0.972618, 0.778095, 0.622476], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 0.648544, 'e_o_k': [0.372116, 0.297692, 0.238154], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 78.016002
    return processors, tasks, B_BUDGET
