"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.882119, 'e_o_k': [0.522811, 0.418249], 'p_i': 10, 'u_i': 3.1325},
        {'id': 1, 'e_m': 0.510977, 'e_o_k': [0.141938, 0.113550], 'p_i': 20, 'u_i': 4.7073},
        {'id': 2, 'e_m': 2.822239, 'e_o_k': [0.382492, 0.305993, 0.244795, 0.195836, 0.156669, 0.125335], 'p_i': 40, 'u_i': 3.8560},
        {'id': 3, 'e_m': 0.414313, 'e_o_k': [0.084900, 0.067920, 0.054336], 'p_i': 80, 'u_i': 2.5226},
        {'id': 4, 'e_m': 2.573196, 'e_o_k': [0.435839, 0.348672, 0.278937, 0.223150], 'p_i': 40, 'u_i': 1.7775},
        {'id': 5, 'e_m': 0.461745, 'e_o_k': [0.128262, 0.102610], 'p_i': 10, 'u_i': 2.7606},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
