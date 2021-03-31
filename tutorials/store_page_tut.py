
import requests 


url = "https://yandex.ru/turbo?text=https%3A%2F%2Fitsmycity.ru%2F2012-04-09%2Fbiznes-lanch-nedeli-seazone"

url = 'https://itsmycity.ru/2019-09-13/7-prichin-pobyvat-na-festivale-love-your-health-v-ekaterinburg'

#https://sergey-57776.medium.com/%D0%BA-%D0%BC%D0%B5%D0%B4%D0%B8%D0%B0%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F%D0%BC-%D0%BD%D0%B0%D1%81%D0%B5%D0%BA%D0%BE%D0%BC%D1%8B%D1%85-%D0%B2%D0%B8%D1%80%D1%83%D1%81%D0%BE%D0%B2-%D0%B8-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2-ada7daecda87


r = requests.get(url)
print ('requesr code:', r.status_code)  # Status code of response

data = r.content.decode()


file_name = 'save_page_2' 

savefile = f'./{file_name}.txt'

f = open(savefile, 'w', encoding="utf-8")

f.write(data)
#print(data)
f.close()

print('file saved')