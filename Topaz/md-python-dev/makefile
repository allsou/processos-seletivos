build:
	docker build . -t topaz:teste

up:
	$$(docker rm topaz) || echo 'Nenhum container topaz criado'
	docker run --name topaz topaz:teste

get-output-and-remove:
	docker cp topaz:/app/data_source/output.txt ./output.txt

run: up get-output-and-remove

unit-test:
	$$(docker rm topaz) || echo 'Nenhum container topaz criado'
	docker run -it --entrypoint python --name topaz topaz:teste -m unittest discover -p *test.py