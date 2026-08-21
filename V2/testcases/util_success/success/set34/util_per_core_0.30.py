"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760009, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760009, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.164580, 'e_o_k': [0.020235, 0.016188, 0.012951], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 0.859018, 'e_o_k': [0.069852, 0.055882, 0.044706, 0.035764, 0.028612, 0.022889], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 8.446294, 'e_o_k': [1.038479, 0.830783, 0.664626], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 5.572862, 'e_o_k': [0.685188, 0.548150, 0.438520], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 1.997342, 'e_o_k': [0.245575, 0.196460, 0.157168], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 2.453536, 'e_o_k': [0.408923, 0.327138], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.021283, 'e_o_k': [0.001731, 0.001385, 0.001108, 0.000886, 0.000709, 0.000567], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 0.980354, 'e_o_k': [0.087490, 0.069992, 0.055994, 0.044795, 0.035836], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 71.760009
    return processors, tasks, B_BUDGET
