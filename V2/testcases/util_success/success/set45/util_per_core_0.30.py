"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759997, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759997, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.071377, 'e_o_k': [0.006370, 0.005096, 0.004077, 0.003261, 0.002609], 'p_i': 10, 'u_i': 1.5331},
        {'id': 1, 'e_m': 0.748369, 'e_o_k': [0.066787, 0.053430, 0.042744, 0.034195, 0.027356], 'p_i': 20, 'u_i': 4.3760},
        {'id': 2, 'e_m': 0.016864, 'e_o_k': [0.002073, 0.001659, 0.001327], 'p_i': 40, 'u_i': 3.1042},
        {'id': 3, 'e_m': 1.673290, 'e_o_k': [0.136066, 0.108853, 0.087082, 0.069666, 0.055733, 0.044586], 'p_i': 80, 'u_i': 1.7042},
        {'id': 4, 'e_m': 4.751766, 'e_o_k': [0.791961, 0.633569], 'p_i': 80, 'u_i': 1.9234},
        {'id': 5, 'e_m': 6.900084, 'e_o_k': [0.561092, 0.448874, 0.359099, 0.287279, 0.229823, 0.183859], 'p_i': 80, 'u_i': 3.4358},
        {'id': 6, 'e_m': 4.826511, 'e_o_k': [0.392476, 0.313981, 0.251185, 0.200948, 0.160758, 0.128606], 'p_i': 80, 'u_i': 1.3923},
        {'id': 7, 'e_m': 3.281266, 'e_o_k': [0.403434, 0.322747, 0.258198], 'p_i': 10, 'u_i': 3.9595},
    ]
    B_BUDGET = 71.759997
    return processors, tasks, B_BUDGET
