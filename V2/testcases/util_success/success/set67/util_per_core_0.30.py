"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759991, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759991, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.716691, 'e_o_k': [0.242446, 0.193957, 0.155166, 0.124132, 0.099306], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.076075, 'e_o_k': [0.007731, 0.006185, 0.004948, 0.003958], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 3.816320, 'e_o_k': [0.636053, 0.508843], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 1.769319, 'e_o_k': [0.294886, 0.235909], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 2.616176, 'e_o_k': [0.321661, 0.257329, 0.205863], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 0.869200, 'e_o_k': [0.144867, 0.115893], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 6.824200, 'e_o_k': [0.839041, 0.671233, 0.536986], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.513429, 'e_o_k': [0.063127, 0.050501, 0.040401], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 71.759991
    return processors, tasks, B_BUDGET
