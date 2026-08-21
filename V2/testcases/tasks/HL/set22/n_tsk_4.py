"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.922344, 'e_o_k': [0.583404, 0.466724, 0.373379, 0.298703, 0.238962], 'p_i': 10, 'u_i': 3.1771},
        {'id': 1, 'e_m': 0.290131, 'e_o_k': [0.080592, 0.064473], 'p_i': 20, 'u_i': 3.8810},
        {'id': 2, 'e_m': 10.050027, 'e_o_k': [1.702240, 1.361792, 1.089434, 0.871547], 'p_i': 40, 'u_i': 1.9496},
        {'id': 3, 'e_m': 11.360669, 'e_o_k': [3.155741, 2.524593], 'p_i': 80, 'u_i': 4.0364},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
