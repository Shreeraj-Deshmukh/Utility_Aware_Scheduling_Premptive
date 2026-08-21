"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199978, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199978, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.977059, 'e_o_k': [0.160768, 0.128614, 0.102891, 0.082313, 0.065851, 0.052680], 'p_i': 10, 'u_i': 2.0118},
        {'id': 1, 'e_m': 9.292577, 'e_o_k': [1.548763, 1.239010], 'p_i': 20, 'u_i': 3.2457},
        {'id': 2, 'e_m': 16.530398, 'e_o_k': [1.679918, 1.343935, 1.075148, 0.860118], 'p_i': 40, 'u_i': 3.0175},
        {'id': 3, 'e_m': 10.488903, 'e_o_k': [0.936063, 0.748851, 0.599081, 0.479264, 0.383412], 'p_i': 80, 'u_i': 1.7336},
        {'id': 4, 'e_m': 2.745331, 'e_o_k': [0.278997, 0.223198, 0.178558, 0.142846], 'p_i': 10, 'u_i': 3.3772},
        {'id': 5, 'e_m': 0.264434, 'e_o_k': [0.032512, 0.026010, 0.020808], 'p_i': 10, 'u_i': 1.0712},
        {'id': 6, 'e_m': 24.013775, 'e_o_k': [2.440424, 1.952339, 1.561872, 1.249497], 'p_i': 80, 'u_i': 4.5626},
        {'id': 7, 'e_m': 7.685811, 'e_o_k': [0.685906, 0.548725, 0.438980, 0.351184, 0.280947], 'p_i': 40, 'u_i': 2.4112},
    ]
    B_BUDGET = 239.199978
    return processors, tasks, B_BUDGET
