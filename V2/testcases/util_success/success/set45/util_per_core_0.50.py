"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600018, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600018, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.136964, 'e_o_k': [0.189494, 0.151595], 'p_i': 10, 'u_i': 3.2915},
        {'id': 1, 'e_m': 2.062020, 'e_o_k': [0.209555, 0.167644, 0.134115, 0.107292], 'p_i': 20, 'u_i': 3.4234},
        {'id': 2, 'e_m': 1.698382, 'e_o_k': [0.172600, 0.138080, 0.110464, 0.088371], 'p_i': 40, 'u_i': 1.9989},
        {'id': 3, 'e_m': 10.323750, 'e_o_k': [0.839493, 0.671594, 0.537276, 0.429820, 0.343856, 0.275085], 'p_i': 80, 'u_i': 4.1665},
        {'id': 4, 'e_m': 3.814835, 'e_o_k': [0.635806, 0.508645], 'p_i': 20, 'u_i': 2.8771},
        {'id': 5, 'e_m': 1.287668, 'e_o_k': [0.130861, 0.104688, 0.083751, 0.067001], 'p_i': 20, 'u_i': 3.3920},
        {'id': 6, 'e_m': 0.556235, 'e_o_k': [0.092706, 0.074165], 'p_i': 10, 'u_i': 1.7352},
        {'id': 7, 'e_m': 6.018952, 'e_o_k': [0.537151, 0.429721, 0.343776, 0.275021, 0.220017], 'p_i': 20, 'u_i': 3.3959},
    ]
    B_BUDGET = 119.600018
    return processors, tasks, B_BUDGET
