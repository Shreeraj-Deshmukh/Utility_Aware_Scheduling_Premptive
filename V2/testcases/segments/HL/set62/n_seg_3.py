"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.118502, 'e_o_k': [0.434119, 0.347295, 0.277836], 'p_i': 10, 'u_i': 2.6711},
        {'id': 1, 'e_m': 1.874501, 'e_o_k': [0.384119, 0.307295, 0.245836], 'p_i': 20, 'u_i': 2.3833},
        {'id': 2, 'e_m': 1.286629, 'e_o_k': [0.263654, 0.210923, 0.168738], 'p_i': 40, 'u_i': 4.1647},
        {'id': 3, 'e_m': 1.712942, 'e_o_k': [0.351013, 0.280810, 0.224648], 'p_i': 80, 'u_i': 1.2796},
        {'id': 4, 'e_m': 2.907669, 'e_o_k': [0.595834, 0.476667, 0.381334], 'p_i': 10, 'u_i': 2.4526},
        {'id': 5, 'e_m': 0.484065, 'e_o_k': [0.099194, 0.079355, 0.063484], 'p_i': 10, 'u_i': 3.7482},
        {'id': 6, 'e_m': 7.564502, 'e_o_k': [1.550103, 1.240082, 0.992066], 'p_i': 80, 'u_i': 2.1247},
        {'id': 7, 'e_m': 0.284703, 'e_o_k': [0.058341, 0.046673, 0.037338], 'p_i': 40, 'u_i': 4.6336},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
