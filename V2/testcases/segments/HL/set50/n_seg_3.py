"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.195644, 'e_o_k': [0.245009, 0.196007, 0.156806], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 1.074656, 'e_o_k': [0.220216, 0.176173, 0.140938], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 3.707536, 'e_o_k': [0.759741, 0.607793, 0.486234], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 9.930702, 'e_o_k': [2.034980, 1.627984, 1.302387], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.251715, 'e_o_k': [0.051581, 0.041265, 0.033012], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 1.973974, 'e_o_k': [0.404503, 0.323602, 0.258882], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 23.874105, 'e_o_k': [4.892235, 3.913788, 3.131030], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 2.464327, 'e_o_k': [0.504985, 0.403988, 0.323190], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
