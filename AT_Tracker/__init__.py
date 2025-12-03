from gsuid_core.sv import Plugins

from . import track  # noqa: F401

Plugins(name="AT_Tracker", force_prefix=["xw"], allow_empty_prefix=True)
