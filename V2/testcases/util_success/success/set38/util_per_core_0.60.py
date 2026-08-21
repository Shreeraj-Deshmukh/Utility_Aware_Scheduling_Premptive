"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520012, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520012, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.211786, 'e_o_k': [0.261172, 0.208937, 0.167150, 0.133720, 0.106976, 0.085581], 'p_i': 10, 'u_i': 1.2855},
        {'id': 1, 'e_m': 3.587766, 'e_o_k': [0.291745, 0.233396, 0.186717, 0.149374, 0.119499, 0.095599], 'p_i': 20, 'u_i': 4.6522},
        {'id': 2, 'e_m': 9.537761, 'e_o_k': [0.851181, 0.680944, 0.544756, 0.435804, 0.348644], 'p_i': 40, 'u_i': 4.9928},
        {'id': 3, 'e_m': 6.030748, 'e_o_k': [0.538203, 0.430563, 0.344450, 0.275560, 0.220448], 'p_i': 80, 'u_i': 3.9733},
        {'id': 4, 'e_m': 0.883521, 'e_o_k': [0.089789, 0.071831, 0.057465, 0.045972], 'p_i': 10, 'u_i': 1.2745},
        {'id': 5, 'e_m': 3.750254, 'e_o_k': [0.304958, 0.243967, 0.195173, 0.156139, 0.124911, 0.099929], 'p_i': 40, 'u_i': 2.7525},
        {'id': 6, 'e_m': 6.931131, 'e_o_k': [0.852188, 0.681751, 0.545400], 'p_i': 40, 'u_i': 3.5893},
        {'id': 7, 'e_m': 0.302180, 'e_o_k': [0.037153, 0.029723, 0.023778], 'p_i': 10, 'u_i': 2.8023},
    ]
    B_BUDGET = 143.520012
    return processors, tasks, B_BUDGET
