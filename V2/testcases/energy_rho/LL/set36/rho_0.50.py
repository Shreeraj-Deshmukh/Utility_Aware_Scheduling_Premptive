"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 45.999999, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1036, "set": 36, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}
"""

_SPEC = '{"B": 45.999999, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1036, "set": 36, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.070080, 0.056064, 0.044851, 0.035881, 0.028705], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.073626, 0.058901, 0.047121], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.051144, 0.040916, 0.032732, 0.026186, 0.020949, 0.016759], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [0.571291, 0.457033], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [1.345946, 1.076757, 0.861406, 0.689125], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.326678, 0.261343, 0.209074], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.089090, 0.071272, 0.057018, 0.045614], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.058682, 0.046946, 0.037557, 0.030045], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 45.999999
    return processors, tasks, B_BUDGET
