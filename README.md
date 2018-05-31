# Rackspace-Python-Assessment-REST-API

### REST API end-Points:

GET:
```sh
curl -X GET http://127.0.0.1:5000/vehicles
```

POST:
```sh
curl -X POST \
  http://127.0.0.1:5000/vehicles \
  -H 'content-type: multipart/form-data' \
  -F brand=Boeing \
  -F speed=800mph \
  -F year=2002 \
  -F 'model=BH 7777' \
  -F type=Aeroplan \
  -F 'description=Boeing flight'
```

GET:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/1
```

PUT:
```sh
curl -X PUT \
  http://127.0.0.1:5000/vehicles/1 \
  -H 'content-type: multipart/form-data' \
  -F brand=Boeing \
  -F speed=800mph \
  -F year=2002 \
  -F 'model=BH 7777' \
  -F type=Aeroplan \
  -F 'description=Boeing flight'
```

DELETE:
```sh
curl -X DELETE http://127.0.0.1:5000/vehicles/1
```
