"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.256635, 'e_o_k': [0.147249, 0.117800, 0.094240], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.540076, 'e_o_k': [0.309880, 0.247904, 0.198323], 'p_i': 20, 'u_i': 2.1078},
        {'id': 2, 'e_m': 0.758738, 'e_o_k': [0.435341, 0.348273, 0.278619], 'p_i': 40, 'u_i': 4.2406},
        {'id': 3, 'e_m': 16.196605, 'e_o_k': [9.293134, 7.434507, 5.947606], 'p_i': 80, 'u_i': 1.1754},
        {'id': 4, 'e_m': 10.131188, 'e_o_k': [5.812977, 4.650382, 3.720305], 'p_i': 40, 'u_i': 3.4237},
        {'id': 5, 'e_m': 6.084943, 'e_o_k': [3.491361, 2.793089, 2.234471], 'p_i': 40, 'u_i': 1.7653},
        {'id': 6, 'e_m': 0.825239, 'e_o_k': [0.473498, 0.378798, 0.303039], 'p_i': 10, 'u_i': 3.9977},
        {'id': 7, 'e_m': 0.759590, 'e_o_k': [0.435830, 0.348664, 0.278931], 'p_i': 20, 'u_i': 1.6134},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
