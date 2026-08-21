"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439997, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439997, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.776745, 'e_o_k': [0.158562, 0.126850, 0.101480, 0.081184, 0.064947], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 2.341740, 'e_o_k': [0.190423, 0.152338, 0.121870, 0.097496, 0.077997, 0.062398], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 2.126896, 'e_o_k': [0.172952, 0.138362, 0.110689, 0.088552, 0.070841, 0.056673], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 19.998078, 'e_o_k': [3.333013, 2.666410], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 7.337313, 'e_o_k': [0.745662, 0.596530, 0.477224, 0.381779], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.946834, 'e_o_k': [0.096223, 0.076978, 0.061583, 0.049266], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 9.906227, 'e_o_k': [1.651038, 1.320830], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 1.146502, 'e_o_k': [0.191084, 0.152867], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 167.439997
    return processors, tasks, B_BUDGET
