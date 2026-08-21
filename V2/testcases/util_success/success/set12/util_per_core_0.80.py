"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359991, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359991, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.294033, 'e_o_k': [0.382339, 0.305871], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 7.547511, 'e_o_k': [1.257918, 1.006335], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 10.700955, 'e_o_k': [1.315691, 1.052553, 0.842042], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 33.938493, 'e_o_k': [3.028780, 2.423024, 1.938419, 1.550736, 1.240588], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 2.198993, 'e_o_k': [0.270368, 0.216294, 0.173036], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.297929, 'e_o_k': [0.026588, 0.021270, 0.017016, 0.013613, 0.010890], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 6.595823, 'e_o_k': [0.536350, 0.429080, 0.343264, 0.274611, 0.219689, 0.175751], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 7.533780, 'e_o_k': [0.672339, 0.537871, 0.430297, 0.344237, 0.275390], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 191.359991
    return processors, tasks, B_BUDGET
