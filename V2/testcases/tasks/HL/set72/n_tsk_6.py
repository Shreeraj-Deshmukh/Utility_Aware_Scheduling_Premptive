"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.320746, 'e_o_k': [0.047707, 0.038166, 0.030533, 0.024426, 0.019541], 'p_i': 10, 'u_i': 1.6464},
        {'id': 1, 'e_m': 2.479074, 'e_o_k': [0.688632, 0.550905], 'p_i': 20, 'u_i': 4.4830},
        {'id': 2, 'e_m': 6.943514, 'e_o_k': [0.941039, 0.752831, 0.602265, 0.481812, 0.385450, 0.308360], 'p_i': 40, 'u_i': 3.9048},
        {'id': 3, 'e_m': 8.482935, 'e_o_k': [1.261741, 1.009393, 0.807514, 0.646011, 0.516809], 'p_i': 80, 'u_i': 3.4604},
        {'id': 4, 'e_m': 4.344856, 'e_o_k': [0.890339, 0.712271, 0.569817], 'p_i': 20, 'u_i': 2.2645},
        {'id': 5, 'e_m': 1.471044, 'e_o_k': [0.218801, 0.175041, 0.140033, 0.112026, 0.089621], 'p_i': 10, 'u_i': 4.9290},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
