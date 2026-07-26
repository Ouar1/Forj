with open("main.py", "r") as f:
    c = f.read()

old = 'logger.info("Admin user created")'
new = """logger.info("Admin user created")
        from models.price_range import PriceRange
        if db.query(PriceRange).count() == 0:
            import modules.routers.admin as admin_mod
            for p in admin_mod.seed_data()["prices"]:
                db.add(p)"""

c = c.replace(old, new)
with open("main.py", "w") as f:
    f.write(c)
print("Patched main.py")