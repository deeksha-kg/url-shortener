from app.utils.shortener import generate_short_code
from app.repositories.url_repository import save, get, exists,get_by_original_url
from app.cache import redis_client
from datetime import datetime

TTL = 24 * 60 * 60  # 24 hours


def create_short_url(original_url: str):

    # Check PostgreSQL first
    existing_url = get_by_original_url(original_url)

    if existing_url is not None:

        # Make sure it is also available in Redis
        redis_client.setex(
            existing_url.short_code,
            TTL,
            existing_url.original_url
        )

        return {
            "original_url": existing_url.original_url,
            "short_code": existing_url.short_code,
            "short_url": f"/{existing_url.short_code}"
        }

    # URL doesn't exist, so generate a new short code
    short_code = generate_short_code()

    while exists(short_code):
        short_code = generate_short_code()

    # Store in Redis
    redis_client.setex(
        short_code,
        TTL,
        original_url
    )

    # Store in PostgreSQL
    save(short_code, original_url)

    return {
        "original_url": original_url,
        "short_code": short_code,
        "short_url": f"/{short_code}"
    }

def get_original_url(short_code: str):

    # 1. Check Redis first
    cached_url = redis_client.get(short_code)

    if cached_url is not None:
        return cached_url

    # 2. Redis miss → check PostgreSQL
    url = get(short_code)

    if url is None:
        return None

    if url.expires_at <= datetime.utcnow():
        return None
    # 3. Put PostgreSQL result back into Redis -- cache aside pattern
    redis_client.setex(
        short_code,
        TTL,
        url.original_url
    )

    # 4. Return URL
    return url.original_url