"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.950986, 'e_o_k': [0.451010, 0.360808, 0.288646, 0.230917], 'p_i': 10, 'u_i': 1.4304},
        {'id': 1, 'e_m': 4.937204, 'e_o_k': [2.056189, 1.644951, 1.315961, 1.052769, 0.842215], 'p_i': 20, 'u_i': 2.0301},
        {'id': 2, 'e_m': 6.848037, 'e_o_k': [2.851990, 2.281592, 1.825274, 1.460219, 1.168175], 'p_i': 40, 'u_i': 4.4775},
        {'id': 3, 'e_m': 11.426349, 'e_o_k': [4.336046, 3.468837, 2.775069, 2.220056, 1.776044, 1.420836], 'p_i': 80, 'u_i': 1.0830},
        {'id': 4, 'e_m': 6.813635, 'e_o_k': [5.299494, 4.239595], 'p_i': 80, 'u_i': 1.9156},
        {'id': 5, 'e_m': 4.707239, 'e_o_k': [1.786293, 1.429034, 1.143228, 0.914582, 0.731666, 0.585332], 'p_i': 80, 'u_i': 2.8864},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
