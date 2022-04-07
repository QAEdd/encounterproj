
#!/bin/bash
declare -a directories=("tests" "tests" "weather" "location")
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
source venv/bin/activate
pip3 install -r test_requirements.txt
python3 -m venv venv
for dir in "${directories[@]}"
do
  cd ${dir}
  python3 -m pytest --cov=application --cov-report=html
  pwd
  cd ..
done