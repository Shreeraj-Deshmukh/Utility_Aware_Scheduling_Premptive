"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.624601, 'e_o_k': [0.105793, 0.084634, 0.067707, 0.054166], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 0.610894, 'e_o_k': [0.103471, 0.082777, 0.066222, 0.052977], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 3.088315, 'e_o_k': [0.523089, 0.418471, 0.334777, 0.267821], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 4.046818, 'e_o_k': [0.685437, 0.548349, 0.438679, 0.350944], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.371042, 'e_o_k': [0.062846, 0.050277, 0.040221, 0.032177], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 3.248721, 'e_o_k': [0.550258, 0.440206, 0.352165, 0.281732], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.378075, 'e_o_k': [0.064037, 0.051230, 0.040984, 0.032787], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 5.584342, 'e_o_k': [0.945857, 0.756686, 0.605349, 0.484279], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
