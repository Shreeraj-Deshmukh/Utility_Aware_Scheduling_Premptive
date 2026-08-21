"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279989, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279989, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.785432, 'e_o_k': [0.145185, 0.116148, 0.092919, 0.074335, 0.059468, 0.047574], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 2.362339, 'e_o_k': [0.240075, 0.192060, 0.153648, 0.122918], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 16.959566, 'e_o_k': [1.379096, 1.103276, 0.882621, 0.706097, 0.564878, 0.451902], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 38.524782, 'e_o_k': [6.420797, 5.136638], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 1.921660, 'e_o_k': [0.320277, 0.256221], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 7.453426, 'e_o_k': [0.757462, 0.605970, 0.484776, 0.387821], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 4.137270, 'e_o_k': [0.336429, 0.269143, 0.215315, 0.172252, 0.137801, 0.110241], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 13.405868, 'e_o_k': [2.234311, 1.787449], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 215.279989
    return processors, tasks, B_BUDGET
