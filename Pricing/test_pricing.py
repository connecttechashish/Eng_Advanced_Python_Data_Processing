import pricing

def test_member_price():
    assert pricing.member_price(1000, 10) == 900.0      # normal
    assert pricing.member_price(1000, 0) == 1000.0      # zero discount
    assert pricing.member_price(1000, 100) == 0.0       # full discount

def test_add_gst():
    assert pricing.add_gst(1000, 5) == 1050.0           # normal
    assert pricing.add_gst(1000, 0) == 1000.0           # zero GST

def test_delivery_fee():
    assert pricing.delivery_fee(600) == 0               # free above threshold
    assert pricing.delivery_fee(500) == 0               # boundary case
    assert pricing.delivery_fee(499) == 40              # below threshold

def test_loyalty_points():
    assert pricing.loyalty_points(950) == 9             # normal
    assert pricing.loyalty_points(99) == 0              # below first point
    assert pricing.loyalty_points(100) == 1             # boundary
