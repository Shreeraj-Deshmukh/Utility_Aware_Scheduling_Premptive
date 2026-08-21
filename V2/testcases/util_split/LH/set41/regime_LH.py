"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 25, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 25, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.251909, 0.201527, 0.161221], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.334014, 0.267211, 0.213769, 0.171015, 0.136812, 0.109450], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [5.916402, 4.733122], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.231750, 0.185400, 0.148320, 0.118656, 0.094925, 0.075940], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.535807, 0.428646, 0.342916], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.370208, 0.296166, 0.236933, 0.189546, 0.151637, 0.121310], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.528502, 0.422802, 0.338241], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.454107, 0.363286], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
