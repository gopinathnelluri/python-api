# Rackspace-Python-Assessment-REST-API

### Sample Requests:

GET all vehicles:
```sh
curl -X GET http://127.0.0.1:5000/vehicles
```

POST new vehicle:
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
DELETE recently added vehicle:
```sh
curl -X DELETE http://127.0.0.1:5000/vehicles
```

GET vehicle with ID = 1:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/1
```

PUT(update data) vehicle with ID = 1:
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

DELETE vehicle with ID = 1:
```sh
curl -X DELETE http://127.0.0.1:5000/vehicles/1
```
