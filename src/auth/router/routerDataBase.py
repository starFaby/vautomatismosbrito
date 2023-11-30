from flask import Blueprint
from src.migrate.migrate import initDB

psfvab= Blueprint('psfvab', __name__)

psfvab.route('/psfvab', methods=['GET'])(initDB)

