"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.102178, 0.061307, 0.036784, 0.022070, 0.013242], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.091657, 0.054994, 0.032997], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.079168, 0.047501, 0.028500, 0.017100, 0.010260, 0.006156], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [0.642702, 0.385621], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [1.825935, 1.095561, 0.657336, 0.394402], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.406681, 0.244009, 0.146405], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.120861, 0.072517, 0.043510, 0.026106], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.079609, 0.047766, 0.028659, 0.017196], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
