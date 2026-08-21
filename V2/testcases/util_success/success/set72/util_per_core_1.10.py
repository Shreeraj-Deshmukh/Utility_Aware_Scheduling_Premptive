"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120002, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120002, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.953642, 'e_o_k': [0.401793, 0.321434, 0.257147, 0.205718], 'p_i': 10, 'u_i': 3.5991},
        {'id': 1, 'e_m': 6.729875, 'e_o_k': [0.827444, 0.661955, 0.529564], 'p_i': 20, 'u_i': 1.8047},
        {'id': 2, 'e_m': 6.708219, 'e_o_k': [0.545490, 0.436392, 0.349114, 0.279291, 0.223433, 0.178746], 'p_i': 40, 'u_i': 3.6123},
        {'id': 3, 'e_m': 31.163471, 'e_o_k': [3.167019, 2.533616, 2.026892, 1.621514], 'p_i': 80, 'u_i': 4.6586},
        {'id': 4, 'e_m': 2.301923, 'e_o_k': [0.283023, 0.226419, 0.181135], 'p_i': 20, 'u_i': 2.5996},
        {'id': 5, 'e_m': 6.606777, 'e_o_k': [1.101129, 0.880904], 'p_i': 40, 'u_i': 2.8042},
        {'id': 6, 'e_m': 2.362388, 'e_o_k': [0.290458, 0.232366, 0.185893], 'p_i': 10, 'u_i': 1.1351},
        {'id': 7, 'e_m': 15.775552, 'e_o_k': [1.407861, 1.126289, 0.901031, 0.720825, 0.576660], 'p_i': 40, 'u_i': 3.5678},
    ]
    B_BUDGET = 263.120002
    return processors, tasks, B_BUDGET
