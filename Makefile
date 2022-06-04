build:
	docker build -t nihaldsouza/523-yelp-dataset . 

run:
	docker run -p 8501:8501 nihaldsouza/523-yelp-dataset 

push:
	docker push nihaldsouza/523-yelp-dataset

pull:
	docker pull nihaldsouza/523-yelp-dataset

build_push:
	docker build -t nihaldsouza/523-yelp-dataset .
	docker push nihaldsouza/523-yelp-dataset

sl:
	streamlit run app.py