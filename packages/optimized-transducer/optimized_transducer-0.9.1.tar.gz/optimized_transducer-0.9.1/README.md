## Introduction

This project implements the optimization techniques proposed in
[Improving RNN Transducer Modeling for End-to-End Speech Recognition](https://arxiv.org/abs/1909.12415)
to reduce the memory consumption for computing transducer loss.

During the implementation, we use [torchaudio](https://github.com/pytorch/audio) as a reference.
We ensure that the transducer loss computed using this project is identical to the one computed
using torchaudio when giving the same inputs.

## Installation

You can install it via `pip`:

```
pip install optimized_transducer
```

### Installation FQA

### What operating systems are supported.

It has been tested on Ubuntu 18.04. It should work on macOS and other unixes systems.
Also, it may also work on Windows, though it is not tested.

