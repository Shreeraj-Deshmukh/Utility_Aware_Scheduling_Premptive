"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.778125, 'e_o_k': [0.131796, 0.105437, 0.084350, 0.067480], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 1.791279, 'e_o_k': [0.242768, 0.194214, 0.155372, 0.124297, 0.099438, 0.079550], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.021926, 'e_o_k': [0.006091, 0.004872], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 9.810039, 'e_o_k': [2.010254, 1.608203, 1.286562], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 17.706132, 'e_o_k': [3.628306, 2.902645, 2.322116], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.074098, 'e_o_k': [0.012550, 0.010040, 0.008032, 0.006426], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 3.015455, 'e_o_k': [0.448515, 0.358812, 0.287050, 0.229640, 0.183712], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 2.180081, 'e_o_k': [0.369255, 0.295404, 0.236323, 0.189058], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
