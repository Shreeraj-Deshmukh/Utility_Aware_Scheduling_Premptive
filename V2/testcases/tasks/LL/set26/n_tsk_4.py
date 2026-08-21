"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.821433, 'e_o_k': [0.477885, 0.382308, 0.305846, 0.244677], 'p_i': 10, 'u_i': 1.8833},
        {'id': 1, 'e_m': 0.734372, 'e_o_k': [0.109230, 0.087384, 0.069907, 0.055926, 0.044740], 'p_i': 20, 'u_i': 2.8074},
        {'id': 2, 'e_m': 1.986615, 'e_o_k': [0.269242, 0.215393, 0.172315, 0.137852, 0.110281, 0.088225], 'p_i': 40, 'u_i': 2.2803},
        {'id': 3, 'e_m': 2.517821, 'e_o_k': [0.341235, 0.272988, 0.218390, 0.174712, 0.139770, 0.111816], 'p_i': 80, 'u_i': 3.9685},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
