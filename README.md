# mutation_testing
## Installation

```pip3 install cosmic-ray```

## Create a new config (or use the example in the repo)

```cosmic-ray new-config```

```
cat tutorial_devide.toml

[cosmic-ray]
module-path = "devide.py"
timeout = 30.0
excluded-modules = []
test-command = "python3 -m unittest devide_test.py"

[cosmic-ray.distributor]
name = "local"
```
## Run
```
sh 1_unittest.sh
sh 2_coverage.sh
sh 3_mutation_test.sh
```
