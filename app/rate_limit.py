import time
from collections import defaultdict
from threading import Lock


class InMemoryRateLimiter:
    def __init__(self, max_requests: int = 60, window_seconds: int = 60) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests: dict[str, list[float]] = defaultdict(list)
        self._lock = Lock()

    def allow(self, key: str) -> bool:
        now = time.time()
        with self._lock:
            requests = self._requests[key]
            requests[:] = [ts for ts in requests if now - ts < self.window_seconds]
            if len(requests) >= self.max_requests:
                return False
            requests.append(now)
            return True
