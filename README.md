# Rackspace-Python-Assessment-REST-API

### Sample GET Requests:

GET all vehicles:
```sh
curl -X GET http://127.0.0.1:5000/vehicles
```

GET vehicle with ID = 1:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/1
```


## Search

GET all vehicles by type Car:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/search/type/Car
```

GET all vehicles of brand BMW:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/search/brand/BMW
```

GET all vehicles with year of make 2002:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/search/year/2002
```

GET all vehicles with word 'flight' in description:
```sh
curl -X GET http://127.0.0.1:5000/vehicles/search/description/flight
```

GET all vehicles with model '7777':
```sh
curl -X GET http://127.0.0.1:5000/vehicles/search/description/7777
```


### Sample POST Requests:

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

### Sample PUT Requests:

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

### Sample DELETE Requests:

DELETE vehicle with ID = 1:
```sh
curl -X DELETE http://127.0.0.1:5000/vehicles/1
```



