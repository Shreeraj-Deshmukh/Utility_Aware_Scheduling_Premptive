"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.155705, 'e_o_k': [0.548098, 0.438479, 0.350783, 0.280626], 'p_i': 10, 'u_i': 4.8210},
        {'id': 1, 'e_m': 0.470230, 'e_o_k': [0.365735, 0.292588], 'p_i': 20, 'u_i': 2.4270},
        {'id': 2, 'e_m': 10.067610, 'e_o_k': [3.820435, 3.056348, 2.445078, 1.956063, 1.564850, 1.251880], 'p_i': 40, 'u_i': 3.3094},
        {'id': 3, 'e_m': 0.738221, 'e_o_k': [0.423569, 0.338855, 0.271084], 'p_i': 80, 'u_i': 3.8452},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
