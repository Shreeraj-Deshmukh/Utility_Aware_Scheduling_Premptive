"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 51.52, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.8, "seed": 1096, "set": 96, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 51.52, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.8, "seed": 1096, "set": 96, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.252893, 'e_o_k': [0.070248, 0.056199], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.097609, 'e_o_k': [0.020002, 0.016002, 0.012801], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 5.092114, 'e_o_k': [1.414476, 1.131581], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 3.280589, 'e_o_k': [0.444611, 0.355689, 0.284551, 0.227641, 0.182113, 0.145690], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 2.269701, 'e_o_k': [0.630473, 0.504378], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 3.382746, 'e_o_k': [0.572958, 0.458367, 0.366693, 0.293355], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 0.542314, 'e_o_k': [0.080663, 0.064531, 0.051624, 0.041300, 0.033040], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.186349, 'e_o_k': [0.038186, 0.030549, 0.024439], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 51.520000
    return processors, tasks, B_BUDGET
