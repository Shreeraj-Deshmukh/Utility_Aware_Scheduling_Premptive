"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280016, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280016, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.779430, 'e_o_k': [0.337289, 0.269831, 0.215865, 0.172692, 0.138153], 'p_i': 10, 'u_i': 3.8323},
        {'id': 1, 'e_m': 4.228996, 'e_o_k': [0.704833, 0.563866], 'p_i': 20, 'u_i': 2.6619},
        {'id': 2, 'e_m': 2.811038, 'e_o_k': [0.345619, 0.276495, 0.221196], 'p_i': 40, 'u_i': 4.8838},
        {'id': 3, 'e_m': 30.653208, 'e_o_k': [2.492617, 1.994094, 1.595275, 1.276220, 1.020976, 0.816781], 'p_i': 80, 'u_i': 1.1242},
        {'id': 4, 'e_m': 33.589330, 'e_o_k': [2.997620, 2.398096, 1.918477, 1.534781, 1.227825], 'p_i': 80, 'u_i': 3.3705},
        {'id': 5, 'e_m': 3.119998, 'e_o_k': [0.317073, 0.253658, 0.202927, 0.162341], 'p_i': 40, 'u_i': 2.3409},
        {'id': 6, 'e_m': 6.068545, 'e_o_k': [1.011424, 0.809139], 'p_i': 80, 'u_i': 3.0130},
        {'id': 7, 'e_m': 1.834428, 'e_o_k': [0.163710, 0.130968, 0.104775, 0.083820, 0.067056], 'p_i': 10, 'u_i': 4.5858},
    ]
    B_BUDGET = 215.280016
    return processors, tasks, B_BUDGET
