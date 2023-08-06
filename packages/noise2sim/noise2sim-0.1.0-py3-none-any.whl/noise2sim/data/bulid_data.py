from noise2sim.data.datasets.data_lmdb import LMDB
from noise2sim.data.datasets.bsd_npy import BSDNPY
from noise2sim.data.datasets.data_mayo import Mayo
from noise2sim.data.datasets.data_SCT import SCT


def build_dataset(data_cfg_ori):
    data_cfg = data_cfg_ori.copy()
    data_type = data_cfg.pop("type")
    dataset = None

    if data_type == "lmdb":
        dataset = LMDB(**data_cfg)
    elif data_type == "bsd_npy":
        dataset = BSDNPY(**data_cfg)
    elif data_type == "mayo":
        dataset = Mayo(**data_cfg)
    elif data_type == "sct":
        dataset = SCT(**data_cfg)
    else:
        assert TypeError

    return dataset