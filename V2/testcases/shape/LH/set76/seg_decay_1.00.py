"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319986, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319986, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.191596, 0.191596, 0.191596, 0.191596], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [1.403584, 1.403584, 1.403584], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.159234, 0.159234, 0.159234, 0.159234, 0.159234, 0.159234], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.282169, 0.282169, 0.282169], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.437186, 0.437186, 0.437186, 0.437186], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.207598, 0.207598, 0.207598], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.131913, 0.131913], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [1.867957, 1.867957], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 88.319986
    return processors, tasks, B_BUDGET
