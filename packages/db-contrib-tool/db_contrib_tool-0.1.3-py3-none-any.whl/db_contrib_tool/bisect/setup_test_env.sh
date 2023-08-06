set -e
db-contrib-tool setup-repro-env -ec "$2" -db -da -i build/resmoke-bisect -l build/resmoke-bisect/"$4" -v "$3" "$4"
"$1" -m venv build/resmoke-bisect/bisect_venv
source build/resmoke-bisect/bisect_venv/bin/activate
"$1" -m pip install --upgrade pip
"$1" -m pip install -r build/resmoke-bisect/"$4"/etc/pip/dev-requirements.txt
deactivate
