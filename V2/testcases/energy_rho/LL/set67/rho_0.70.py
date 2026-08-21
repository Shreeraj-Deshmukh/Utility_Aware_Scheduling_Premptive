"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 49.680006, "H": 80, "J": 24, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1067, "set": 67, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 49.680006, "H": 80, "J": 24, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1067, "set": 67, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.811128, 'e_o_k': [0.269385, 0.215508, 0.172406, 0.137925, 0.110340], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.050717, 'e_o_k': [0.008590, 0.006872, 0.005498, 0.004398], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 2.544213, 'e_o_k': [0.706726, 0.565381], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 1.179546, 'e_o_k': [0.327652, 0.262121], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 1.744117, 'e_o_k': [0.357401, 0.285921, 0.228737], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 0.579467, 'e_o_k': [0.160963, 0.128770], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 4.549467, 'e_o_k': [0.932268, 0.745814, 0.596651], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.342286, 'e_o_k': [0.070141, 0.056112, 0.044890], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 49.680006
    return processors, tasks, B_BUDGET
