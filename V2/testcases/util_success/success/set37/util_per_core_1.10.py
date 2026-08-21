"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119991, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119991, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.958386, 'e_o_k': [0.402275, 0.321820, 0.257456, 0.205965], 'p_i': 10, 'u_i': 4.7284},
        {'id': 1, 'e_m': 1.348256, 'e_o_k': [0.224709, 0.179768], 'p_i': 20, 'u_i': 2.9850},
        {'id': 2, 'e_m': 18.358043, 'e_o_k': [3.059674, 2.447739], 'p_i': 40, 'u_i': 4.6281},
        {'id': 3, 'e_m': 17.476914, 'e_o_k': [1.559696, 1.247757, 0.998205, 0.798564, 0.638851], 'p_i': 80, 'u_i': 1.0041},
        {'id': 4, 'e_m': 12.606009, 'e_o_k': [1.125001, 0.900001, 0.720001, 0.576000, 0.460800], 'p_i': 40, 'u_i': 2.2799},
        {'id': 5, 'e_m': 0.773792, 'e_o_k': [0.078637, 0.062910, 0.050328, 0.040262], 'p_i': 10, 'u_i': 4.7563},
        {'id': 6, 'e_m': 1.687703, 'e_o_k': [0.281284, 0.225027], 'p_i': 10, 'u_i': 4.7914},
        {'id': 7, 'e_m': 39.842906, 'e_o_k': [3.555709, 2.844567, 2.275654, 1.820523, 1.456418], 'p_i': 80, 'u_i': 4.0401},
    ]
    B_BUDGET = 263.119991
    return processors, tasks, B_BUDGET
