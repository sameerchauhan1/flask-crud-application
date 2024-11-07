from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['users_db']
users_collection = db['users']


# Get the list of all the users present in the database
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

# Get a specific user by giving its id
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = users_collection.insert_one(data).inserted_id
    new_user = users_collection.find_one({'_id': user_id})
    new_user['_id'] = str(new_user['_id'])
    return jsonify(new_user), 201

# Update a user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count == 1:
        updated_user = users_collection.find_one({'_id': ObjectId(id)})
        updated_user['_id'] = str(updated_user['_id'])
        return jsonify(updated_user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Delete a user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)