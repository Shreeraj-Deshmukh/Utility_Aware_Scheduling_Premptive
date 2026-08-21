"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400015, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400015, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.222670, 'e_o_k': [0.207092, 0.165673, 0.132539, 0.106031], 'p_i': 10, 'u_i': 4.4576},
        {'id': 1, 'e_m': 0.002934, 'e_o_k': [0.000815, 0.000652], 'p_i': 20, 'u_i': 1.2102},
        {'id': 2, 'e_m': 17.452391, 'e_o_k': [3.576310, 2.861048, 2.288838], 'p_i': 40, 'u_i': 3.7306},
        {'id': 3, 'e_m': 5.457841, 'e_o_k': [1.118410, 0.894728, 0.715782], 'p_i': 80, 'u_i': 4.1325},
        {'id': 4, 'e_m': 1.018899, 'e_o_k': [0.172578, 0.138062, 0.110450, 0.088360], 'p_i': 20, 'u_i': 2.4718},
        {'id': 5, 'e_m': 4.884345, 'e_o_k': [0.661965, 0.529572, 0.423657, 0.338926, 0.271141, 0.216913], 'p_i': 40, 'u_i': 1.1369},
    ]
    B_BUDGET = 110.400015
    return processors, tasks, B_BUDGET
