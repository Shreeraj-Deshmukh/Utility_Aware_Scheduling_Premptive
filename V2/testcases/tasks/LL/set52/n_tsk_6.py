"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050612, 'e_o_k': [0.007528, 0.006022, 0.004818, 0.003854, 0.003083], 'p_i': 10, 'u_i': 1.6984},
        {'id': 1, 'e_m': 0.842273, 'e_o_k': [0.142661, 0.114129, 0.091303, 0.073043], 'p_i': 20, 'u_i': 3.4597},
        {'id': 2, 'e_m': 7.106119, 'e_o_k': [1.203611, 0.962889, 0.770311, 0.616249], 'p_i': 40, 'u_i': 4.7133},
        {'id': 3, 'e_m': 9.044792, 'e_o_k': [1.225821, 0.980657, 0.784525, 0.627620, 0.502096, 0.401677], 'p_i': 80, 'u_i': 2.1441},
        {'id': 4, 'e_m': 1.353058, 'e_o_k': [0.201252, 0.161002, 0.128801, 0.103041, 0.082433], 'p_i': 40, 'u_i': 1.5180},
        {'id': 5, 'e_m': 0.282859, 'e_o_k': [0.047910, 0.038328, 0.030662, 0.024530], 'p_i': 10, 'u_i': 2.4726},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
