"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.368544, 'e_o_k': [0.139080, 0.111264, 0.089011, 0.071209], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 7.519201, 'e_o_k': [0.924492, 0.739594, 0.591675], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.706074, 'e_o_k': [0.138732, 0.110986, 0.088789, 0.071031, 0.056825, 0.045460], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.511622, 'e_o_k': [0.185855, 0.148684, 0.118947], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 3.122761, 'e_o_k': [0.317354, 0.253883, 0.203106, 0.162485], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 1.112132, 'e_o_k': [0.136737, 0.109390, 0.087512], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.471119, 'e_o_k': [0.078520, 0.062816], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 6.671274, 'e_o_k': [1.111879, 0.889503], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 119.600007
    return processors, tasks, B_BUDGET
