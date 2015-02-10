from 臺灣言語平臺.資料組模型 import 資料組表

def __揣平臺項目():
	pass

def __照修改紀錄整理文本(文本):
	文本陣列=[]
	文本修改紀錄={}
	while 文本:
		文本結果={'編號':文本.編號(),'項目':'文本'}
		文本結果.update(__揣平臺項目(文本))
		編號=文本.項目.編號()
		if 編號 in 文本修改紀錄:
			所在=文本修改紀錄.pop(編號)
		else:
			所在=len(文本陣列)
			文本陣列.append([])
		改做=文本.項目.改做.first()
		if 改做:
			後一个編號=改做.新
			文本修改紀錄[編號]=後一个編號
		文本陣列[所在].append(文本結果)
		校對=文本.校對表
		if 校對:
			文本=校對.新文本
		else:
			文本=None

#華語/母語音/母語字
def 看外語資料組(資料組編號):
	外語=資料組表.objects.get(pk=資料組編號).外語
	外語結果={'編號':外語.編號(),'項目':'外語'}
	外語結果.update(__揣平臺項目(外語))
	影音陣列=[]
	for 影音 in 外語.翻譯影音.影音\
			.order('評分總合表_正規化結果').order('-評分總合表_分數'):
		影音結果={'編號':影音.編號(),'項目':'影音'}
		影音結果.update(__揣平臺項目(影音))
		文本=影音.影音文本.文本.first()
		影音結果['對應資料']=__照修改紀錄整理文本(文本)#
		影音陣列.append(影音結果)

#華語/母語字
def 看平行語料資料組(資料組編號):
	外語=資料組表.objects.get(pk=資料組編號).外語
	外語結果={'編號':外語.編號(),'項目':'外語'}
	外語結果.update(__揣平臺項目(外語))
	外語結果['對應資料']=__照修改紀錄整理文本(外語.翻譯文本.文本)

#母語音/母語字
def 看影音拍字資料組(資料組編號):
	影音=資料組表.objects.get(pk=資料組編號).影音
	影音結果={'編號':影音.編號(),'項目':'影音'}
	影音結果.update(__揣平臺項目(影音))
	影音結果['對應資料']=__照修改紀錄整理文本(影音.影音文本.文本)

#母語字
def 看正規化資料組(資料組編號):
	文本=資料組表.objects.get(pk=資料組編號).文本
	文本結果={'編號':文本.編號(),'項目':'文本'}
	文本結果.update(__揣平臺項目(文本))
	對應文本=文本.文本校對.新文本
	文本結果['對應資料']=__照修改紀錄整理文本(對應文本)

		