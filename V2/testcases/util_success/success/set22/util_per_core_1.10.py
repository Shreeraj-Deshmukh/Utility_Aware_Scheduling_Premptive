"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119999, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119999, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.343225, 'e_o_k': [0.271860, 0.217488, 0.173990, 0.139192, 0.111354, 0.089083], 'p_i': 10, 'u_i': 3.0520},
        {'id': 1, 'e_m': 0.365352, 'e_o_k': [0.044920, 0.035936, 0.028749], 'p_i': 20, 'u_i': 1.8188},
        {'id': 2, 'e_m': 6.450565, 'e_o_k': [1.075094, 0.860075], 'p_i': 40, 'u_i': 1.3467},
        {'id': 3, 'e_m': 11.981414, 'e_o_k': [0.974289, 0.779431, 0.623545, 0.498836, 0.399069, 0.319255], 'p_i': 80, 'u_i': 3.9525},
        {'id': 4, 'e_m': 3.419764, 'e_o_k': [0.347537, 0.278030, 0.222424, 0.177939], 'p_i': 10, 'u_i': 3.3005},
        {'id': 5, 'e_m': 4.881077, 'e_o_k': [0.435603, 0.348482, 0.278786, 0.223029, 0.178423], 'p_i': 10, 'u_i': 3.6474},
        {'id': 6, 'e_m': 3.300846, 'e_o_k': [0.335452, 0.268361, 0.214689, 0.171751], 'p_i': 10, 'u_i': 2.4979},
        {'id': 7, 'e_m': 7.524189, 'e_o_k': [0.764653, 0.611723, 0.489378, 0.391503], 'p_i': 20, 'u_i': 1.8465},
    ]
    B_BUDGET = 263.119999
    return processors, tasks, B_BUDGET
