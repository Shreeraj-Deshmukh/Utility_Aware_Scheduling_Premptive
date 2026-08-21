"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.699129, 'e_o_k': [0.330122, 0.264098, 0.211278, 0.169023, 0.135218], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.713729, 'e_o_k': [0.087754, 0.070203, 0.056162], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 2.631184, 'e_o_k': [0.234815, 0.187852, 0.150282, 0.120225, 0.096180], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 27.683787, 'e_o_k': [3.403744, 2.722995, 2.178396], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 5.439812, 'e_o_k': [0.552826, 0.442261, 0.353809, 0.283047], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 3.964013, 'e_o_k': [0.660669, 0.528535], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 2.332715, 'e_o_k': [0.208179, 0.166543, 0.133235, 0.106588, 0.085270], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 5.117280, 'e_o_k': [0.456683, 0.365346, 0.292277, 0.233821, 0.187057], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 215.280007
    return processors, tasks, B_BUDGET
