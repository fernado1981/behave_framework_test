from behave import given, when, then
import requests

api_endpoints = {}
request_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url=None

@given('I set sample REST API url')
def step_impl(context):
    global api_url
    api_url = 'http://jsonplaceholder.typicode.com'

@given('I Set POST posts api endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url+'/posts'

@when('I Set HEADER param request content type as "{header_conent_type}"')
def step_impl(context, header_conent_type):
    request_headers['Content-Type'] = header_conent_type

@when('Set request Body "{title_post}" "{body_post}" "{userId_post}"')
def step_impl(context,title_post,body_post,userId_post):
    request_bodies['POST']={"title": title_post,"body": body_post,"userId": userId_post}

@when('Send a POST HTTP request')
def step_impl(context):
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], headers=request_headers)
    response_texts['POST']=response.text
    statuscode = response.status_code
    response_codes['POST'] = statuscode

@then('I receive valid HTTP response code 201')
def step_impl(context):
    assert response_codes['POST'] == 201

@then('Response BODY "{request_name}" is non-empty.')
def step_impl(context,request_name):
    assert response_texts[request_name] is not None