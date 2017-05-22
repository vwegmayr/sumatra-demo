env:
	conda env create -f environment.yml -n sumatra-demo

smt:
	@read -r -p "Enter sumatra project: " PROJ; \
	read -r -p "Enter sumatra username: " USER; \
	read -r -p "Enter sumatra password: " PASS; \
	read -r -p "Enter archive path: " ARCH; \
	read -r -p "Enter path where Sumatra should look for output: " D_PATH; \
	echo "\nAdditionally, using the following sumatra settings:"; \
	echo "--executable python"; \
	echo "--main $(PROJECT)/examples/sumatra.py"; \
	echo "--on-changed diff"; \
	echo "--store http://$$USER:***@192.33.91.83:8080/records"; \
	smt init \
	--datapath $$D_PATH \
	--archive $$ARCH \
	--executable python \
	--main main.py \
	--on-changed store-diff \
	--store http://$$USER:$$PASS@192.33.91.83:8080/records \
	$$PROJ
