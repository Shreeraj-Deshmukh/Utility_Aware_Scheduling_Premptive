"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360002, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360002, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.424148, 'e_o_k': [0.359757, 0.287806, 0.230245, 0.184196, 0.147356, 0.117885], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 4.199296, 'e_o_k': [0.699883, 0.559906], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.511003, 'e_o_k': [0.045604, 0.036483, 0.029186, 0.023349, 0.018679], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 12.324426, 'e_o_k': [1.002181, 0.801745, 0.641396, 0.513117, 0.410493, 0.328395], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 6.514510, 'e_o_k': [0.800964, 0.640772, 0.512617], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 3.585400, 'e_o_k': [0.364370, 0.291496, 0.233197, 0.186557], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 29.194823, 'e_o_k': [2.374026, 1.899221, 1.519377, 1.215501, 0.972401, 0.777921], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 2.447883, 'e_o_k': [0.218457, 0.174766, 0.139812, 0.111850, 0.089480], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 191.360002
    return processors, tasks, B_BUDGET
