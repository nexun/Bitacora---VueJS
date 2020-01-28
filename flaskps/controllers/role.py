import json
from flask import request, Response, jsonify
from flaskps.models import role
from flaskps.models import permission
from flaskps.classes.forms.role import RoleForm
from flaskps.classes.forms.role import PermissionForm


def show_roles():
    response = [{
        'id': role.id,
        'name': role.name
    } for role in role.get_roles()]
    return jsonify(response)


def show_permissions():
    response = [{
        'id': permission.id,
        'name': permission.public_name,
        'code': permission.name
    } for permission in permission.get_permissions()]
    return jsonify(response)


def show_all():
    return jsonify(role.get_all())

def show_ids():    
    return role.get_ids()

def assign_permissions():
    check1 = True
    check2 = True
    adds = json.loads(request.form['adds'])
    removes = json.loads(request.form['removes'])
    role_selected = request.form['role']
    all_permissions=[permission[0] for permission in permission.get_ids()]
    if role.check_exist_id(role_selected):
        # Check that permissions are exist
        for add in adds:
            if add not in all_permissions:
                check1 = False
                break
        for remove in removes:
            if remove not in all_permissions:
                check2 = False
                break
        # If exists, add and remove permissions
        if check1 & check2:
            for add in adds:
                role.add_permission(role_selected, add)
            for remove in removes:
                role.remove_permission(role_selected, remove)
            return Response(status=200)
        else:
            response = jsonify(
                "Algunos de los permisos asignados no existen. Quizas estos fueron actualizados y necesites recargar la pagina")
            response.status_code = 400
            return response
    else:
        response = jsonify("El rol seleccionado no existe")
        response.status_code = 400
        return response


def create_permission():
    form = PermissionForm(request.form)
    if form.validate():
        if permission.check_exist(request.form['code_permission']):
            response = jsonify("El codigo de permiso ingresado ya existe")
            response.status_code = 400
            return response
        else:
            if permission.check_exist_public(request.form['name_permission']):
                response = jsonify("El nombre de permiso ingresado ya existe")
                response.status_code = 400
                return response
            else:
                lastId=permission.create(request.form['code_permission'], request.form['name_permission'])
                response=jsonify(lastId)
                response.status_code=200
                return response
    else:
        response = jsonify(form.errors[0])
        response.status_code = 400
        return response


def update_permission():
    form = PermissionForm(request.form)
    if form.validate():
        if permission.check_exist(request.form['selected_code']):
            if permission.check_exist(request.form['code_permission']) and request.form['selected_code'] != request.form['code_permission']:
                response = jsonify("El codigo de permiso ingresado ya existe")
                response.status_code = 400
                return response
            else:
                if permission.check_exist_public(request.form['name_permission']) and request.form['selected'] != request.form['name_permission']:
                    response = jsonify("El nombre de permiso ingresado ya existe")
                    response.status_code = 400
                    return response
                else:
                    permission.update(request.form["selected_code"], request.form['code_permission'], request.form['name_permission'])
                    return Response(status=200)
        else:
            response = jsonify("El permiso seleccionado no existe")
            response.status_code = 400
            return response
    else:
        response = jsonify(form.errors[0])
        response.status_code = 400
        return response


def delete_permission():
    if permission.check_exist(request.form['selected']):
        permission.delete(request.form["selected"])
        return Response(status=200)
    else:
        response = jsonify("El permiso seleccionado no existe")
        response.status_code = 400
        return response


def create_role():
    form = RoleForm(request.form)
    if form.validate():
        if role.check_exist(request.form['name_role']):
            response = jsonify("El nombre de rol ingresado ya existe")
            response.status_code = 400
            return response
        else:
            lastId=role.create(request.form['name_role'])
            response=jsonify(lastId)
            response.status_code=200
            return response
    else:
        response = jsonify(form.errors['name_role'][0])
        response.status_code = 400
        return response


def update_role():
    form = RoleForm(request.form)
    if form.validate():
        if role.check_exist(request.form['selected']):
            if role.check_exist(request.form['name_role']):
                response = jsonify("El nombre de rol ingresado ya existe")
                response.status_code = 400
                return response
            else:
                role.update(request.form["selected"],
                            request.form['name_role'])
                return Response(status=200)
        else:
            response = jsonify("El rol seleccionado no existe")
            response.status_code = 400
            return response
    else:
        response = jsonify(form.errors['name_role'][0])
        response.status_code = 400
        return response


def delete_role():
    if role.check_exist(request.form['selected']):
        if role.check_exist_user(request.form['selected']):
            if role.nobody_need_it(request.form['selected']):
                role.delete(request.form["selected"])
                return Response(status=200)
            else:
                response = jsonify(
                    "Existen usuarios que poseen solo el rol seleccionado. No puede eliminarse")
                response.status_code = 400
                return response
        else:
            role.delete(request.form["selected"])
            return Response(status=200)
    else:
        response = jsonify("El rol seleccionado no existe")
        response.status_code = 400
        return response
