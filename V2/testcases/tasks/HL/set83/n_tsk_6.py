"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.112793, 'e_o_k': [0.586887, 0.469510], 'p_i': 10, 'u_i': 3.4799},
        {'id': 1, 'e_m': 1.985293, 'e_o_k': [0.295290, 0.236232, 0.188986, 0.151188, 0.120951], 'p_i': 20, 'u_i': 2.9893},
        {'id': 2, 'e_m': 1.603759, 'e_o_k': [0.238541, 0.190833, 0.152666, 0.122133, 0.097706], 'p_i': 40, 'u_i': 3.6030},
        {'id': 3, 'e_m': 19.251871, 'e_o_k': [5.347742, 4.278194], 'p_i': 80, 'u_i': 4.7122},
        {'id': 4, 'e_m': 13.207286, 'e_o_k': [3.668690, 2.934952], 'p_i': 80, 'u_i': 2.7870},
        {'id': 5, 'e_m': 1.744905, 'e_o_k': [0.357563, 0.286050, 0.228840], 'p_i': 40, 'u_i': 1.7506},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
