"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.140267, 'e_o_k': [0.019010, 0.015208, 0.012166, 0.009733, 0.007787, 0.006229], 'p_i': 10, 'u_i': 3.8731},
        {'id': 1, 'e_m': 0.613585, 'e_o_k': [0.125735, 0.100588, 0.080470], 'p_i': 20, 'u_i': 4.5676},
        {'id': 2, 'e_m': 3.794514, 'e_o_k': [0.642702, 0.514162, 0.411329, 0.329064], 'p_i': 40, 'u_i': 2.8991},
        {'id': 3, 'e_m': 22.763738, 'e_o_k': [3.385849, 2.708679, 2.166943, 1.733555, 1.386844], 'p_i': 80, 'u_i': 1.9490},
        {'id': 4, 'e_m': 2.089724, 'e_o_k': [0.580479, 0.464383], 'p_i': 20, 'u_i': 1.1516},
        {'id': 5, 'e_m': 10.855934, 'e_o_k': [2.224577, 1.779661, 1.423729], 'p_i': 40, 'u_i': 2.6742},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
