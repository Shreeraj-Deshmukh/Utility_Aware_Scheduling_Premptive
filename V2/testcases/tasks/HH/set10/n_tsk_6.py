"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.613560, 'e_o_k': [0.255528, 0.204423, 0.163538, 0.130830, 0.104664], 'p_i': 10, 'u_i': 4.4970},
        {'id': 1, 'e_m': 0.560926, 'e_o_k': [0.321843, 0.257474, 0.205979], 'p_i': 20, 'u_i': 1.4275},
        {'id': 2, 'e_m': 10.590332, 'e_o_k': [4.018796, 3.215037, 2.572030, 2.057624, 1.646099, 1.316879], 'p_i': 40, 'u_i': 3.5743},
        {'id': 3, 'e_m': 25.380665, 'e_o_k': [12.036901, 9.629520, 7.703616, 6.162893], 'p_i': 80, 'u_i': 4.9867},
        {'id': 4, 'e_m': 1.454899, 'e_o_k': [0.552102, 0.441682, 0.353345, 0.282676, 0.226141, 0.180913], 'p_i': 20, 'u_i': 3.7777},
        {'id': 5, 'e_m': 1.116723, 'e_o_k': [0.465080, 0.372064, 0.297651, 0.238121, 0.190497], 'p_i': 20, 'u_i': 2.9102},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
