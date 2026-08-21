"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.929756, 'e_o_k': [0.195052, 0.117031, 0.070219, 0.042131, 0.025279, 0.015167], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.056878, 'e_o_k': [0.011932, 0.007159, 0.004296, 0.002577, 0.001546, 0.000928], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 2.623994, 'e_o_k': [0.819998, 0.491999], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 4.474673, 'e_o_k': [1.398335, 0.839001], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 2.349668, 'e_o_k': [0.734271, 0.440563], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 10.542988, 'e_o_k': [2.422562, 1.453537, 0.872122, 0.523273], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.342456, 'e_o_k': [0.107017, 0.064210], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 3.346871, 'e_o_k': [1.045897, 0.627538], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
