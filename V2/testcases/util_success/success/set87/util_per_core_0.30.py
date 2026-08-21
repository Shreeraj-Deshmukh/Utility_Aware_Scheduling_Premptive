"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.233043, 'e_o_k': [0.110041, 0.088033, 0.070426, 0.056341, 0.045073], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.237910, 'e_o_k': [0.029251, 0.023401, 0.018721], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 0.877061, 'e_o_k': [0.078272, 0.062617, 0.050094, 0.040075, 0.032060], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 9.227929, 'e_o_k': [1.134581, 0.907665, 0.726132], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 1.813271, 'e_o_k': [0.184275, 0.147420, 0.117936, 0.094349], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 1.321338, 'e_o_k': [0.220223, 0.176178], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 0.777572, 'e_o_k': [0.069393, 0.055514, 0.044412, 0.035529, 0.028423], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 1.705760, 'e_o_k': [0.152228, 0.121782, 0.097426, 0.077940, 0.062352], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET
