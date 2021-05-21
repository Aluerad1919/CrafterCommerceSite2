from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# from .forms import *
# from taggit.models import Tag


# ---------------Render pages---------------
def index(request):
    context ={
        'text_db': Textile_Craft.objects.all(),
        'wood_db': Wood_Craft.objects.all(),
        'metal_db' : Metal_Craft.objects.all(),
        'leather_db' : Leather_Craft.objects.all(),
        'jewel_db' : Jewelry_Craft.objects.all(),
        'digital_db' : Digital_Craft.objects.all(),
        }
    if('userid' not in request.session):
        print("not logged")
        return render(request, 'index.html', context)
    else:
        print("logged in")
        context={
            'logged_user': Users.objects.get(id=request.session['userid']),
            'text_db': Textile_Craft.objects.all(),
            'wood_db': Wood_Craft.objects.all(),
            'metal_db' : Metal_Craft.objects.all(),
            'leather_db' : Leather_Craft.objects.all(),
            'jewel_db' : Jewelry_Craft.objects.all(),
            'digital_db' : Digital_Craft.objects.all(),
        }
        return render(request, 'index.html', context)

def registerform(request):
    return render(request,'register.html')

def user_account(request, val):
    context={
        'logged_user':Users.objects.get(id=val),
        'address_db':Address.objects.all()
    }
    return render(request, 'user_account.html', context)

def address_form(request, val):
    context={
        'logged_user':Users.objects.get(id=val)
    }
    return render(request, 'address_form.html', context)

def store_front(request, val):
    clerk = Users.objects.get(id=val)
    context = {
        'shop_stall': Users.objects.get(id=val),
        'logged_user': request.session['userid'],
        'cloth_db': Textile_Craft.objects.filter(seller=Users.objects.get(id=val)),
        'leather_db': Leather_Craft.objects.filter(seller=Users.objects.get(id=val)),
        'metal_db': Metal_Craft.objects.filter(seller=Users.objects.get(id=val)),
        'wood_db': Wood_Craft.objects.filter(seller=Users.objects.get(id=val)),
        'jewel_db': Jewelry_Craft.objects.filter(seller=Users.objects.get(id=val)),
        'digi_db': Digital_Craft.objects.filter(seller=Users.objects.get(id=val)),
    }
    if(clerk.has_store == False):
        return render(request, 'open_store.html', context)
    else:
        return render(request, 'store_front.html', context)

def add_product(request, val):
    context={
        'crafter':Users.objects.get(id=val),
        # 'tags': Craft.tags.most_common()[:4]
    }
    return render(request, 'add_product.html', context)

def show_product(request, mats, val):
    # print(mats)
    if mats == "Textile_Craft":
        context ={
            'details': Textile_Craft.objects.get(id=val),
            'logged_user': Users.objects.get(id=request.session['userid']),
        }
    return render(request, 'show_product.html', context)
# -----------User account logic----------- 
def add_address(request):
    # errors
    Address.objects.create(
        first_name = request.POST['f_name_input'],
        last_name = request.POST['l_name_input'],
        street_Add = request.POST['street_input'],
        city = request.POST['city_input'],
        state = request.POST['state_input'],
        zip_code = request.POST['zip_input'],
        user_address = Users.objects.get(id=request.session['userid'])
    )
    return redirect(user_account, request.session['userid'])
    
def register(request):
    errors=Users.objects.count_Vald(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('CrafterMall/Signup')
    password = request.POST['pw_input']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = Users.objects.create(
        user_name = request.POST['username_input'],
        email = request.POST['email_input'],
        password = pw_hash
    )
    request.session['userid'] = new_user.id
    return redirect('/')
    
def login(request):
    user = Users.objects.filter(user_name=request.POST['username_input']) 
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['pw_input'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/')
        return redirect("CrafterMall/Signup")
    else:
        return redirect('/')
    
def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request, val):
    this_guy = Users.objects.get(id=val)
    this_guy.delete()
    return redirect('/')
    
def success(request):
    context ={
        'logged_in': Users.objects.get(id=request.session['userid']),
        'users_db': Users.objects.all()
    }
    return render(request, 'index.html',context)

def new_address(request):
    Address.objects.create(
        first_name = request.POST['first_name_input'],
        last_name = request.POST['last_name_input'],
        street_address = request.POST['street_input'],
        user_city = request.POST['city_input'],
        user_state = request.POST['state_input'],
        user_zip = request.POST['zip_input']
    )
    return redirect('/user_account.html')

def edit_form(request, val):
    context = {
        'the_address': Address.objects.get(id=val)
    }
    return render(request, 'edit_form.html', context)

def edit_address(request, val):
    add_change = Address.objects.get(id=val)
    if 'f_name_input' != '':
        add_change.first_name = request.POST['f_name_input']
        add_change.save()
    if 'l_name_inut' != '':
        add_change.first_name = request.POST['l_name_input']
        add_change.save()
    if 'street_input' != '':
        add_change.first_name = request.POST['street_input']
        add_change.save()
    if 'city_input' != '':
        add_change.first_name = request.POST['city_input']
        add_change.save()
    if 'state_input' != '':
        add_change.first_name = request.POST['state_input']
        add_change.save()
    if 'zip_input' != '':
        add_change.first_name = request.POST['zip_input']
        add_change.save()
    return redirect(user_account, request.session['userid'])

def delete_address(request, val):
    del_address = Address.objects.get(id=val)
    del_address.delete()
    return redirect(user_account, request.session['userid'])

    # -----------Store Front Logic-----------
def opening_store(request, val):
    clerk = Users.objects.get(id=val)
    if('opening_input' != ''):
        clerk.has_store = True
        clerk.store_name = request.POST['st_name_input']
        clerk.save()
    return redirect(store_front, request.session['userid'])

def post_new_product (request):
    # First Priority when reformatting for effeciticy. Right now just getting it to work.
    # errors

    if(request.POST['prod_cat'] == 'Textile_Craft'):
        newcraft = Textile_Craft.objects.create(
        craft_name = request.POST['prod_name'],
        description = request.POST['prod_desc'],
        craft_image = request.FILES['craft_img'],
        price = request.POST['prod_price'],
        seller = Users.objects.get(id= request.session['userid'])
        )
        if (request.POST['stock_amount'] != '' ):
            inv = Textile_Craft.objects.get(id = newcraft.id)
            inv.in_stock_num = request.POST['stock_amount']
            inv.save()
        elif (request.POST['made2order'] == True):
            inv = Textile_Craft.objects.get(id = newcraft.id)
            inv.on_order = True
            inv.save()
        return redirect(store_front, request.session['userid'])
        # Add a Leather Product -------------------------------
    if(request.POST['prod_cat'] == 'Leather_Craft'):
        newcraft = Leather_Craft.objects.create(
        craft_name = request.POST['prod_name'],
        description = request.POST['prod_desc'],
        craft_image = request.FILES['craft_img'],
        price = request.POST['prod_price'],
        seller = Users.objects.get(id= request.session['userid'])
        )
        if (request.POST['stock_amount'] != '' ):
            inv = Leather_Craft.objects.get(id = newcraft.id)
            inv.in_stock_num = request.POST['stock_amount']
            inv.save()
        elif (request.POST['made2order'] == True):
            inv = Leather_Craft.objects.get(id = newcraft.id)
            inv.on_order = True
            inv.save()
        return redirect(store_front, request.session['userid'])
# Add a metal product ----------------------------
    if(request.POST['prod_cat'] == 'Metal_Craft'):
        newcraft = Metal_Craft.objects.create(
        craft_name = request.POST['prod_name'],
        description = request.POST['prod_desc'],
        craft_image = request.FILES['craft_img'],
        price = request.POST['prod_price'],
        seller = Users.objects.get(id= request.session['userid'])
        )
        if (request.POST['stock_amount'] != '' ):
            inv = Metal_Craft.objects.get(id = newcraft.id)
            inv.in_stock_num = request.POST['stock_amount']
            inv.save()
        elif (request.POST['made2order'] == True):
            inv = Metal_Craft.objects.get(id = newcraft.id)
            inv.on_order = True
            inv.save()
        return redirect(store_front, request.session['userid'])
# Add Carpenty product---------------------
    if(request.POST['prod_cat'] == 'Wood_Craft'):
        newcraft = Wood_Craft.objects.create(
        craft_name = request.POST['prod_name'],
        description = request.POST['prod_desc'],
        craft_image = request.FILES['craft_img'],
        price = request.POST['prod_price'],
        seller = Users.objects.get(id= request.session['userid'])
        )
        if (request.POST['stock_amount'] != '' ):
            inv = Wood_Craft.objects.get(id = newcraft.id)
            inv.in_stock_num = request.POST['stock_amount']
            inv.save()
        elif (request.POST['made2order'] == "True"):
            inv = Wood_Craft.objects.get(id = newcraft.id)
            inv.on_order = True
            inv.save()
        return redirect(store_front, request.session['userid'])
# Add a jewelry product ------------------------------
    if(request.POST['prod_cat'] == 'Jewelry_Craft'):
        newcraft = Jewelry_Craft.objects.create(
        craft_name = request.POST['prod_name'],
        description = request.POST['prod_desc'],
        craft_image = request.FILES['craft_img'],
        price = request.POST['prod_price'],
        seller = Users.objects.get(id= request.session['userid'])
        )
        if (request.POST['stock_amount'] != '' ):
            inv = Jewelry_Craft.objects.get(id = newcraft.id)
            inv.in_stock_num = request.POST['stock_amount']
            inv.save()
        elif (request.POST['made2order'] == True):
            inv = Jewelry_Craft.objects.get(id = newcraft.id)
            inv.on_order = True
            inv.save()
        return redirect(store_front, request.session['userid'])
        # New Digital product---------------------------
    if(request.POST['prod_cat'] == 'Digital_Craft'):
        newcraft = Digital_Craft.objects.create(
        craft_name = request.POST['prod_name'],
        description = request.POST['prod_desc'],
        craft_image = request.FILES['craft_img'],
        price = request.POST['prod_price'],
        seller = Users.objects.get(id= request.session['userid'])
        )
        if (request.POST['stock_amount'] != '' ):
            inv = Digital_Craft.objects.get(id = newcraft.id)
            inv.in_stock_num = request.POST['stock_amount']
            inv.save()
        elif (request.POST['made2order'] == "True"):
            inv = Digital_Craft.objects.get(id = newcraft.id)
            inv.on_order = True
            inv.save()
        return redirect(store_front, request.session['userid'])

# part of brute forcing decently organized store front.
def delete_cloth(request, val):
    c = Textile_Craft.objects.get(id=val)
    c.delete()
    return redirect(store_front, request.session['userid']) 

def delete_leather(request, val):
    craft = Leather_Craft.objects.get(id=val)
    craft.delete()
    return redirect(store_front, request.session['userid']) 

def delete_metal(request, val):
    craft = Metal_Craft.objects.get(id=val)
    craft.delete()
    return redirect(store_front, request.session['userid']) 

def delete_wood(request, val):
    craft = Wood_Craft.objects.get(id=val)
    craft.delete()
    return redirect(store_front, request.session['userid']) 

def delete_jewel(request, val):
    craft = Jewelry_Craft.objects.get(id=val)
    craft.delete()
    return redirect(store_front, request.session['userid']) 
    
def delete_digi(request, val):
    craft = Digital_Craft.objects.get(id=val)
    craft.delete()
    return redirect(store_front, request.session['userid']) 
    