"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.123701, 'e_o_k': [0.983238, 0.589943], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 2.998422, 'e_o_k': [1.929132, 1.157479, 0.694488, 0.416693], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 12.570386, 'e_o_k': [8.087565, 4.852539, 2.911523, 1.746914], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.317492, 'e_o_k': [0.277805, 0.166683], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 2.758630, 'e_o_k': [1.774854, 1.064912, 0.638947, 0.383368], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 2.930909, 'e_o_k': [2.564546, 1.538727], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.031369, 'e_o_k': [0.019048, 0.011429, 0.006857, 0.004114, 0.002469], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.066594, 'e_o_k': [0.040437, 0.024262, 0.014557, 0.008734, 0.005241], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
