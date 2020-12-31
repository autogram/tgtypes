import json
from abc import abstractmethod
from pathlib import Path
from typing import Any, Coroutine, Dict, Optional

from tgtypes.interfaces.resolvercache import IResolverCache, T
import sys

from tgtypes.utils.async_lazy_dict import AsyncLazyDict


class JsonFileResolverCache(AsyncLazyDict, IResolverCache):
    DEFAULT_PATH = Path.cwd() / ".botkitcache" / "resolver-cache.json"

    def __init__(self, file_path: Optional[Path] = None):
        super().__init__()
        self.file_path = file_path or JsonFileResolverCache.DEFAULT_PATH
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self._is_initialized: bool = False

    async def dump_data(self):
        self.file_path.write_text(json.dumps(self))

    async def ensure_initialized(self) -> None:
        if self._is_initialized:
            return
        data: Dict = json.loads(self.file_path.read_text()) if self.file_path.exists() else {}
        self.update(**data)
        self._is_initialized = True


if "haps" in sys.modules:
    import traceback

    try:
        import haps

        haps.egg("json")(JsonFileResolverCache)
        haps.scope(haps.INSTANCE_SCOPE)(JsonFileResolverCache)
    except:
        traceback.print_exc()
