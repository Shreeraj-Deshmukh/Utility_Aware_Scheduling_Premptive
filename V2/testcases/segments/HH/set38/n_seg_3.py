"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.141191, 'e_o_k': [1.228552, 0.982842, 0.786273], 'p_i': 10, 'u_i': 2.6411},
        {'id': 1, 'e_m': 2.391844, 'e_o_k': [1.372370, 1.097896, 0.878317], 'p_i': 20, 'u_i': 4.9928},
        {'id': 2, 'e_m': 6.358508, 'e_o_k': [3.648324, 2.918659, 2.334927], 'p_i': 40, 'u_i': 3.9733},
        {'id': 3, 'e_m': 4.020499, 'e_o_k': [2.306843, 1.845475, 1.476380], 'p_i': 80, 'u_i': 1.2745},
        {'id': 4, 'e_m': 0.589014, 'e_o_k': [0.337959, 0.270367, 0.216294], 'p_i': 10, 'u_i': 1.8926},
        {'id': 5, 'e_m': 2.500170, 'e_o_k': [1.434524, 1.147619, 0.918095], 'p_i': 40, 'u_i': 4.4301},
        {'id': 6, 'e_m': 4.620754, 'e_o_k': [2.651252, 2.121002, 1.696801], 'p_i': 40, 'u_i': 2.8023},
        {'id': 7, 'e_m': 0.201453, 'e_o_k': [0.115588, 0.092470, 0.073976], 'p_i': 10, 'u_i': 1.0101},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
