import requests
import os

def get_file(url : str, headers : dict, cookies : dict, post_data : str) -> str:
    return requests.post(url=url, headers=headers, cookies=cookies, data=post_data).text

def save_file(file_content : str, extension : str) -> str:
    if not os.path.exists("./result"):
        os.mkdir("./result")
        
    with open(f"./result/result{extension}", "w") as file:
        file.write(file_content)
    return f"./result/result{extension}"

def main_calendar(session_id : str) -> None:
    url : str = "https://vtmob.uphf.fr/esup-vtclient-up4/stylesheets/desktop/welcome.xhtml"

    headers : dict = {
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    cookies : dict = {
        "JSESSIONID" : session_id
    }

    data : str = "org.apache.myfaces.trinidad.faces.FORM=j_id12&_noJavaScript=false&javax.faces.ViewState=%211&j_id12%3A_idcl=j_id12%3Aj_id15"

    file_content :str = get_file(url, headers, cookies, data)
    return save_file(file_content, ".ics")

if __name__ == "__main__":
    session_id = "SESSION_ID"
    main_calendar(session_id)