"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.495128, 'e_o_k': [0.133430, 0.106744, 0.085395, 0.068316, 0.054653], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.891029, 'e_o_k': [0.109553, 0.087642, 0.070114], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 2.673820, 'e_o_k': [0.238620, 0.190896, 0.152717, 0.122174, 0.097739], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 6.988530, 'e_o_k': [0.623679, 0.498943, 0.399154, 0.319324, 0.255459], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 1.311340, 'e_o_k': [0.106634, 0.085307, 0.068246, 0.054597, 0.043677, 0.034942], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 27.487845, 'e_o_k': [2.793480, 2.234784, 1.787827, 1.430262], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 2.329822, 'e_o_k': [0.388304, 0.310643], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 3.260774, 'e_o_k': [0.331380, 0.265104, 0.212083, 0.169666], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 143.520003
    return processors, tasks, B_BUDGET
