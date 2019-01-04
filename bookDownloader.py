import requests, json
import yaml
import os
import zipfile

ROBOT_ENV = "https://luka-api.ling.cn"  # 环境改这里
ROBOT_LOGIN_BODY = {
    'data': {
        'type': 'robot-login',
        'attributes': {
            'udid': 'FRFF2WR9'  # 设备码改这里
        }
    }
}
GENERATED_PATH = "./sdcard/model/book"  # 脚本下载文件的位置

# bookIdList = (
# 20833,
# 20835,
# 20832,
# 60002,
# 60003,
# 60004,
# 60005,
# 60007,
# 60008,
# 60009,
# 60010,
# 60013,
# 60016,
# 60017,
# 60019,
# 60020,
# 62000,
# 62001,
# 62002,
# 62003,
# 62004,
# 62015,
# 62016,
# 62020,
# 62021,
# 62025,
# 62027,
# 62029,
# 62030,
# 62041,
# 62042,
# 62053,
# 62054,
# 62064,
# 60217,
# 60218,
# 60220,
# 60221,
# 60223,
# 60224,
# 60226,
# 60227,
# 60229,
# 60230,
# 60232,
# 60233,
# 60235,
# 60236,
# 60238,
# 60239,
# 60241,
# 60242,
# 60244,
# 60245,
# 60247,
# 60248,
# 60250,
# 60251,
# 60253,
# 60254,
# 60256,
# 60257,
# 60259,
# 60260,
# 60262,
# 60263,
# 60265,
# 60266,
# 60268,
# 60269,
# 60271,
# 60272,
# 60274,
# 60276,
# 60277,
# 60278,
# 60280,
# 60281,
# 60283,
# 60284,
# 60286,
# 60288,
# 60289,
# 60290,
# 60292,
# 60293,
# 60295,
# 60296,
# 60298,
# 60299,
# 60302,
# 60303,
# 60304,
# 60305,
# 60307,
# 60308,
# 60310,
# 60311,
# 60313,
# 60314,
# 70000)
bookIdList = (
60284,
60286,
60288,
60289,
60290,
60292,
60293,
60295,
60296,
60298,
60299,
60302,
60303,
60304,
60305,
60307,
60308,
60310,
60311,
60313,
60314,
70000)
# bookIdList = list(range(100))
ROBOT_LOGIN_URL = ROBOT_ENV + "/robot-login"
ROBOT_BOOK_URL = ROBOT_ENV + "/cv/model/book/"

headersLogin = {'Content-Type': 'application/json',
                'Accept': 'application/vnd.luka.v1.14+json',
                'Accept-Language': 'zh'}


def get_book_info(book_id):
    return requests.get(ROBOT_BOOK_URL + str(book_id), headers=headersBookInfo)


def download_file(url, position):
    local_filename = url.split('/')[-1].split('?')[0]
    local_file_path = os.path.join(position, local_filename)
    print("local filename is " + local_filename)
    response = requests.get(url, stream=True)
    handle = open(local_file_path, "wb")
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    return local_file_path


def get_camel_case(underline_str):
    first, *rest = underline_str.split('_')
    return first + ''.join(word.capitalize() for word in rest)


data = json.dumps(ROBOT_LOGIN_BODY)
r = requests.put(ROBOT_LOGIN_URL, data=data, headers=headersLogin)

print("current env is " + ROBOT_ENV)
print("login request data is " + data)
print("login response is " + str(r))

login_result = r.json()

if login_result['errno'] != 0:
    raise Exception('login error!')

token = login_result['data']['token']

headersBookInfo = {'Authorization': 'Bearer ' + token,
                   'Accept': 'application/vnd.luka.v1.12+json'}

if not os.path.exists(GENERATED_PATH):
    os.makedirs(GENERATED_PATH)

for bookId in bookIdList:

    book_result = get_book_info(bookId).json()
    print(book_result)

    if book_result['errno'] != 0:
        print('get book info failed book id is' + str(bookId))
        continue

    voice_json = book_result['data']['voice']
    model_url = book_result['data']['url']
    version = book_result['data']['version']

    if voice_json is None:
        print('The voice of ' + str(bookId) + ' is None')
        continue

    if model_url is None:
        print('The model of ' + str(bookId) + ' is None')
        continue

    voice_url = voice_json['voice_url']

    md5 = voice_json['voice_tag']

    excludeKey = ('download_url', 'voice_url', 'user_id')

    voice_json_wanted = {get_camel_case(element): voice_json[element]
                         for element in voice_json
                         if voice_json[element] != ''
                         and (element not in excludeKey)}

    # print(voice_json_wanted)

    bookFolder = os.path.join(GENERATED_PATH, str(bookId))
    audioFolder = os.path.join(bookFolder, "audio")
    md5Folder = os.path.join(audioFolder, md5)
    modelFolder = os.path.join(bookFolder, "model")
    if not os.path.exists(bookFolder):
        os.mkdir(bookFolder)
        if not os.path.exists(audioFolder):
            os.mkdir(audioFolder)
            if not os.path.exists(md5Folder):
                os.mkdir(md5Folder)

    if not os.path.exists(modelFolder):
        os.mkdir(modelFolder)
    
    file_path = download_file(voice_url, md5Folder)
   
    model_path = download_file(model_url, bookFolder)
    
    with zipfile.ZipFile(file_path) as zp:
        
            zp.extractall(md5Folder)
        
    os.remove(file_path)

    with zipfile.ZipFile(model_path) as mzp:
        mzp.extractall(bookFolder)
    os.remove(model_path)

    with open(os.path.join(GENERATED_PATH, str(bookId), "book_info.yml"), "w", encoding="utf-8") as f:
        voice_yaml = yaml.dump(voice_json_wanted, f, default_flow_style=False, encoding='UTF-8')

    fp = open(os.path.join(bookFolder, "version"), "w+")
    fp.write(str(version))
    fp.close()

    # print(yaml.dump(voice_json_wanted, default_flow_style=False))
