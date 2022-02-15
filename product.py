products = []
while True:
	name = input("請輸入商品名稱")
	if name == "q":
		break
	#離開ｗhile loop
	price = input("請輸入商品價格") #如果是quit，則直接break,
	p = [name, price] #將商品名稱和價格存成清單
	products.append(p)
print(products)


