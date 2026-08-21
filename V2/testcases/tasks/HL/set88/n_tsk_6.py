"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400021, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400021, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.944372, 'e_o_k': [0.159955, 0.127964, 0.102371, 0.081897], 'p_i': 10, 'u_i': 3.1874},
        {'id': 1, 'e_m': 2.227287, 'e_o_k': [0.618691, 0.494953], 'p_i': 20, 'u_i': 2.4550},
        {'id': 2, 'e_m': 7.236978, 'e_o_k': [1.482987, 1.186390, 0.949112], 'p_i': 40, 'u_i': 4.1368},
        {'id': 3, 'e_m': 0.354839, 'e_o_k': [0.098566, 0.078853], 'p_i': 80, 'u_i': 2.0023},
        {'id': 4, 'e_m': 14.061479, 'e_o_k': [2.091486, 1.673189, 1.338551, 1.070841, 0.856673], 'p_i': 40, 'u_i': 1.7941},
        {'id': 5, 'e_m': 2.292064, 'e_o_k': [0.340919, 0.272735, 0.218188, 0.174550, 0.139640], 'p_i': 40, 'u_i': 1.7354},
    ]
    B_BUDGET = 110.400021
    return processors, tasks, B_BUDGET
