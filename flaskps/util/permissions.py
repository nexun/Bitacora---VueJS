
misc = ['serve_js']

def checkPermissions(per,rule):
    print('Permission required:', rule)
    if rule in misc: return True
    if rule in per: return True
    print('Permission: NO')
    return False

'''
Por las dudas que quede en el abismo esto 


auth_authenticate = ['auth_authenticate']
auth_login = ['auth_login']
auth_logout = ['auth_logout']
configuration_index = ['configuration_index']  
configuration_roles = ['configuration_roles','configuration_create_role','configuration_update_role','configuration_delete_role','configuration_show_roles']
configuration_toggle_maintenance_mode = ['configuration_toggle_maintenance_mode']
configuration_update_pagination = ['configuration_update_pagination']
configuration_update_public_info = ['configuration_update_public_info']
home_about = ['home_about']
home_index = ['home_index']
user_index = ['user_index','search_index','search_users_all','search_users','search_administrators'
,'search_preceptors','search_teachers','teacher_show','teacher_index','administrator_index','preceptor_index']
misc = ['serve_js']

all_permissions = [auth_authenticate,auth_login,auth_logout,configuration_index,configuration_roles,configuration_toggle_maintenance_mode
,configuration_update_pagination,configuration_update_public_info,home_about,home_index,user_index, misc]
'search_preceptors','search_teachers','teachers_query']
misc = ['serve_js','confirm_email']
user_new = ['user_new']
send_email = ['send_email']
confirm_email = ['confirm_email']
activate = ['activate']

all_permissions = [auth_authenticate,auth_login,auth_logout,configuration_index,configuration_roles,configuration_toggle_maintenance_mode
,configuration_update_pagination,configuration_update_public_info,home_about,home_index,user_index, misc, user_new, send_email, confirm_email, activate]

def checkPermissions(per,rule):
    print(rule)
    if rule == 'static': return True
    if rule in misc: return True
    
    for p in all_permissions:
        if rule in p:
            if p[0] in per:
                print('Permission: OK')
                return True
    print('Permission: NO')
    return False
'''