"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.035016, 0.021010, 0.012606], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [1.239075, 0.743445, 0.446067, 0.267640, 0.160584, 0.096351], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [2.360003, 1.416002], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [3.212394, 1.927436, 1.156462, 0.693877], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [12.288312, 7.372987, 4.423792, 2.654275], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.053392, 0.032035, 0.019221, 0.011533], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.938528, 0.563117, 0.337870, 0.202722], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [4.207279, 2.524368, 1.514621], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
