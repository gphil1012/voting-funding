cd tests
coverage run --omit=/usr/local/lib/python2.7/* --include=../db/*,./tests/* test_dbInterface.py
coverage html
coverage-badge -fo coverage.svg
convert coverage.svg coverage.png
mv coverage.png ../
