"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.342956, 'e_o_k': [0.196778, 0.157423, 0.125938], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 1.242204, 'e_o_k': [0.712740, 0.570192, 0.456154], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.024035, 'e_o_k': [0.013791, 0.011033, 0.008826], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 5.660673, 'e_o_k': [3.247927, 2.598342, 2.078674], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 4.931490, 'e_o_k': [2.829543, 2.263635, 1.810908], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 1.603581, 'e_o_k': [0.920088, 0.736070, 0.588856], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 4.803527, 'e_o_k': [2.756122, 2.204898, 1.763918], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 0.705118, 'e_o_k': [0.404576, 0.323661, 0.258929], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
