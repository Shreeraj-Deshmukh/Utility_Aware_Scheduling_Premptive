"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.677743, 0.542194, 0.433755], 'p_i': 10, 'u_i': 4.5874},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.521664, 0.417331, 0.333865], 'p_i': 20, 'u_i': 2.7347},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.579049, 0.463239, 0.370591], 'p_i': 40, 'u_i': 4.9671},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [3.149313, 2.519450, 2.015560], 'p_i': 80, 'u_i': 4.8761},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [1.560655, 1.248524, 0.998819], 'p_i': 80, 'u_i': 2.5248},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.081505, 0.065204, 0.052163], 'p_i': 10, 'u_i': 4.9532},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.417630, 0.334104, 0.267283], 'p_i': 40, 'u_i': 2.2979},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [1.748348, 1.398679, 1.118943], 'p_i': 40, 'u_i': 4.0423},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
