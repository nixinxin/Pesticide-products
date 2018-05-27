import redis
from nongyao.settings import start_urls, redis_key, REDIS_HOST
from scrapy.cmdline import execute


conn = redis.StrictRedis(host=REDIS_HOST)


def main():
    conn.lpush(redis_key, start_urls)
    execute(['scrapy', 'crawl', 'spider'])


if __name__ == '__main__':
    main()
