import argparse
import os
from impl_model_training import load_config, RlTlTraining, combine_into
import wandb

# parse args
parser = argparse.ArgumentParser(prog='Refinement/Transfer Learning - Training Script')
parser.add_argument('--config', type=str, required=True)
parser.add_argument('--sweep-id', type=str, required=True)
parser.add_argument('--sweep-count', type=int, required=False)
parser.add_argument('--cuda-device-nr', type=str, required=False)
parser.add_argument('--cpu-threads', type=int, required=False)
args = parser.parse_args()

def train():
    # create config
    config = load_config(args.config)
    if "project" not in config:
        config["project"] = "refinement transfer learning"

    overwritten_params = {
        "processing": {}
    }
    if args.cuda_device_nr is not None:
        overwritten_params['processing']['cuda_device_nr'] = args.cuda_device_nr
    if args.cpu_threads is not None:
        overwritten_params['processing']['num_proc'] = args.cpu_threads

    # start agent
    combine_into(overwritten_params, config)
    train_func = RlTlTraining(config)
    train_func()

wandb.agent(args.sweep_id, train, count=args.sweep_count)