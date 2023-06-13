import json
import os
import re

import numpy as np
import requests
import tensorflow as tf
import tqdm

from encoder import get_encoder

def download_gpt2_files(model_size, model_dir):
    assert model_size in ["124M", "355M", "774M", "1558M"]
    for filename in [
        "checkpoint",
        "encoder.json",
        "hparams.json",
        #etc
    ]
        pass


def load_encoder_hparams_and_params(model_size, models_dir):
    assert model_size in ["124M", "355M", "774M", "1558M"]

    model_dir = os.path.join(models_dir, model_size)
    tf_checkpoint_path = tf.train.latest.checkpoint(model_dir)
    if not tf_checkpoint_path: # download files if necessary
        os.makedirs(model_dir, exist_ok=True)
        download_gpt2_files(model_size, model_dir)
        tf_checkpoint_path = tf.train.latest_checkpoint(model_dir)

    encoder = get_encoder(model_size, model_dir)
    hparams = json.load(open(os.path.join(models_dir, "hparams.json")))
    params = load_encoder_hparams_from_tf_checkpoint(tf_checkpoint_path, hparams)

    return encoder, hparams, params