# Works Single View

1. Clone this repo with `git clone https://github.com/mkiterian/musical_works`
2. Go to the project root directory `cd musical_works`

### How to run
Run `docker-compose up --build`

### Ingest data command
In a seperate terminal window,
- run migrations `docker-compose run web python3 manage.py migrate` 
- To ingest data run `docker-compose run web python3 manage.py ingest_data_from_file works_metadata.csv`

### Sanity checks
- Make a GET request to `http://localhost:8000/works/` via a browser/Postman/curl
- Make a GET request to `http://localhost:8000/works/?iswc=T0046951705`
- Make a GET request to `http://localhost:8000/contributors/`


### To run tests
- Run `docker-compose run web python3 manage.py test`
