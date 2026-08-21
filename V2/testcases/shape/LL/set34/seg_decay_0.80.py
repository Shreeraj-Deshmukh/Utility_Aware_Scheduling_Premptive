"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200016, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 55.200016, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.109720, 'e_o_k': [0.022484, 0.017987, 0.014390], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 0.572679, 'e_o_k': [0.077614, 0.062091, 0.049673, 0.039738, 0.031791, 0.025433], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 5.630863, 'e_o_k': [1.153865, 0.923092, 0.738474], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 3.715241, 'e_o_k': [0.761320, 0.609056, 0.487245], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 1.331561, 'e_o_k': [0.272861, 0.218289, 0.174631], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 1.635691, 'e_o_k': [0.454358, 0.363487], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.014189, 'e_o_k': [0.001923, 0.001538, 0.001231, 0.000985, 0.000788, 0.000630], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 0.653569, 'e_o_k': [0.097211, 0.077769, 0.062215, 0.049772, 0.039818], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 55.200016
    return processors, tasks, B_BUDGET
