from flask import Flask, session, jsonify, request, render_template
import pymysql
import json
APP = Flask('backend')
@APP.route('/')
def showPage():
	return render_template('Project.html')
@APP.route('/todo/create', methods = ['POST'])
def addTask():
	database = pymysql.connect(db = "toDos")
	cursor = database.cursor()
	action = "INSERT INTO toDos (items) VALUES (%s)"
	newItem = request.get_json().get('newTask')
	cursor.execute(action, newItem)
	database.commit()
	cursor.close()
	database.close()
	return "Done"
@APP.route('/todo/read', methods = ['GET'])
def getTasks():
	database = pymysql.connect(db = "toDos")
	cursor = database.cursor()
	cursor.execute("SELECT items FROM toDos")
	lst = cursor.fetchall()
	cursor.close()
	database.close()
	return jsonify(lst)
@APP.route('/todo/update', methods = ['PUT'])
def changeTask():
	original = request.get_json().get('originalTask')
	newTask = request.get_json().get('replacementTask')
	database = pymysql.connect(db = "toDos")
	cursor = database.cursor()
	action = "UPDATE toDos SET items = %s WHERE items = %s"
	cursor.execute(action, (newTask, original))
	database.commit()
	cursor.close()
	database.close()
	return "Done"
@APP.route('/todo/delete', methods = ['DELETE'])
def deleteTask():
	database = pymysql.connect(db = "toDos")
	cursor = database.cursor()
	action = "DELETE FROM toDos WHERE items = %s"
	item = request.get_json().get('deleteItem')
	cursor.execute(action, item)
	database.commit()
	cursor.close()
	database.close()
	return "Done"
@APP.after_request
def affter_request(response):
	header = response.headers
	header['Access-Control-Allow-Origin'] = '*'
	header['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
	header['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE'
	return response
APP.run(debug = True)
