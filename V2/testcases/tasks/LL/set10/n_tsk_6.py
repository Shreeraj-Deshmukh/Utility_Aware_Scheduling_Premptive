"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.306780, 'e_o_k': [0.045630, 0.036504, 0.029203, 0.023363, 0.018690], 'p_i': 10, 'u_i': 4.4970},
        {'id': 1, 'e_m': 0.280463, 'e_o_k': [0.057472, 0.045978, 0.036782], 'p_i': 20, 'u_i': 1.4275},
        {'id': 2, 'e_m': 5.295166, 'e_o_k': [0.717642, 0.574114, 0.459291, 0.367433, 0.293946, 0.235157], 'p_i': 40, 'u_i': 3.5743},
        {'id': 3, 'e_m': 12.690332, 'e_o_k': [2.149447, 1.719557, 1.375646, 1.100517], 'p_i': 80, 'u_i': 4.9867},
        {'id': 4, 'e_m': 0.727450, 'e_o_k': [0.098590, 0.078872, 0.063097, 0.050478, 0.040382, 0.032306], 'p_i': 20, 'u_i': 3.7777},
        {'id': 5, 'e_m': 0.558362, 'e_o_k': [0.083050, 0.066440, 0.053152, 0.042522, 0.034017], 'p_i': 20, 'u_i': 2.9102},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
