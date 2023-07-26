from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


categories = ['https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/ovoshchi', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/frukti', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/zelen-salati', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/yagodi', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/gribi', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/orekhi-sukhofrukti-semechki', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/zamorozhennie-smesi', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/ovoshchnie-konservi', 'https://sbermarket.ru/magnit_express/c/ovoshchi-frukti-orekhi/fruktovie-yagodnie-konservi', 'https://sbermarket.ru/magnit_express/c/sladosti_new/pechene-pryaniki-sushki', 'https://sbermarket.ru/magnit_express/c/sladosti_new/konfeti', 'https://sbermarket.ru/magnit_express/c/sladosti_new/shokolad-batonchiki-365e745', 'https://sbermarket.ru/magnit_express/c/sladosti_new/vipechka-pirogi-keksi', 'https://sbermarket.ru/magnit_express/c/sladosti_new/torti-pirozhnie', 'https://sbermarket.ru/magnit_express/c/sladosti_new/marmelad-zefir-khalva', 'https://sbermarket.ru/magnit_express/c/sladosti_new/med-varene-siropi', 'https://sbermarket.ru/magnit_express/c/sladosti_new/zhevatelnaya-rezinka', 'https://sbermarket.ru/magnit_express/c/sladosti_new/morozhenoe', 'https://sbermarket.ru/magnit_express/c/sladosti_new/den-shokolada-1f7e6ce', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/moloko-slivki', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/siyri', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/kislomolochnie-produkti', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/smetana', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/tvorog-tvorozhnaya-massa', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/maslo-slivochnoe-margarin-29c3879', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/jogurti-tvorozhki-a7e4c19', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/deserti-sgushchenka-sirki-4109a2d', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/morozhenoe', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/yajtsa', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/maionez', 'https://sbermarket.ru/magnit_express/c/moloko-sir-yajtsa-rastitelnie-produkti-8f15252/detskie-molochnie-produkti', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/ptitsa', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/myaso', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/polufabrikati-iz-myasa-ptitsi', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/subprodukti', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/pelmeni-manti', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/konservi-iz-myasa', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/rastitelnoe-myaso', 'https://sbermarket.ru/magnit_express/c/miaso-ptitsa/shashlik-kupati-d9c63aa', 'https://sbermarket.ru/magnit_express/c/kolbasi-sosiski-delikatesy/kolbasi', 'https://sbermarket.ru/magnit_express/c/kolbasi-sosiski-delikatesy/sosiski-sardelki', 'https://sbermarket.ru/magnit_express/c/kolbasi-sosiski-delikatesy/vetchina-delikatesi', 'https://sbermarket.ru/magnit_express/c/kolbasi-sosiski-delikatesy/pashteti-kholodtsi', 'https://sbermarket.ru/magnit_express/c/kolbasi-sosiski-delikatesy/vyazanka', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/riiba', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/moreprodukti', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/solenaya-kopchenaya-riba', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/ikrra', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/krabovie-palochki-myaso', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/zakuski-iz-ribi-moreproduktov', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/konservi-iz-ribi', 'https://sbermarket.ru/magnit_express/c/riba-moreprodukti-new-new/sushenaya-riba-kalmari', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/morozhenoe-sladosti-5810632', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/pelmeni-vareniki', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/naggetsi-kotleti-myaso-27ed313', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/riba-krevetki-palochki-187318d', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/blini-oladi-sirniki', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/pitstsa-osnova-7c334f5', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/supi-vtorie-blyuda-d267b28', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/khleb-vipechka-testo-a0be669', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/ovoshchi-smesi-gribi', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/frukti-yagodi', 'https://sbermarket.ru/magnit_express/c/zamorozhennie-produkti-copy/goryachaya-shtuchka', 'https://sbermarket.ru/magnit_express/c/bakaleya/makaroni-pasta', 'https://sbermarket.ru/magnit_express/c/bakaleya/krupi-gorokh', 'https://sbermarket.ru/magnit_express/c/bakaleya/sakhar-sol', 'https://sbermarket.ru/magnit_express/c/bakaleya/khlopya-myusli-otrubi', 'https://sbermarket.ru/magnit_express/c/bakaleya/produkti-bistrogo-prigotovleniya', 'https://sbermarket.ru/magnit_express/c/bakaleya/muka', 'https://sbermarket.ru/magnit_express/c/bakaleya/dlya-vipechki-desertov', 'https://sbermarket.ru/magnit_express/c/khleb-khlebtsi-vipechka/svezhaya-vipechka', 'https://sbermarket.ru/magnit_express/c/khleb-khlebtsi-vipechka/khleb-lavash-lepeshki', 'https://sbermarket.ru/magnit_express/c/khleb-khlebtsi-vipechka/khlebtsi-tartaletki', 'https://sbermarket.ru/magnit_express/c/khleb-khlebtsi-vipechka/kruassani-pirogi-vipechka-testo-4e169c7', 'https://sbermarket.ru/magnit_express/c/khleb-khlebtsi-vipechka/sushki-sukhari', 'https://sbermarket.ru/magnit_express/c/gotovaya-eda-copy/zavtraki', 'https://sbermarket.ru/magnit_express/c/gotovaya-eda-copy/salati-zakuski', 'https://sbermarket.ru/magnit_express/c/gotovaya-eda-copy/vtorie-blyuda', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/voda', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/gazirovannie-napitki', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/soki-nektari-morsi', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/kvas', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/morsi-kiseli-kompoti', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/energeticheskie-napitki', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/kholodnij-chaj-kofe', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/bezalkogolnoe-pivo-vino', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/rastitelnie-napitki', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/svyatoj-istochnik-letnie-khiti-7a9f32b', 'https://sbermarket.ru/magnit_express/c/voda-soki-napitki-copy/prokhlada-so-vkusom-rich-eb356f5', 'https://sbermarket.ru/magnit_express/c/chaj-kofe-n2/chaj-0d1bd55', 'https://sbermarket.ru/magnit_express/c/chaj-kofe-n2/rastvorimij-kofe-1571891', 'https://sbermarket.ru/magnit_express/c/chaj-kofe-n2/molotij-zernovoj-kofe-1054f02', 'https://sbermarket.ru/magnit_express/c/chaj-kofe-n2/kakao-tsikorij-50d3ce5', 'https://sbermarket.ru/magnit_express/c/chaj-kofe-n2/kofejnie-koktejli-c85c60b', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/sousi-zapravki', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/rastitelnie-masla', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/spetsii-panirovka-sukhie-buloni', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/ketchup', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/gorchitsa-khren-adzhika', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/majonez', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/marinadi-uksus', 'https://sbermarket.ru/magnit_express/c/sousi-spetsii-maslo/sakhar-sol-test-lenta-2', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/chipsi', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/sukhariki-grenki', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/kukuruznie-palochki-popkorn', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/khlebtsi-kreker', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/batonchiki', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/sukhofrukti-ovoshchnie-sneki', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/orekhi-semechki', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/sushenaya-riba-kalmari-copy', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/myasnie-sneki', 'https://sbermarket.ru/magnit_express/c/chipsi-sneki-sukhofrukti/chipsi-i-solomka-lorenz-590f054', 'https://sbermarket.ru/magnit_express/c/konservi-solenya-copy/ovoshchnie-konservi-gribi', 'https://sbermarket.ru/magnit_express/c/konservi-solenya-copy/kukuruza-goroshek-fasol', 'https://sbermarket.ru/magnit_express/c/konservi-solenya-copy/olivki-maslini-kapersi_test', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/poleznij-perekus', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/vegetariantsam', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/bez-glyutena', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/bez-laktozi', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/sladosti-bez-sakhara', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/diabeticheskie-produkti', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/sportivnoe-pitanie-badi-superfudi', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/organicheskie-produkti', 'https://sbermarket.ru/magnit_express/c/zdorovoe-pitanie/ekologichnaya-bitovaya-khimiya-dubl', 'https://sbermarket.ru/magnit_express/c/spetspredlozheniya-magnit/mestnie-proizvoditeli', 'https://sbermarket.ru/magnit_express/c/retsepti/letnie-retsepti-a4cbd34', 'https://sbermarket.ru/magnit_express/c/melochi-vozle-kassi/zhevatelnie-rezinki', 'https://sbermarket.ru/magnit_express/c/melochi-vozle-kassi/shokolad-batonchiki-new', 'https://sbermarket.ru/magnit_express/c/melochi-vozle-kassi/gazirovannie-napitki-voda', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/sredstva-dlya-stirki', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/konditsioneri-opolaskivateli', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/otbelivateli-pyatnovivoditeli', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/sredstva-dlya-mitya-posudi', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/chistyashchie-sredstva', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/inventar-dlya-uborki', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/ukhod-za-obuvyu-odezhdoj-copy', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/osvezhiteli-aromatizatori', 'https://sbermarket.ru/magnit_express/c/bitovaya-himiya-uborka-/sredstva-ot-nasekomikh-grizunov', 'https://sbermarket.ru/magnit_express/c/kosmetika-gigiena2/gotovimsya-k-otpusku', 'https://sbermarket.ru/magnit_express/c/kosmetika-gigiena2/lichnaya-gigiena', 'https://sbermarket.ru/magnit_express/c/kosmetika-gigiena2/ukhod-za-litsom', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/korma-dlya-koshek', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/korma-dlya-sobak', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/zdorovij-ratsion-dlya-vashego-pitomtsa-2e5a215', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/napolniteli-pelenki-lotki', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/ukhod-zdorove', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/aksessuari-igrushki', 'https://sbermarket.ru/magnit_express/c/tovari-dlya-zhivotnikh/lyubimie-korma-i-lakomstva-df8a790', 'https://sbermarket.ru/magnit_express/c/detskie-tovari_supermarket/detskoe-pitanie', 'https://sbermarket.ru/magnit_express/c/detskie-tovari_supermarket/podguzniki-pelenki', 'https://sbermarket.ru/magnit_express/c/detskie-tovari_supermarket/gigiena-ukhod', 'https://sbermarket.ru/magnit_express/c/detskie-tovari_supermarket/igrushki-tvorchestvo', 'https://sbermarket.ru/magnit_express/c/dom-kukhnya-7f6da39/uborka-khranenie-tekstil-ab1a617', 'https://sbermarket.ru/magnit_express/c/dom-kukhnya-7f6da39/kukhnya-8c4f970', 'https://sbermarket.ru/magnit_express/c/dom-kukhnya-7f6da39/vannaya-komnata-3e00a39', 'https://sbermarket.ru/magnit_express/c/dom-kukhnya-7f6da39/dekor-tovari-dlya-prazdnika-f82c51f', 'https://sbermarket.ru/magnit_express/c/dom-kukhnya-7f6da39/elektrotovari-8c13b78', 'https://sbermarket.ru/magnit_express/c/dom-kukhnya-7f6da39/remont-avtotovari-810e4b1', 'https://sbermarket.ru/magnit_express/c/dacha-sad-super/mangali-shampuri-reshetki', 'https://sbermarket.ru/magnit_express/c/dacha-sad-super/piknik-otdikh-na-prirode', 'https://sbermarket.ru/magnit_express/c/dacha-sad-super/zashchita-ot-nasekomikh-i-grizunov', 'https://sbermarket.ru/magnit_express/c/dacha-sad-super/semena-lukovitsi-rassada', 'https://sbermarket.ru/magnit_express/c/dacha-sad-super/sadovij-inventar-instrumenti', 'https://sbermarket.ru/magnit_express/c/odezhda-obuv-aksessuari/ukhod-za-obuvyu-i-odezhdoj', 'https://sbermarket.ru/magnit_express/c/odezhda-obuv-aksessuari/noski-golfi-getri', 'https://sbermarket.ru/magnit_express/c/odezhda-obuv-aksessuari/kolgotki-chulki', 'https://sbermarket.ru/magnit_express/c/odezhda-obuv-aksessuari/aksessuari', 'https://sbermarket.ru/magnit_express/c/odezhda-obuv-aksessuari/sumki-ryukzaki-chemodani']
#categories = ['ovoshchi-frukti-orekhi/ovoshchi', 'ovoshchi-frukti-orekhi/frukti', 'ovoshchi-frukti-orekhi/frukti', 'ovoshchi-frukti-orekhi/yagodi', 'ovoshchi-frukti-orekhi/gribi', 'orekhi-sukhofrukti-semechki', 'ovoshchi-frukti-orekhi/zamorozhennie-smesi', '/magnit_express/c/ovoshchi-frukti-orekhi/ovoshchnie-konservi', 'ovoshchi-frukti-orekhi/fruktovie-yagodnie-konservi', 'sladosti_new/pechene-pryaniki-sushki', 'sladosti_new/konfeti', 'sladosti_new/shokolad-batonchiki-365e745', 'sladosti_new/vipechka-pirogi-keksi', 'sladosti_new/torti-pirozhnie', 'sladosti_new/marmelad-zefir-khalva', 'sladosti_new/med-varene-siropi',  'sladosti_new/zhevatelnaya-rezinka', 'sladosti_new/morozhenoe', 'sladosti_new/den-shokolada-1f7e6ce', ''  ]
s = Service(executable_path=r'C:\Users\Betwist\PycharmProjects\parserv2\chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(service=s, options=options)

for link in categories:
    url = link
    try:
        driver.maximize_window()
        driver.get(url=url)
        time.sleep(10)
        try:
            pagesCount = driver.find_element(By.CLASS_NAME, 'pagination_last__Ft3WQ')
            print(pagesCount.text)
            time.sleep(1)
            for _ in range(int(pagesCount.text)*2):
                driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
                time.sleep(3)
                try:
                    driver.find_element(By.CLASS_NAME, 'ProductsGrid_buttonWrapper__VC_Ki').click()
                except:
                    print('Кнопки или страниц больше нет')
        except:
            for _ in range(5):
                try:
                    driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
                    time.sleep(3)
                    driver.find_element(By.CLASS_NAME, 'ProductsGrid_buttonWrapper__VC_Ki').click()
                except:
                    print('Кнопки или страниц больше нет')
        # driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
        # time.sleep(2)
        # driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
        # time.sleep(222)
        #cat =driver.find_elements(By.CLASS_NAME, 'ProductCard_withNewStyledQuantityInput__lc_0A')
        cat = driver.find_elements(By.CLASS_NAME, 'ProductCard_withNewStyledQuantityInput__lc_0A')

        for item in cat:
            item.click()
            driver.implicitly_wait(15)
            title = driver.find_element(By.CLASS_NAME, 'ProductTitle_title__aJyqe')
            print(f'Товар: {title.text}')
                #a = driver.find_element(By.CLASS_NAME, 'Price_original__ScjXY')
                #print(f'Цена без скидки: {a.text}')
                # try:
            price = driver.find_element(By.CLASS_NAME, 'PriceContent_price__8BKOP')
            print(f'Цена : {price.text}')
                # except:
                #     b = driver.find_element(By.CLASS_NAME, 'PriceContent_price__8BKOP')
                #     print(f'Цена текущая: {b.text}')
                # driver.implicitly_wait(5)
            #price2 = driver.find_element(By.CLASS_NAME, 'ProductCard_title__iNsaD')

            #title2 = driver.find_element(By.CLASS_NAME, 'ProductCardPrice_price__Kv7Q7')
            #print(f'Товар: {title2.text}')
            #print(f'Цена : {price2.text}')
            driver.find_element(By.CLASS_NAME, 'styles_btnFloatRight__RkQAo').click()
            driver.implicitly_wait(5)
                #driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
                #driver.implicitly_wait(5)
                #cat =driver.find_elements(By.CLASS_NAME, 'ProductCard_withNewStyledQuantityInput__lc_0A')






        #time.sleep(300)
        # for i in range(0, 10):
        #     cat[i].click()
        #     driver.implicitly_wait(5)
        #     driver.back()
        #     driver.implicitly_wait(5)
        #     cat = driver.find_elements(By.CLASS_NAME, 'ProductCard_title__iNsaD')
        #     driver.implicitly_wait(5)
            #print(i.text)
            #print(a.text)
            #driver.implicitly_wait(5)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
