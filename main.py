from flask import Flask, abort
from flask_restful import Api, Resource
from flask import jsonify
import requests
import json
import datadog_api_client
import datadog_api_client.v1
import time, random
import csv
from urllib.request import urlopen

# import json
import json


from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.api.authentication_api import AuthenticationApi
from datadog_api_client.v1.model.webhooks_integration import WebhooksIntegration


app = Flask(__name__)
app.debug = True

api = Api(app)


configuration = datadog_api_client.v1.Configuration(
    host = "https://app.datadoghq.com/"
)

# api_url = 'https://api.datadoghq.com/api/v1/test?api_key=8d26c547b6a075490cc26faaacf12a9b'

response1 = requests.get("https://api.datadoghq.com/api/v1/test?api_key=8d26c547b6a075490cc26faaacf12a9b")

test_url = 'https://api.github.com'
gg = urlopen(test_url)

response = requests.get("http://httpbin.org/stream/1")

data1 = response.json()


@app.route('/')
def bla():
    return 'hello'
    # data = response.json()
    # print(data)
    # print("fhakfh")
    # pass
# api.add_resource(Locations, '/locations')

@app.route('/webhooks', methods=['GET'])
def webhook():
    data = response.json()
    return data



@app.route('/hha', methods=['GET'])
def webhook1():
    # configuration = Configuration()
    # with ApiClient(configuration) as api_client:
    #     api_instance = AuthenticationApi(api_client)
    #     response2 = api_instance.validate()
    print(response2)
    data1 = response1.json()
    return data1
    # print(data)
    # print the json response
    # print(response)
    # if request.method == 'GET':
    #     print(test_url.json)
    #     return 'success', 200
    # else:
    #     abort(400)
    # pass

@app.route('/test', methods=['GET'])
def test():
    data = test_url.json()
    print(data)
    pass



# app.config["DEBUG"] = True

if __name__ == '__main__':
    app.run()

# webhook_url = "https://api.datadoghq.com/api/v1/check_run?api_key=8d26c547b6a075490cc26faaacf12a9b"
# webhook_api = "https://api.datadoghq.com/api/v1/integration/webhooks/configuration/webhooks"
#
#
#
# body = WebhooksIntegration(
#     name="Example-Create_a_webhooks_integration_returns_OK_response", url="https://example.com/webhook"
# )
#
# configuration = Configuration()
# with ApiClient(configuration) as api_client:
#     api_instance = WebhooksIntegrationApi(api_client)
#     response = api_instance.create_webhooks_integration(body=body)
#
#     print(response)
#
# app = Flask(__name__)
# app.config["DEBUG"] = True
