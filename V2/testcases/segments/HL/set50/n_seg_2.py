"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.195644, 'e_o_k': [0.332123, 0.265699], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 1.074656, 'e_o_k': [0.298516, 0.238812], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 3.707536, 'e_o_k': [1.029871, 0.823897], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 9.930702, 'e_o_k': [2.758528, 2.206823], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.251715, 'e_o_k': [0.069921, 0.055937], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 1.973974, 'e_o_k': [0.548326, 0.438661], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 23.874105, 'e_o_k': [6.631696, 5.305357], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 2.464327, 'e_o_k': [0.684535, 0.547628], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
