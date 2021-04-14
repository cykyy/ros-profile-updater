from helper import profile_serializer, get_desired_ppp, sum_of_profile_ppp
from ros_sync import ros_api
from datetime import datetime

ros_obj = ros_api()


def profile_update_recursive(ppps, profile_to_match, profile_to_update_to):
    file1 = open("logs.txt", "a")
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file1.write('Time: ' + dt_string + "\n")
    for xy in ppps:
        _ppp = xy.get('c_ident')
        if xy.get('profile') == profile_to_match:
            print(_ppp, ':', xy.get('profile'), ' -> ', profile_to_update_to)
            ros_obj.update_secret_profile(_ppp, profile_to_update_to)

            file1.write(_ppp + ':' + xy.get('profile') + ' -> ' + profile_to_update_to + '\n')
    file1.close()  # to change file access modes


print("Do you want to change *ppp profile? Yes/No")
kb_put1 = str(input())
if kb_put1 == 'Yes' or kb_put1 == "yes":
    print("Please specify the value (e.g: BBN for all BBN1-* ppps):")
    kb_put2 = str(input())
    if kb_put2:
        ppp_exact = get_desired_ppp(ros_obj.get_ppp_secret(), kb_put2)
        # print("ppp_exact", ppp_exact)
        print('Please select the profile number to change from:')
        current_profiles = sum_of_profile_ppp(ppp_exact)
        # print('current_profiles: ', current_profiles)
        for k, v in current_profiles.items():
            print(k, v)
        kb_put23 = int(input())
        pro_chng_from = current_profiles.get(kb_put23)
        print('Selected: ', pro_chng_from)
        print()

        print('Please select the profile number to update with:')
        profiles = profile_serializer(ros_obj.get_profile())
        for x, y in profiles.items():
            print(x, y)
        kb_put4 = int(input())
        if profiles.get(kb_put4):
            chosen_profile = profiles.get(kb_put4)
            print('Selected: ', profiles.get(kb_put4))
            print("Alright, applying...")
            profile_update_recursive(ppp_exact, pro_chng_from, chosen_profile)
            print()
            print('Operation Successful! Thanks.')
