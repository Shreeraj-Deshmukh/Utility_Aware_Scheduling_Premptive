"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.106037, 'e_o_k': [0.634611, 0.507689, 0.406151], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 1.049824, 'e_o_k': [0.602358, 0.481886, 0.385509], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.127751, 'e_o_k': [0.073300, 0.058640, 0.046912], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 3.081106, 'e_o_k': [1.767848, 1.414278, 1.131423], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 1.628628, 'e_o_k': [0.934458, 0.747567, 0.598053], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 0.896350, 'e_o_k': [0.514299, 0.411439, 0.329151], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 7.298706, 'e_o_k': [4.187782, 3.350226, 2.680180], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 0.611971, 'e_o_k': [0.351131, 0.280905, 0.224724], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
