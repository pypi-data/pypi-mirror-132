# Paips
Run complex Python pipelines from command line using configuration files.

### How it works
- First define tasks that you want to be executed. These tasks are written in Python and consist of classes inheriting from paips.core.Task. Tasks can receive parameters and data from other tasks, return data, and be interconnected.
- Then, write one or more configuration files, which will tell Paips which tasks to run, with which parameters and how they will be connected. Configuration files are written in yaml, are modular and can be easily composed and also modified from command line.
- Finally, run in command line:
```
paiprun <config_path>
```
and the tasks declared in the configuration file will be executed in the right order.

Now, hands on pipelining...

Installing paips is really easy, just run:

```
pip install paips
```

Now that paips is installed, take a look at the [Tutorial](docs/tutorial.md) to learn how to make your life easier when building those large and complex pipelines.







