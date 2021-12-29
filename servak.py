def get_vat(payment, persent=20):
    try:
    	payment = float(payment)
    	vat = payment / 100 * persent
    	vat = round(vat, 2) 
    	return "Sun VAT: {}".format(vat) 
    except TypeError:
    	return "cant count. chek"

result = get_vat(400, 25) 
print(result)