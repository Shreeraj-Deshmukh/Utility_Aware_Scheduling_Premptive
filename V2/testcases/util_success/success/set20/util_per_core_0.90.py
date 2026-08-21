"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279998, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279998, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.822505, 'e_o_k': [0.430376, 0.344301, 0.275441, 0.220352, 0.176282], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 3.181397, 'e_o_k': [0.258701, 0.206960, 0.165568, 0.132455, 0.105964, 0.084771], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 7.656459, 'e_o_k': [0.941368, 0.753094, 0.602475], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 27.002955, 'e_o_k': [4.500492, 3.600394], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 1.998336, 'e_o_k': [0.178338, 0.142670, 0.114136, 0.091309, 0.073047], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 5.208099, 'e_o_k': [0.423505, 0.338804, 0.271043, 0.216835, 0.173468, 0.138774], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 22.852804, 'e_o_k': [2.039458, 1.631566, 1.305253, 1.044202, 0.835362], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 1.639103, 'e_o_k': [0.146279, 0.117023, 0.093618, 0.074895, 0.059916], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 215.279998
    return processors, tasks, B_BUDGET
