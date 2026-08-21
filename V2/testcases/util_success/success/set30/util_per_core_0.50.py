"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.60001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.60001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.061278, 'e_o_k': [0.007534, 0.006027, 0.004822], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.636753, 'e_o_k': [0.214412, 0.171530, 0.137224, 0.109779, 0.087823, 0.070259], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 3.371433, 'e_o_k': [0.561906, 0.449524], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 6.241223, 'e_o_k': [0.634271, 0.507416, 0.405933, 0.324747], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 23.874434, 'e_o_k': [2.426264, 1.941011, 1.552809, 1.242247], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.103733, 'e_o_k': [0.010542, 0.008434, 0.006747, 0.005397], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.823425, 'e_o_k': [0.185307, 0.148246, 0.118597, 0.094877], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 7.362739, 'e_o_k': [0.905255, 0.724204, 0.579363], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 119.600010
    return processors, tasks, B_BUDGET
