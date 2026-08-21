"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400016, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400016, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255642, 'e_o_k': [0.052386, 0.041909, 0.033527], 'p_i': 10, 'u_i': 1.1226},
        {'id': 1, 'e_m': 5.834936, 'e_o_k': [1.195684, 0.956547, 0.765237], 'p_i': 20, 'u_i': 3.8598},
        {'id': 2, 'e_m': 1.030030, 'e_o_k': [0.211072, 0.168857, 0.135086], 'p_i': 40, 'u_i': 4.6365},
        {'id': 3, 'e_m': 1.325038, 'e_o_k': [0.271524, 0.217219, 0.173775], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 19.367876, 'e_o_k': [3.968827, 3.175062, 2.540049], 'p_i': 80, 'u_i': 3.5452},
        {'id': 5, 'e_m': 0.396585, 'e_o_k': [0.081267, 0.065014, 0.052011], 'p_i': 40, 'u_i': 3.7479},
        {'id': 6, 'e_m': 3.226328, 'e_o_k': [0.661133, 0.528906, 0.423125], 'p_i': 80, 'u_i': 4.4508},
        {'id': 7, 'e_m': 2.960663, 'e_o_k': [0.606693, 0.485355, 0.388284], 'p_i': 20, 'u_i': 2.7382},
    ]
    B_BUDGET = 110.400016
    return processors, tasks, B_BUDGET
