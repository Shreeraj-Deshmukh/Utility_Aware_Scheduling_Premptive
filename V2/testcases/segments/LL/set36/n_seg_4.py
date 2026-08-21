"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.079804, 0.063843, 0.051074, 0.040860], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.060856, 0.048685, 0.038948, 0.031158], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.063918, 0.051134, 0.040908, 0.032726], 'p_i': 40, 'u_i': 4.4037},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [0.348348, 0.278679, 0.222943, 0.178354], 'p_i': 80, 'u_i': 1.7011},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [1.345946, 1.076757, 0.861406, 0.689125], 'p_i': 40, 'u_i': 1.8442},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.270019, 0.216015, 0.172812, 0.138250], 'p_i': 40, 'u_i': 2.3108},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.089090, 0.071272, 0.057018, 0.045614], 'p_i': 10, 'u_i': 1.0383},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.058682, 0.046946, 0.037557, 0.030045], 'p_i': 40, 'u_i': 2.0614},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
