env:
	conda env create -f environment.yml -n sumatra-demo
	
smt:
	smt init \
	--datapath output \
	--archive output \
	--executable python \
	--main main.py \
	--on-changed store-diff \
	--store http://demo:demo@192.33.91.83:8080/records \
	demo
