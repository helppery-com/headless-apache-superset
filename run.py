import os
os.environ["SUPERSET_CONFIG_PATH"] = "%s/config.py" % os.path.dirname(__file__)
from superset.cli import superset

superset()
