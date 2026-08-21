"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.202831, 'e_o_k': [1.263919, 1.011135, 0.808908], 'p_i': 10, 'u_i': 1.0870},
        {'id': 1, 'e_m': 0.431270, 'e_o_k': [0.163657, 0.130926, 0.104741, 0.083793, 0.067034, 0.053627], 'p_i': 20, 'u_i': 2.0773},
        {'id': 2, 'e_m': 1.727609, 'e_o_k': [0.719495, 0.575596, 0.460477, 0.368381, 0.294705], 'p_i': 40, 'u_i': 2.9699},
        {'id': 3, 'e_m': 18.665343, 'e_o_k': [10.709623, 8.567698, 6.854159], 'p_i': 80, 'u_i': 1.6736},
        {'id': 4, 'e_m': 3.502419, 'e_o_k': [1.458647, 1.166917, 0.933534, 0.746827, 0.597462], 'p_i': 20, 'u_i': 2.6796},
        {'id': 5, 'e_m': 4.261019, 'e_o_k': [2.444847, 1.955878, 1.564702], 'p_i': 40, 'u_i': 2.5270},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
