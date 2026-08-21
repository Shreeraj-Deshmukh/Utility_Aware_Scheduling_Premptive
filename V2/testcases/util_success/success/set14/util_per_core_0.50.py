"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599998, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599998, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.903073, 'e_o_k': [0.150512, 0.120410], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 3.858610, 'e_o_k': [0.474419, 0.379535, 0.303628], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 14.015840, 'e_o_k': [1.723259, 1.378607, 1.102886], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 5.582582, 'e_o_k': [0.686383, 0.549106, 0.439285], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.211049, 'e_o_k': [0.021448, 0.017158, 0.013727, 0.010981], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 2.485101, 'e_o_k': [0.202080, 0.161664, 0.129331, 0.103465, 0.082772, 0.066218], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 9.889027, 'e_o_k': [1.215864, 0.972691, 0.778153], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 8.656439, 'e_o_k': [0.879719, 0.703776, 0.563020, 0.450416], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 119.599998
    return processors, tasks, B_BUDGET
