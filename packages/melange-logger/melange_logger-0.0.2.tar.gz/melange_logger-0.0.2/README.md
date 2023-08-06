# tpc_logger
Logging system for the TPC software.
------------------------------------
The TPC Logger class provides a singleton for logging information within C++ code or in the python API.  The class *Logger* contains an instance of spdlog::logger for both printing to the console (s_ConsoleLogger) and for logging to a file (s_FileLogger).  There are four basic log levels:
```c++
Logger::info("Generic information...");
Logger::trace("Stack trace level of information...");
Logger::warn("Warning! Don't do what you're thinking of doing!");
Logger::error("ERROR! Program crashing!");
```
Logs which are saved to file utilize a revolving file structure in a hidden folder *.logs* which is created wherever the code is run.  Running the pytest example generates a file called *log.log* whose entries look like:
```bash
[08:36:07] [info] File: GHDAYVXHMKXWSUAHDIVSSMQRG
[08:36:07] [info] File: MDDKVVRIPLFIJNWXOMHLHXECIPJLUJAPSIMDRJHDSSUAXDTMUGEWMYJNZSSISIVKRXNJLVEPZJFNFYFBEREGPAPQCSU
[08:36:07] [info] File: XGEAJZRSKZCRMWQVZABADVBZCQLMBPYKWSOVZDLFXMIUMD
```
### Performance
---------------
Below are some benchmarks of performance within the python API.  The source code that generates the plot below is in the /app/ directory of the main branch.  The code runs a simple function that adds two numbers and either calls a generic logging message (*tpc_logger.info("Adding x + y")*) or doesn't.  The two curves below show the difference <img src="https://render.githubusercontent.com/render/math?math=%5CDelta%20t"> between calling the logging function and not calling it (*log - no log*) and between asking whether to call it with a debug parameter and not calling it (*debug - no log*).  Each of these calls happens within a for loop, and the number of times is given by *N*.  The average call time is computed by taking the difference between the two curves and dividing by *N* (i.e. the number of calls).  The error bars are the error on the mean as computed for ten trials for each value of *N*.

<img src="/app/speed_test.png" alt="speed test"/>

### Installation
Some minimum requirements must be met in order to install:
#### Required Packages
 - cmake (latest version)
 - python (>= 3.7)
 - pytest (for testing)

Once dependencies have been met, clone the repo along with its submodules
```bash
git clone --recurse-submodules https://github.com/UC-Davis-Machine-Learning/tpc_logger.git
```
or 
```bash
git clone https://github.com/UC-Davis-Machine-Learning/tpc_logger.git
cd tpc_logger
git submodule init
git submodule update
```

To install, run the setup.py script:
```bash
python setup.py install
```
This will run cmake to compile the project and generate the python library.  The default settings set the logger to only output to the log file, the console logger is turned off by default (*CONSOLE_LOGGER=OFF*).  Unit tests are enabled by default, but can be turned off by swtiching *BUILD_TESTS=OFF*.  To run the tests, either go to the "tests" directory and issue:
```bash
pytest .
```
or, go to the build directory (probably "build/temp.[environment]") and issue,
```bash
ctest
```

### C++ usage
To use within a C++ class, first include the header *Logger.hh*.  You can then invoke the log level commands:
```c++
#include "Logger.hh"

// some condition causes an error
if (condition == true)
{
    Logger::error("ERROR! generic error message ...");
}

// store/print some generic info
Logger::info("Calling function foo()");
foo();
```

#### Python
Basic usage in python is to first import *tpc_logger* which returns an instance of the singleton class.  Then, issue one of the four log level commands:
```python
import tpc_logger as logger
import sys

# some condition causes an error
if (condition == True):
    logger.error("ERROR! generic error message ...")
    sys.exit()

# store/print some generic info
logger.info("Calling funcion bar()")
bar()
```


