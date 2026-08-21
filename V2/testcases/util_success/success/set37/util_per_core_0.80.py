"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360007, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360007, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.878826, 'e_o_k': [0.292564, 0.234051, 0.187241, 0.149793], 'p_i': 10, 'u_i': 4.7284},
        {'id': 1, 'e_m': 0.980550, 'e_o_k': [0.163425, 0.130740], 'p_i': 20, 'u_i': 2.9850},
        {'id': 2, 'e_m': 13.351304, 'e_o_k': [2.225217, 1.780174], 'p_i': 40, 'u_i': 4.6281},
        {'id': 3, 'e_m': 12.710483, 'e_o_k': [1.134324, 0.907460, 0.725968, 0.580774, 0.464619], 'p_i': 80, 'u_i': 1.0041},
        {'id': 4, 'e_m': 9.168006, 'e_o_k': [0.818182, 0.654546, 0.523637, 0.418909, 0.335128], 'p_i': 40, 'u_i': 2.2799},
        {'id': 5, 'e_m': 0.562758, 'e_o_k': [0.057191, 0.045753, 0.036602, 0.029282], 'p_i': 10, 'u_i': 4.7563},
        {'id': 6, 'e_m': 1.227420, 'e_o_k': [0.204570, 0.163656], 'p_i': 10, 'u_i': 4.7914},
        {'id': 7, 'e_m': 28.976659, 'e_o_k': [2.585970, 2.068776, 1.655021, 1.324017, 1.059213], 'p_i': 80, 'u_i': 4.0401},
    ]
    B_BUDGET = 191.360007
    return processors, tasks, B_BUDGET
