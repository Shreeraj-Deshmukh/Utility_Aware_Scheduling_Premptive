"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.252893, 'e_o_k': [0.221282, 0.132769], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.097609, 'e_o_k': [0.069721, 0.041833, 0.025100], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 5.092114, 'e_o_k': [4.455600, 2.673360], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 3.280589, 'e_o_k': [1.927038, 1.156223, 0.693734, 0.416240, 0.249744, 0.149846], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 2.269701, 'e_o_k': [1.985989, 1.191593], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 3.382746, 'e_o_k': [2.176399, 1.305839, 0.783504, 0.470102], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 0.542314, 'e_o_k': [0.329303, 0.197582, 0.118549, 0.071129, 0.042678], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.186349, 'e_o_k': [0.133106, 0.079864, 0.047918], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
