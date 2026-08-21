"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.040333, 'e_o_k': [0.005466, 0.004373, 0.003498, 0.002799, 0.002239, 0.001791], 'p_i': 10, 'u_i': 1.7448},
        {'id': 1, 'e_m': 0.627139, 'e_o_k': [0.093280, 0.074624, 0.059699, 0.047759, 0.038207], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 0.595631, 'e_o_k': [0.088593, 0.070875, 0.056700, 0.045360, 0.036288], 'p_i': 40, 'u_i': 1.5908},
        {'id': 3, 'e_m': 6.445710, 'e_o_k': [0.958727, 0.766981, 0.613585, 0.490868, 0.392694], 'p_i': 80, 'u_i': 1.2188},
        {'id': 4, 'e_m': 1.367973, 'e_o_k': [0.280322, 0.224258, 0.179406], 'p_i': 10, 'u_i': 2.5958},
        {'id': 5, 'e_m': 1.323503, 'e_o_k': [0.271210, 0.216968, 0.173574], 'p_i': 10, 'u_i': 3.0557},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
