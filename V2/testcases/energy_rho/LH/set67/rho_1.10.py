"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 93.472001, "H": 80, "J": 24, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1067, "set": 67, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}
"""

_SPEC = '{"B": 93.472001, "H": 80, "J": 24, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1067, "set": 67, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.811128, 'e_o_k': [0.754277, 0.603422, 0.482737, 0.386190, 0.308952], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.050717, 'e_o_k': [0.024053, 0.019242, 0.015394, 0.012315], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 2.544213, 'e_o_k': [1.978832, 1.583066], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 1.179546, 'e_o_k': [0.917424, 0.733940], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 1.744117, 'e_o_k': [1.000723, 0.800578, 0.640463], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 0.579467, 'e_o_k': [0.450696, 0.360557], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 4.549467, 'e_o_k': [2.610350, 2.088280, 1.670624], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.342286, 'e_o_k': [0.196394, 0.157115, 0.125692], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 93.472001
    return processors, tasks, B_BUDGET
