# uMonitor

This is a minimalistic python supervisor for your 
microservices.  
Once started, it will launch all the services you've specified 
in the provided config file, and monitor their execution.
Suppose you have following services in the `config.json`:
```json
{
    "services" : [
        {
            "comment": "Another service to run and monitor.",
            "program" : "python3",
            "args" : ["other_script.py"],
            "persist"  : true,
            "cwd" : "/opt"
        },
        {
            "comment": "And this one should not be restarted",
            "program" : "bash",
            "args" : ["will_be_executed_with_bin_bash.sh"],
            "persist" : false,
            "cwd" : "/opt"
        }
    ]
}
```
Then the supervisor (uMonitor) will run the specified commands
and for those which have `persis` set, will restart the described
processes, whenever they fail/crash.

More complex: it also provides environment variables and venv-like
behavior for the specified programs. See the `config_example.json`
for more details.

```json
{
    "comment": "Treat this as virtual environment, but not only for python.",
    "interpreters" : {
        "python3" : "/venv_some/bin/python3",
        "sh" : "/bin/sh",
        "bash" : "/bin/bash"
    },

    "comment": "Services to run and monitor.",
    "services" : [
        {
            "program" : "python3",
            "args" : ["script_1.py"],
            "comment": "Do not recover after crashes",
            "persist" : false,
            "cwd" : "/opt",
            "env" : {
                "PYTHONPATH" : [
                    "/opt/your_python_module/",
                    "/usr/local/another/module/",
                    "/joined_with/colon/will_be"
                ],
                "PATH": [
                    "/opt/prog_1/bin/",
                    "/home/username/.prog_2/bin/",
                    "/joined_with/colon/will_be"
                ],
                "ENVIRON_VARIABLE": [
                    "SINGLE_VALUE_42"
                ]
            }
        },
        {
            "comment": "Another service to run and monitor.",
            "program" : "python3",
            "args" : ["other_script.py"],
            "persist"  : true,
            "cwd" : "/opt"
        },
        {
            "comment": "And this one should not be restarted",
            "program" : "bash",
            "args" : ["will_be_executed_with_bin_bash.sh"],
            "persist" : false,
            "cwd" : "/opt"
        }
    ]
}
```
## Installation:

- Installation using pip:
```shell
python3 -m pip install umonitor
```

- Installation using poetry:
```shell
poetry add umonitor
```


## Usage example:

- As a callable module:
```shell
python3 -m umonitor config.json
```

- In a script:
```python
import umonitor

monitor = umonitor.uMonitor("config.json")
monitor.run()
```
