import requests

def get_exec(url : str) -> str:
    request : str = requests.get(url).text
    return request.split(f'<input type="hidden" name="execution" value="')[1].split('"')[0]

def get_token(url : str, queryStringParameters : dict, post_data : dict) -> str:
    request : str = requests.post(url=url, params=queryStringParameters, data=post_data).history[-1].headers.get("Set-Cookie") 
    return request.split(";")[0].split("=")[1]

def main_token(username : str, password : str) -> str:
    # 1. Fetch execution token
    get_token_url : str = "https://cas.uphf.fr/cas/login"

    query_string_parameters_token : dict = {
        "service" : "https%3A%2F%2Fvtmob.uphf.fr%2Fesup-vtclient-up4%2Fstylesheets%2Fdesktop%2Fwelcome.xhtml"
    }

    exec_token : str = get_exec(get_token_url+"?service="+query_string_parameters_token.get("service"))
    
    # 2. Fetch user token
    post_data : dict = {
        "username" : username,
        "password" : password, 
        "execution" : exec_token + "=",
        "_eventId" : "submit",
        "geolocation" : ""
    }

    token : str = get_token(get_token_url, query_string_parameters_token, post_data)
    return token
