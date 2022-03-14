# Job Posting Analysis and Summary

### Installation 
1. Clone the repo 
2. Create virtual environment 
3. Switch to created virtual environment 
4. Install requirements 

### While working
1. Never commit to master!!!
2. Always create new branch before starting individual work
3. Always pull then push

Add any huge files to .gitignore
```
cat > .gitignore
```
If any new packages/dependencies are installed 
```
pip freeze > requirements.txt
```

### Code for Installation
```
git clone https://github.com/ani-poroorkara/jpas.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test.py
```

## Development

### Phase 1: 
~~1. Web Scraper~~
2. Data input into MongoDB.
3. Creating master tables from staging data.
4. Schedular script.
5. Database Schemass