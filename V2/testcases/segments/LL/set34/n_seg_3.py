"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200011, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200011, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.109720, 'e_o_k': [0.022484, 0.017987, 0.014390], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 0.572679, 'e_o_k': [0.117352, 0.093882, 0.075105], 'p_i': 20, 'u_i': 3.8785},
        {'id': 2, 'e_m': 5.630863, 'e_o_k': [1.153865, 0.923092, 0.738474], 'p_i': 40, 'u_i': 2.8542},
        {'id': 3, 'e_m': 3.715241, 'e_o_k': [0.761320, 0.609056, 0.487245], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 1.331561, 'e_o_k': [0.272861, 0.218289, 0.174631], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 1.635691, 'e_o_k': [0.335182, 0.268146, 0.214517], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.014189, 'e_o_k': [0.002908, 0.002326, 0.001861], 'p_i': 40, 'u_i': 2.8369},
        {'id': 7, 'e_m': 0.653569, 'e_o_k': [0.133928, 0.107143, 0.085714], 'p_i': 10, 'u_i': 1.1432},
    ]
    B_BUDGET = 55.200011
    return processors, tasks, B_BUDGET
