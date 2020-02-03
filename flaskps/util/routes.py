from flaskps import app
from flaskps.controllers import home
from flaskps.controllers import auth
from flaskps.controllers import administrator
from flaskps.controllers import configuration
from flaskps.controllers import role
from flaskps.controllers import user
from flaskps.controllers import item
from flaskps.controllers import mail_sender
from flaskps.controllers import center
from flaskps.controllers import category
from flaskps.controllers import about

# Home
app.add_url_rule('/', 'home_index', home.index)

# Auth
app.add_url_rule('/auth', 'auth_authenticate', auth.authenticate, methods=['POST'])
app.add_url_rule('/logout', 'auth_logout', auth.logout)
app.add_url_rule('/authorize/<endpoint>', 'auth_authorize', auth.authorize)

# Config
app.add_url_rule('/configuration', 'configuration_index', configuration.index)
app.add_url_rule('/configuration/publicInfo', 'configuration_public_info_index', configuration.public_info)
app.add_url_rule('/configuration/pagination', 'configuration_pagination_index', configuration.pagination)
app.add_url_rule('/configuration/maintenanceMode', 'configuration_maintenance_mode_index', configuration.maintenance_mode)
# app.add_url_rule("/configuration/roles", 'configuration_roles',role.roles)
app.add_url_rule('/configuration/createRole', 'configuration_create_role', role.create_role,methods=['POST'])
app.add_url_rule('/configuration/updateRole', 'configuration_update_role', role.update_role,methods=['POST'])
app.add_url_rule('/configuration/deleteRole', 'configuration_delete_role', role.delete_role,methods=['POST'])
app.add_url_rule('/configuration/showRoles', 'configuration_show_roles', role.show_roles)
app.add_url_rule('/configuration/showPermissions', 'configuration_show_permissions', role.show_permissions)
app.add_url_rule('/configuration/showRolesPermissions', 'configuration_show_roles_permissions', role.show_all)
app.add_url_rule('/configuration/createPermission', 'configuration_create_permission', role.create_permission,methods=['POST'])
app.add_url_rule('/configuration/editPermission', 'configuration_update_permission', role.update_permission,methods=['POST'])
app.add_url_rule('/configuration/deletePermission', 'configuration_delete_permission', role.delete_permission,methods=['POST'])
app.add_url_rule('/configuration/assignPermissions', 'configuration_assign_permissions', role.assign_permissions,methods=['POST'])
app.add_url_rule('/configuration/updatePagination', 'configuration_update_pagination', configuration.update_pagination, methods=['POST'])
app.add_url_rule('/configuration/updatePublicInfo', 'configuration_update_public_info', configuration.update_public_info, methods=['POST'])
app.add_url_rule('/configuration/toggleMaintenanceMode', 'configuration_toggle_maintenance_mode', configuration.toggle_maintenance_mode, methods=['POST'])

################################################## USER ROUTES ############################################################

# User list
app.add_url_rule('/user','user_index', user.index)
app.add_url_rule('/user_role_cant','user_role_cant',user.get_cant_roles)
app.add_url_rule('/user_confirm_cant','user_confirm_cant',user.get_cant_confirmed)
app.add_url_rule('/user_bloqued_cant','user_bloqued_cant',user.get_cant_bloqued)

# User Profile
app.add_url_rule('/user/<id>','user_profile', user.get_user_profile, methods=['GET'])   
app.add_url_rule('/user/<id>','user_update_info', user.user_update, methods=['PUT'])    
app.add_url_rule('/user/<id>','user_delete', user.user_delete, methods=['DELETE'])    

app.add_url_rule('/user/<id>/block','user_get_block', user.get_bloqued_value, methods=['GET'])    
app.add_url_rule('/user/<id>/block','user_block', user.set_bloqued_value, methods=['PUT'])     

app.add_url_rule('/user/<id>/roles','user_get_roles', user.get_user_roles, methods=['GET'])        
app.add_url_rule('/user/<id>/roles','user_update_role', user.set_user_roles, methods=['PUT']) 

app.add_url_rule('/user/exist/<id>','user_exist', user.exist, methods=['GET'])   

# User New 
app.add_url_rule('/user/activate','change_password', user.activate_account, methods=['POST'])
app.add_url_rule('/user/new','user_new', user.up, methods=['POST'])


##########################################################################################################################
################################################ CENTER ROUTES ##############################################################

# Center list
app.add_url_rule('/center', 'center_index', center.index)

# Center Profile
app.add_url_rule('/center/<id>','center_profile', center.get_center_profile, methods=['GET'])
app.add_url_rule('/center/<id>','center_update_info', center.center_update, methods=['PUT']) 
app.add_url_rule('/center/<id>','center_delete', center.center_delete, methods=['DELETE'])

app.add_url_rule('/center/exist/<id>','center_exist', center.exist, methods=['GET'])     

# Center New 
app.add_url_rule('/center/new','center_new', center.up, methods=['POST'])

##########################################################################################################################
################################################ Category ROUTES ##############################################################

# Category list
app.add_url_rule('/category', 'category_index', category.index)

# Category Profile
app.add_url_rule('/category/<id>','category_profile', category.get_category, methods=['GET'])
app.add_url_rule('/category/<id>','category_update_info', category.category_update, methods=['PUT']) 
app.add_url_rule('/category/<id>','category_delete', category.category_delete, methods=['DELETE'])

app.add_url_rule('/category/exist/<id>','category_exist', category.exist, methods=['GET'])     

# Category New 
app.add_url_rule('/category/new','category_new', category.up, methods=['POST'])

##########################################################################################################################
################################################ Item ROUTES ##############################################################

# Item list
app.add_url_rule('/item', 'item_index', item.index)

# Item Profile
app.add_url_rule('/item/<id>','item_profile', item.get_item, methods=['GET'])
app.add_url_rule('/item/<id>','item_update_info', item.item_update, methods=['PUT']) 
app.add_url_rule('/item/<id>','item_delete', item.item_delete, methods=['DELETE'])

app.add_url_rule('/item/exist/<id>','item_exist', item.exist, methods=['GET'])     

# Item New 
app.add_url_rule('/item/new','item_new', item.up, methods=['POST'])

##########################################################################################################################
################################################ VARIOUS ROUTES ##############################################################

# Send message
app.add_url_rule('/check','check_link', mail_sender.check_link, methods=['POST'])


##########################################################################################################################
################################################ ADMIN ROUTES ##############################################################

# Administrator list
app.add_url_rule('/administrator', 'administrator_index', administrator.index)


# About
app.add_url_rule('/getPublicInfo', 'about_getInfo', about.getInfo, methods=['GET'])

