"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 166.335995, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1056, "set": 56, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}
"""

_SPEC = '{"B": 166.335995, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1056, "set": 56, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.150064, 'e_o_k': [0.815902, 0.652721, 0.522177, 0.417742, 0.334193, 0.267355], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.276887, 'e_o_k': [0.115314, 0.092252, 0.073801, 0.059041, 0.047233], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 1.036903, 'e_o_k': [0.431837, 0.345470, 0.276376, 0.221101, 0.176881], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.261660, 'e_o_k': [0.203513, 0.162811], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 12.654356, 'e_o_k': [9.842277, 7.873821], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.168799, 'e_o_k': [0.131288, 0.105031], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 2.612506, 'e_o_k': [1.088026, 0.870421, 0.696337, 0.557069, 0.445655], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 3.342402, 'e_o_k': [1.917772, 1.534217, 1.227374], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 166.335995
    return processors, tasks, B_BUDGET
