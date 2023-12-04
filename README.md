# Celery-multi-example

## Start
```bash
docker-compose up -d
```

## ready to monitoring
### FLOWER
localhost:5556

### API server
localhost:8888
### request
localhost:8888/req

## Method
1. open flower(localhost:5556) and check 4 workers
2. open new browser(localhost:8888) and check page content ('{"result": "hi"}')
3. in 2. change domain to localhost:8888/req
4. in 3. refresh many times
5. in flower page. Check the increased processed count
