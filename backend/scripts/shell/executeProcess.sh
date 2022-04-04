export PYTHONPATH=${PYTHONPATH}:/Users/vijetavamannayak/LinkedInProject/scripts/utility/
export PYTHONPATH=${PYTHONPATH}:/Users/vijetavamannayak/LinkedInProject/scripts/master/
export PYTHONPATH=${PYTHONPATH}:/Users/vijetavamannayak/LinkedInProject/scripts/summary/
mv /Users/vijetavamannayak/LinkedInProject/rawData/*.csv* /Users/vijetavamannayak/LinkedInProject/archive
python3 /Users/vijetavamannayak/LinkedInProject/scripts/utility/web_script.py
python3 /Users/vijetavamannayak/LinkedInProject/scripts/driver/driver.py config_file=/Users/vijetavamannayak/LinkedInProject/scripts/driver/driver.json