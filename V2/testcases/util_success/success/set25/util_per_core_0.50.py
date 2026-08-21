"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600006, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600006, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.999300, 'e_o_k': [0.333217, 0.266573], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 6.481904, 'e_o_k': [0.796955, 0.637564, 0.510051], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 3.652780, 'e_o_k': [0.371218, 0.296974, 0.237579, 0.190063], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 9.480613, 'e_o_k': [1.580102, 1.264082], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.298734, 'e_o_k': [0.105609, 0.084487, 0.067590, 0.054072, 0.043257, 0.034606], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 1.777113, 'e_o_k': [0.144509, 0.115607, 0.092486, 0.073989, 0.059191, 0.047353], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 3.962233, 'e_o_k': [0.660372, 0.528298], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.457678, 'e_o_k': [0.056272, 0.045018, 0.036014], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 119.600006
    return processors, tasks, B_BUDGET
