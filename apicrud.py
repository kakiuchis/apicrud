from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name' : 'java'}, {'name' : 'php'}, {'name' : 'ruby'}]

@app.route("/", methods = ['GET'])
def test():
    return jsonify({'message' : 'it is works.'})

@app.route("/lang", methods = ['GET'])
def returnAll():
    return jsonify({'langages' : languages})

@app.route("/lang/<string:name>", methods = ['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'langages' : langs[0]})

@app.route("/lang", methods = ['POST'])
def addOne():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'langages' : languages})

@app.route("/lang/<string:name>", methods = ['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'langages' : langs[0]})

@app.route("/lang/<string:name>", methods = ['DELETE'])
def removeOne(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'langages' : languages})

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')