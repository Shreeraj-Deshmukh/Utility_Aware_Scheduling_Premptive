"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.178484, 'e_o_k': [0.030231, 0.024185, 0.019348, 0.015478], 'p_i': 10, 'u_i': 4.6156},
        {'id': 1, 'e_m': 0.396303, 'e_o_k': [0.067124, 0.053700, 0.042960, 0.034368], 'p_i': 20, 'u_i': 1.3815},
        {'id': 2, 'e_m': 0.607908, 'e_o_k': [0.124571, 0.099657, 0.079726], 'p_i': 40, 'u_i': 2.2542},
        {'id': 3, 'e_m': 13.292945, 'e_o_k': [1.801564, 1.441251, 1.153001, 0.922401, 0.737920, 0.590336], 'p_i': 80, 'u_i': 3.1493},
        {'id': 4, 'e_m': 3.115303, 'e_o_k': [0.527660, 0.422128, 0.337702, 0.270162], 'p_i': 20, 'u_i': 4.3022},
        {'id': 5, 'e_m': 2.016943, 'e_o_k': [0.273352, 0.218682, 0.174945, 0.139956, 0.111965, 0.089572], 'p_i': 80, 'u_i': 4.8493},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
