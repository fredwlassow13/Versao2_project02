import time
import os
import json

DEFAULT_TTL = 60

class Cache:
    def __init__(self, cache_file=None, default_ttl=DEFAULT_TTL):
        self.cache_file = cache_file
        self.default_ttl = default_ttl
        if cache_file and os.path.exists(cache_file):
            self._load_file()
        else:
            self._data = {}
    def _load_file(self):
        with open(self.cache_file, "r") as f:
            self._data = json.load(f)
    def _save_file(self):
        if self.cache_file:
            with open(self.cache_file, "w") as f:
                json.dump(self._data, f)

    def set(self, key, value, ttl=None):
        expire_at = time.time() + (ttl or self.default_ttl)
        self._data[key] = {"value": value, "expire_at": expire_at}
        self._save_file()

    def get(self, key):
        entry = self._data.get(key)
        if not entry:
            return None

        if time.time() < entry["expire_at"]:
            return entry["value"]
        else:
            del self._data[key]
            self._save_file()
            return None

    def _cache_in_memory(self, key, value, expire_at):
        cache[key] = (value, expire_at)

    def clear_cache(self):
        self._data.clear()
        if self.cache_file:
            self.save_file()

    def delete(self, key):
        if key in self._data:
            del self._data[key]