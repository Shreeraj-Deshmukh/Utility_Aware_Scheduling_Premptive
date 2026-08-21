"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.830191, 'e_o_k': [0.420959, 0.336767, 0.269414, 0.215531, 0.172425], 'p_i': 10, 'u_i': 3.0842},
        {'id': 1, 'e_m': 1.814502, 'e_o_k': [0.307334, 0.245868, 0.196694, 0.157355], 'p_i': 20, 'u_i': 4.6180},
        {'id': 2, 'e_m': 4.430906, 'e_o_k': [0.659047, 0.527238, 0.421790, 0.337432, 0.269946], 'p_i': 40, 'u_i': 1.1953},
        {'id': 3, 'e_m': 14.541137, 'e_o_k': [2.979741, 2.383793, 1.907034], 'p_i': 80, 'u_i': 1.1811},
        {'id': 4, 'e_m': 1.174677, 'e_o_k': [0.174720, 0.139776, 0.111821, 0.089457, 0.071565], 'p_i': 40, 'u_i': 1.7367},
        {'id': 5, 'e_m': 4.174079, 'e_o_k': [0.565704, 0.452563, 0.362050, 0.289640, 0.231712, 0.185370], 'p_i': 40, 'u_i': 3.6203},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
