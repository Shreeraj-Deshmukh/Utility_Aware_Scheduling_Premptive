"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 29, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 29, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.014064, 0.011251, 0.009001], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.400236, 0.320189, 0.256151, 0.204921, 0.163937, 0.131149], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [1.048890, 0.839112], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [1.183972, 0.947177, 0.757742, 0.606194], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [4.529025, 3.623220, 2.898576, 2.318861], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.019678, 0.015743, 0.012594, 0.010075], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.345907, 0.276726, 0.221381, 0.177104], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [1.689809, 1.351847, 1.081478], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
