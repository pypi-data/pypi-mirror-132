## Python Alogger

### Usage

```
from Alogger import Alogger
logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL, log_to_file=True, log_file_type="txt")

logger.fatal("fatal")
logger.error("error")
logger.warning("warning")
logger.info("info")
logger.debug("debug")
logger.trace("trace")
logger.test("test")
```
