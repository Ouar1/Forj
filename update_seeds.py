with open('modules/routers/admin.py', 'r') as f:
    content = f.read()

pairs = [
    ("800, max_price=2500", "500, max_price=1500"),
    ("2500, max_price=6000", "1500, max_price=4000"),
    ("120, max_price=250", "80, max_price=150"),
    ("1200, max_price=3500", "800, max_price=2500"),
    ("3500, max_price=12000", "2500, max_price=8000"),
    ("600, max_price=2500, []", "400, max_price=1800, []"),
    ("