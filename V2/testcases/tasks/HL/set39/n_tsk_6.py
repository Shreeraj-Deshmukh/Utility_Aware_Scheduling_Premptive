"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.602748, 'e_o_k': [0.123514, 0.098811, 0.079049], 'p_i': 10, 'u_i': 4.0696},
        {'id': 1, 'e_m': 5.070740, 'e_o_k': [1.408539, 1.126831], 'p_i': 20, 'u_i': 1.5844},
        {'id': 2, 'e_m': 2.297287, 'e_o_k': [0.638135, 0.510508], 'p_i': 40, 'u_i': 4.9877},
        {'id': 3, 'e_m': 26.256921, 'e_o_k': [7.293589, 5.834871], 'p_i': 80, 'u_i': 3.4936},
        {'id': 4, 'e_m': 0.797956, 'e_o_k': [0.135155, 0.108124, 0.086499, 0.069199], 'p_i': 80, 'u_i': 4.0270},
        {'id': 5, 'e_m': 0.905700, 'e_o_k': [0.153405, 0.122724, 0.098179, 0.078543], 'p_i': 10, 'u_i': 3.7051},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
