"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.078517, 'e_o_k': [0.281697, 0.225357, 0.180286, 0.144229, 0.115383, 0.092306], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 0.654353, 'e_o_k': [0.088683, 0.070946, 0.056757, 0.045406, 0.036325, 0.029060], 'p_i': 20, 'u_i': 3.9685},
        {'id': 2, 'e_m': 1.726347, 'e_o_k': [0.479541, 0.383633], 'p_i': 40, 'u_i': 1.4001},
        {'id': 3, 'e_m': 4.516779, 'e_o_k': [0.765037, 0.612030, 0.489624, 0.391699], 'p_i': 80, 'u_i': 2.1780},
        {'id': 4, 'e_m': 2.027836, 'e_o_k': [0.415540, 0.332432, 0.265946], 'p_i': 80, 'u_i': 3.8388},
        {'id': 5, 'e_m': 2.757147, 'e_o_k': [0.466996, 0.373597, 0.298878, 0.239102], 'p_i': 80, 'u_i': 1.0041},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
