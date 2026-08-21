"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.786850, 'e_o_k': [0.161240, 0.128992, 0.103194], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 0.744352, 'e_o_k': [0.152531, 0.122025, 0.097620], 'p_i': 20, 'u_i': 4.7122},
        {'id': 2, 'e_m': 0.568045, 'e_o_k': [0.116403, 0.093122, 0.074498], 'p_i': 40, 'u_i': 2.7870},
        {'id': 3, 'e_m': 6.876570, 'e_o_k': [1.409133, 1.127307, 0.901845], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 2.991189, 'e_o_k': [0.612949, 0.490359, 0.392287], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.337006, 'e_o_k': [0.069059, 0.055247, 0.044197], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.443917, 'e_o_k': [0.090967, 0.072773, 0.058219], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 5.148870, 'e_o_k': [1.055096, 0.844077, 0.675262], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
