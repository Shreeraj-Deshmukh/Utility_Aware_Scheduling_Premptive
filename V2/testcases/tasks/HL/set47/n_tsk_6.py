"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.185113, 'e_o_k': [0.884754, 0.707803], 'p_i': 10, 'u_i': 1.2617},
        {'id': 1, 'e_m': 2.093692, 'e_o_k': [0.283753, 0.227003, 0.181602, 0.145282, 0.116225, 0.092980], 'p_i': 20, 'u_i': 4.5683},
        {'id': 2, 'e_m': 3.410608, 'e_o_k': [0.462232, 0.369786, 0.295829, 0.236663, 0.189330, 0.151464], 'p_i': 40, 'u_i': 2.4732},
        {'id': 3, 'e_m': 7.341214, 'e_o_k': [0.994939, 0.795951, 0.636761, 0.509409, 0.407527, 0.326021], 'p_i': 80, 'u_i': 3.5676},
        {'id': 4, 'e_m': 2.542005, 'e_o_k': [0.706112, 0.564890], 'p_i': 20, 'u_i': 2.3263},
        {'id': 5, 'e_m': 1.453470, 'e_o_k': [0.403742, 0.322993], 'p_i': 20, 'u_i': 1.7445},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
