from pathlib import Path

from gsuid_core.data_store import get_res_path

# 主路径
MAIN_PATH = get_res_path() / "AT_Tracker"

# 配置文件
CONFIG_PATH = MAIN_PATH / "config.json"

# 记录数据
RECORD_PATH = MAIN_PATH / "records"

# 头像缓存
AVATAR_CACHE_PATH = MAIN_PATH / "avatar_cache"


def init_dir():
    """初始化所有必要的目录"""
    for path in [MAIN_PATH, RECORD_PATH, AVATAR_CACHE_PATH]:
        path.mkdir(parents=True, exist_ok=True)


init_dir()
