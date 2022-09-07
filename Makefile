run:
	flask run --reload --debugger
db_mig:
	flask db migrate
db_upg:
	flask db upgrade