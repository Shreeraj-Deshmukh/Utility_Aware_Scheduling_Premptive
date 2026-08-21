"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399984, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399984, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.722711, 'e_o_k': [0.233475, 0.186780, 0.149424, 0.119539, 0.095631, 0.076505], 'p_i': 10, 'u_i': 3.5509},
        {'id': 1, 'e_m': 0.629824, 'e_o_k': [0.106677, 0.085342, 0.068274, 0.054619], 'p_i': 20, 'u_i': 2.4298},
        {'id': 2, 'e_m': 11.031418, 'e_o_k': [2.260537, 1.808429, 1.446743], 'p_i': 40, 'u_i': 2.9531},
        {'id': 3, 'e_m': 25.636179, 'e_o_k': [3.474415, 2.779532, 2.223626, 1.778900, 1.423120, 1.138496], 'p_i': 80, 'u_i': 4.5727},
    ]
    B_BUDGET = 110.399984
    return processors, tasks, B_BUDGET
