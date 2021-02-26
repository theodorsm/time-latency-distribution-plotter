# RTT-PLOTTER

A basic script used for plotting round-trip-times from ping.
Useful for getting a quick insight into the state of a link.

## Requirements

- python >=3.3 (venv)
- pip

## Running

### Getting started

```bash
# Initial setup (once)
python -m venv venv
pip install -r requirements.txt

# Activate (everytime)
source venv/bin/activate
```

### Example

```bash
./generate_rtt.sh -c 10 -d 10.0.0.1
```

Plot will be saved as `./plots/PLOT_<TIMESTAMP>.png` and log file with data is found under `./rt_log/<TIMESTAMP>.log`

![Example plot](./example_out.png)

## TODO

- [ ] Add CPU & RAM usage
- [ ] Add jitter measurement
- [ ] Add standard deviation
- [ ] Use iperf(?)
