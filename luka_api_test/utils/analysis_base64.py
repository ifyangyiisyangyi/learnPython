import base64
import yaml

nlu = {}


def analysis_base64(words):
    script = base64.b64decode(words['data']['script'])
    result = yaml.load(script, Loader=yaml.FullLoader)['main']
    # print(result)
    for i in result:
        # print(result)
        if i.split(' ')[0] == 'play_tts':
            nlu['play_tts'] = str(base64.b64decode(i.split(' ')[-1]), 'utf-8')
        elif i.split(' ')[0] == 'play_song':
            nlu['play_song'] = str(base64.b64decode(i.split(' ')[-1]), 'utf-8')
        # elif i.split(' ')[0] == 'play_audio':
        #     nlu['play_audio'] = str(base64.b64decode(i.split(' ')[-1]), 'utf-8')
    return nlu


if __name__ == '__main__':
    words = {'errno': 0, 'errmsg': 'success', 'debug': 'success', 'data': {'event_id': 0, 'listen': False,
                                                                           'script': 'bWFpbjoKICAtIHBsYXlfdHRzIDVMaUE1WXFnNUxpQTU2Mko1THFPTWc9PQogIC0gc3RhcnQgc3ViCiAgLSBwbGF5X2F1ZGlvIC0tdHlwZT1hc3NldHMgc3BlZWNoX3NvdW5kLm1wMwpzdWI6CiAgLSBwbGF5X2FjdGlvbiBsaXN0ZW4='}}

    analysis_base64(words)
