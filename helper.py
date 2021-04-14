def get_desired_ppp(ppp_all, value=''):
    ppp_lst = []
    if ppp_all:
        for x in ppp_all:
            if value:
                if x.get('c_ident').startswith(value):
                    ppp_lst.append(x)
    return ppp_lst


def only_required_cols(ppp_all):
    ppp_lst = []
    ppp_dict = {}
    if ppp_all:
        for x in ppp_all:
            ppp_dict.update({
                'c_ident': x.get('c_ident'),
                'package': x.get('profile'),
                'has_suspended': x.get('has_suspended'),
                'comment': x.get('comment'),
                'last_logged_out': x.get('last_logged_out')
            })
            ppp_lst.append(ppp_dict)
            ppp_dict = {}
    return ppp_lst


def profile_serializer(profiles):
    # print(profiles)
    pro_dict = {}
    count = 0
    for x in profiles:
        pro_dict.update({count: x})
        count += 1
    return pro_dict


def sum_of_profile_ppp(ppps):
    pro_dict = {}
    count = 0
    for x in ppps:
        if bool(pro_dict):
            if x.get('profile') in pro_dict.values():
                continue
        pro_dict.update({count: x.get('profile')})
        count += 1
    return pro_dict


def read_dict_from_file(file):
    import json
    with open(file) as f:
        data = f.read()
    js = json.loads(data)
    return js
