import spell.metrics as metrics
import time
import argparse

# Runs for --steps seconds and sends --steps spell metrics with the key 'value'
# and a numeric value starting at --start and incrementing by --stepsize
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default=0, type=float, help="Value to start at")
    parser.add_argument("--steps", default=1000000, type=int, help="Number of metrics to send")
    parser.add_argument("--stepsize", default=1, type=float, help="Size of step to take")
    args = parser.parse_args()

    value = args.start
    for i in range(args.steps):
        metrics.send_metric("value", value)
        value += args.stepsize
