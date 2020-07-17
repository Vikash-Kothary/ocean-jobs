import pandas as pd
from flask import Blueprint, request

data = Blueprint('data', __name__)

@data.route('/search', methods=['POST'])
def search():
	response = dict()
	response['role'] = request.form.get('role')
	response['company'] = request.form.get('company', '')
	response['keywords'] = request.form.get('keywords', '').split(';')
	response['keywords'] = [keyword.strip() for keyword in response['keywords'] if keyword != '']
	response['schedule'] = request.form.get('schedule', False) == True
	return response

@data.route('/totaljobs')
def get_totaljobs_jobs():
	# TODO: Trigger TotalJobs Scraper
    df = pd.read_csv('data/raw/totaljobs.csv')
    return df.to_json(orient='records')
