#檢查檔案是否在電腦裡面
import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f: #讀取f的每一行
			if "商品,價格" in line:
				continue #如果商品、價格在行裡面的話，就跳到下一個for loop
			name, price = line.strip().split(",") #字串可以用split去做切割
			products.append([name, price]) #製造一個小清單
	return products	

# 使用者輸入
def user_input(products):
	while True:
		name = input("請輸入商品名稱")
		if name == "q":
			break
		#離開ｗhile loop
		price = input("請輸入商品價格") #如果是quit，則直接break,
		price = int(price)
		p = [name, price] #將商品名稱和價格存成清單
		products.append(p)
	print(products)
	return products

#分別印出商品與價格
def print_products(products):
	for p in products:
		print(p[0], "的價格是", p[1])
	#沒有改變或者增加任何東西，故不需要使用return

#寫到檔案
def write_file(filename, products):
	with open(filename, "w", encoding = "utf-8" ) as f: #只有打開檔案
		f.write("商品,價格\n") #加入商品與價格變成第一行 
		for p in products: #function 內無declare此參數，需要傳遞Pass in 
			f.write(p[0] + "," + str(p[1]) + "\n") #只有寫入檔案
			# csv檔案通用逗點做區隔
			#由於此時price是數字，不能通過加號做相加，因此
			#此時，需要使用type casting str(p[1])

	#僅是寫入檔案，不需要回傳結果

#才開始執行功能(主要的執行程式碼)
def main(): 
	filename = "products.csv"
	if os.path.isfile(filename): #不會重複使用
		print("找到檔案!")
		products = read_file(filename)
	else:
		print("無法找到檔案")

	products = user_input(products)
	print_products(products)
	write_file("products.csv", products)


main() #使用main function  #程式的進入點