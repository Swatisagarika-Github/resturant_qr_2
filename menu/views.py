from django.shortcuts import render, redirect
from .models import MenuItem, Order
import qrcode
from io import BytesIO
import base64

# ---------- Step 3: QR Code View ----------
def qr_code_view(request):
    """
    Display a public QR code.
    Scanning this QR code opens the table selection page.
    """
    url = request.build_absolute_uri('/select_table/')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'menu/qr_code.html', {'qr_code': img_str})


# ---------- Step 4: Table Selection ----------
def select_table(request):
    """
    Page for customer to select their table number after scanning the QR code.
    """
    if request.method == "POST":
        table_no = request.POST.get("table_no")
        return redirect(f"/menu/{table_no}/")  # Redirect to menu for the table
    return render(request, 'menu/select_table.html')


# ---------- Step 5: Show Menu and Place Order ----------
def show_menu(request, table_no):
    """
    Display menu items for the customer and allow placing an order.
    """
    items = MenuItem.objects.all()

    if request.method == "POST":
        selected_items = request.POST.getlist("items")
        order = Order.objects.create(table_no=table_no)
        order.items.set(selected_items)
        order.save()
        return render(request, 'menu/order_success.html', {'table_no': table_no})

    return render(request, 'menu/menu.html', {'items': items, 'table_no': table_no})


# ---------- Step 6: Kitchen Display ----------
def kitchen_display(request):
    """
    Display all pending orders on the kitchen screen.
    """
    orders = Order.objects.filter(status="Pending").order_by('timestamp')
    return render(request, 'menu/kitchen.html', {'orders': orders})