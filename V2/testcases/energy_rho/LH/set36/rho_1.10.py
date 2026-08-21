"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 93.471987, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1036, "set": 36, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}
"""

_SPEC = '{"B": 93.471987, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1036, "set": 36, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.196224, 0.156979, 0.125583, 0.100467, 0.080373], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.206153, 0.164923, 0.131938], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.143204, 0.114563, 0.091651, 0.073321, 0.058656, 0.046925], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [1.599615, 1.279692], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [3.768650, 3.014920, 2.411936, 1.929549], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.914700, 0.731760, 0.585408], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.249452, 0.199561, 0.159649, 0.127719], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.164310, 0.131448, 0.105159, 0.084127], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 93.471987
    return processors, tasks, B_BUDGET
