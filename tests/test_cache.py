import pytest
import time
from project_02.cache import Cache

def test_cache_set_get():
    cache = Cache()
    cache.set("ari", "nen", ttl=3)
    assert cache.get("ari") == "nen"

def test_cache_set_get_expired():
    cache = Cache()
    cache.set("ari", "nen", ttl=1)
    time.sleep(4)
    assert cache.get("ari") is None

def test_cache_set_get_overwrite():
    cache = Cache()
    cache.set("ari", "nen", ttl=4)
    cache.set("ari", "nen", ttl=4)
    assert cache.get("ari") == "nen"

def test_cache_set_get_delete():
    cache = Cache()
    cache.set("ari", "nen", ttl=2)
    cache.delete("ari")
    assert cache.get("ari") is None

def test_cache_set_get_clear():
    cache = Cache()
    cache.set("ari", "nen", ttl=4)
    cache.set("ton", "aiu", ttl=4)
    cache.clear_cache()
    assert cache.get("ari") is None
    assert cache.get("ton") is None

def test_get_nonexist_key():
    cache = Cache()
    result = cache.get("chave_inexistente")
    assert result is None

def test_get_expired_key():
    cache = Cache()
    cache.set("ari", "nen", ttl=1)
    time.sleep(1)
    assert cache.get("ari") is None

def test_delete_nonexist_key():
    cache = Cache()
    cache.clear_cache()
    assert cache._data == {}

def test_clear_empty_cache():
    cache = Cache()
    cache.clear_cache()
    assert cache._data == {}
