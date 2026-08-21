"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.635332, 'e_o_k': [0.107610, 0.086088, 0.068871, 0.055097], 'p_i': 10, 'u_i': 3.6021},
        {'id': 1, 'e_m': 0.040561, 'e_o_k': [0.008312, 0.006649, 0.005319], 'p_i': 20, 'u_i': 4.3808},
        {'id': 2, 'e_m': 2.011850, 'e_o_k': [0.340760, 0.272608, 0.218087, 0.174469], 'p_i': 40, 'u_i': 1.2748},
        {'id': 3, 'e_m': 3.807699, 'e_o_k': [0.780266, 0.624213, 0.499370], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 2.323533, 'e_o_k': [0.476134, 0.380907, 0.304726], 'p_i': 20, 'u_i': 3.8582},
        {'id': 5, 'e_m': 2.407392, 'e_o_k': [0.493318, 0.394654, 0.315724], 'p_i': 20, 'u_i': 1.6137},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
