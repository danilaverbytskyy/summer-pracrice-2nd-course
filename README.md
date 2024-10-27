# Example Python Flask Crud

 Simple example python flask crud app for sqlite.
 
## Screenshots

 
 
### Installing (for linux)

open the terminal and follow the white rabbit.


```
git clone https://github.com/gurkanakdeniz/example-flask-crud.git
```
```
cd example-flask-crud/
```
```
python -m venv venv
```
```
venv/Source/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
set FLASK_APP=crudapp.py
```
```
flask db init
```
```
flask db migrate -m "entries table"
```
```
flask db upgrade
```
```
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
